# Rakefile
namespace :test do
  desc "Run validation checks for the Jekyll site (title and nav_order duplicates)"
  task :site do
    puts "Running site validation checks (title/nav_order duplicates) using Ruby script..."
    success = system("ruby scripts/check_site.rb")
    if success
      puts "Site validation checks passed."
    else
      puts "Site validation checks failed."
      exit 1 # Rakeタスクを失敗させる
    end
  end
end

# デフォルトタスクとしてtest:siteを設定することも可能
# task default: "test:site"
