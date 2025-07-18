require 'yaml'
require 'find'

def check_duplicates
  errors = []
  titles = Hash.new { |h, k| h[k] = [] }
  nav_orders = Hash.new { |h, k| h[k] = Hash.new { |h2, k2| h2[k2] = [] } }

  # _config.ymlからtitleを読み込む
  begin
    config = YAML.load_file("_config.yml")
    titles[config['title']] << "_config.yml" if config['title']
  rescue Errno::ENOENT
    errors << "エラー: _config.yml が見つかりません。"
  rescue Psych::SyntaxError => e
    errors << "エラー: _config.yml の解析中にエラーが発生しました: #{e.message}"
  end

  # docsディレクトリ内のMarkdownファイルを処理
  Find.find("docs") do |path|
    if path.end_with?(".md") # Removed "&& path.end_with?("追加役職.md")"
      begin
        content = File.read(path)
        # Front matterを抽出
        match = content.match(/---\s*\n(.*?)---\s*\n/m)
        if match
          front_matter_str = match[1]
          front_matter = YAML.safe_load(front_matter_str) || {} # 空の場合を考慮
          titles[front_matter['title']] << path if front_matter['title']
          if front_matter['nav_order']
            base_name = File.basename(path, ".md")
            parent_dir_name = File.basename(File.dirname(path))
            current_parent_dir = File.dirname(path)

            comparison_dir = if base_name == parent_dir_name
                               # 親フォルダと同じ名前のmdファイルの場合、親ディレクトリのnav_orderと比較
                               # 例 : a/b/b.md => b.mdはaフォルダ内のnav_orderと比較
                               File.dirname(current_parent_dir)
                             else
                               # 上記以外は現ディレクトリのnav_orderと比較
                               # 例 : a/b/c.md => c.mdはbフォルダ内のnav_orderと比較
                               current_parent_dir
                             end
            nav_orders[comparison_dir][front_matter['nav_order']] << path
          end
        else
          # errors << "警告: #{path} にFront matterが見つかりません。" # 必要に応じてコメント解除
        end
      rescue Errno::ENOENT
        # errors << "エラー: #{path} が見つかりません。" # bundle exec jekyll build で生成されるファイルもあるので、ファイルがないエラーは無視する
      rescue Psych::SyntaxError => e
        errors << "エラー: #{path} のFront matter解析中にエラーが発生しました: #{e.message}"
      rescue StandardError => e
        errors << "エラー: #{path} の処理中に予期せぬエラーが発生しました: #{e.message}"
      end
    end
  end

  # titleの重複をチェック
  titles.each do |title, paths|
    if paths.size > 1
      errors << "エラー: title '#{title}' が次のファイルで重複しています: #{paths.join(', ')}"
    end
  end

  # nav_orderの重複をチェック
  nav_orders.each do |parent_dir, orders|
    orders.each do |order, paths|
      if paths.size > 1
        errors << "エラー: nav_order '#{order}' がディレクトリ '#{parent_dir}' 内の次のファイルで重複しています: #{paths.join(', ')}"
      end
    end
  end

  errors
end

if __FILE__ == $0
  puts "--- title と nav_order の重複チェック開始 ---"
  validation_errors = check_duplicates
  if validation_errors.any?
    puts "\n--- エラー概要 ---"
    validation_errors.each { |e| puts e }
    puts "--- チェック完了: エラーあり ---"
    exit 1
  else
    puts "--- チェック完了: 問題ありません ---"
  end
end
