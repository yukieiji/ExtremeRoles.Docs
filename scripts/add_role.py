import os
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass

from jsonargparse import auto_cli

@dataclass
class RoleInfo:
    name_ja: str
    name_en: str
    type_ja: str
    options: list[dict[str, str]]
    full_description: str | None

ROLE_TYPE_MAP: dict[str, str] = {
    "Crewmate": "クルー",
    "Impostor": "インポスター",
    "Neutral": "ニュートラル",
    "Combination": "コンビネーション役職",
    "GhostCrew": "ゴーストクルー",
    "GhostImpostor": "ゴーストインポスター",
    "GhostNeutral": "ゴーストニュートラル",
}

BLACKLISTED_SUFFIXES: list[str] = ["FullDescription", "IntroDescription", "ShortDescription"]

def find_role_info(name_en: str, resx_dir: str) -> RoleInfo | None:
    """
    Searches .resx files to find role information, including options and description.
    """
    if not os.path.isdir(resx_dir):
        return None

    for filename in os.listdir(resx_dir):
        if not filename.endswith(".resx"):
            continue
        file_path = os.path.join(resx_dir, filename)
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            main_role_node = root.find(f".//data[@name='{name_en}']")
            if main_role_node is None:
                continue

            name_ja_node = main_role_node.find("value")
            if name_ja_node is None or name_ja_node.text is None:
                continue
            name_ja = name_ja_node.text

            role_type_en = os.path.splitext(filename)[0]
            type_ja = ROLE_TYPE_MAP.get(role_type_en)
            if not type_ja:
                continue

            options: list[dict[str, str]] = []
            full_description: str | None = None

            for data_node in root.findall(".//data"):
                node_name = data_node.get("name")
                if not node_name:
                    continue
                if not node_name.lower().startswith(name_en.lower()):
                    continue
                if node_name.lower() == name_en.lower():
                    continue

                if node_name.endswith("FullDescription"):
                    description_node = data_node.find("value")
                    if description_node is not None:
                        full_description = description_node.text
                    continue

                if any(node_name.endswith(suffix) for suffix in BLACKLISTED_SUFFIXES):
                    continue

                value_node = data_node.find("value")
                if value_node is not None and value_node.text:
                    options.append({"name": node_name, "value": value_node.text})
                    

            return RoleInfo(
                name_ja=name_ja, name_en=name_en, type_ja=type_ja,
                options=options, full_description=full_description
            )

        except ET.ParseError:
            print(f"Warning: Could not parse XML file: {file_path}", file=sys.stderr)
            continue

    return None

def create_role_markdown(role_info: RoleInfo, base_dir: str = "docs/追加役職") -> None:
    """
    Creates a new markdown file for a role, including description and options table.
    Args:
        role_info: parsed role info
        base_dir: The directory to add md
    """
    role_type_dir = os.path.join(base_dir, role_info.type_ja)
    os.makedirs(role_type_dir, exist_ok=True)
    try:
        nav_order = len([f for f in os.listdir(role_type_dir) if f.endswith('.md')]) + 2
    except FileNotFoundError:
        nav_order = 1
    file_path = os.path.join(role_type_dir, f"{role_info.name_ja}.md")
    if os.path.exists(file_path):
        print(f"Error: File '{file_path}' already exists.")
        return

    # --- Dynamically build a single, combined options list ---
    all_option_rows = []

    # First, add common options if applicable
    if "ゴースト" not in role_info.type_ja:
        common_options: list[dict[str, str]] = []
        common_options.append({"name": "スポーン数", "value": "何人この役職にアサインされるか"})

        if role_info.type_ja == "インポスター":
            common_options.append({"name": "別の視界設定を持つか", "value": "ゲームで設定されているインポスターの視界設定と別の視界設定を持つか"})
        else: # Crew, Neutral, Combination, etc.
            common_options.append({"name": "別の視界設定を持つか", "value": "ゲームで設定されているクルーの視界設定と別の視界設定を持つか"})
        
        common_options.append({"name": "ビジョン", "value": "視界の広さ"})
        common_options.append({"name": "視界効果を受けるか", "value": "停電等の視界効果を受けるかどうか"})

        if role_info.type_ja == "インポスター":
            common_options.extend([
                {"name": "別のキルクールタイムを持つか", "value": "ゲームで設定されているキルクールと別のキルクール設定を持つか"},
                {"name": "キルクールタイム", "value": "キルクールタイムの設定"},
                {"name": "別のキルレンジを持つか", "value": "ゲームで設定されているキルレンジと別のキルレンジ設定を持つか"},
                {"name": "キルレンジ", "value": "キルレンジ"}
            ])

        for opt in common_options:
             all_option_rows.append(f"| {opt['name']} | {opt['value']} |")

    # Next, add role-specific options
    if role_info.options:
        for opt in sorted(role_info.options, key=lambda x: x['name']):
            option_text = opt['value'].replace('\n', ' ')
            all_option_rows.append(f"| {option_text} | {option_text} |")

    # Now, build the final table section
    options_section = ""
    if all_option_rows:
        table_header = "| オプション名 | 詳細 |\n| ---- | ---- |"
        table_body = "\n".join(all_option_rows)
        options_section = f"## オプション\n{table_header}\n{table_body}\n"
    else:
        options_section = "## オプション\n\n(オプションなし)\n"

    description_section = role_info.full_description if role_info.full_description else "*説明文が.resxファイルに見つかりませんでした。手動で追加してください。*"

    content = f"""---
layout: default
title: {role_info.name_ja}
nav_order: {nav_order}
grand_parent: 追加役職
parent: {role_info.type_ja if role_info.type_ja != "クルー" else "クルーメイト"}
---

# {role_info.name_ja}

{description_section}

{options_section}
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully created '{file_path}'")

def main(role_name_en: str, resx_dir: str=r"..\\ExtremeRoles\\ExtremeRoles\\Translation\\resx", out_dir: str= r"docs\\追加役職"):
    """Create a new role markdown file by looking up role info in .resx files."

    Args:
        role_name_en: The English name of the role (e.g., Captain).
        resx_dir: The directory containing the .resx localization files.
        out_dir: The directory to add md
    """

    print(f"Searching for English role '{role_name_en}' in directory '{resx_dir}'...")

    role_info = find_role_info(role_name_en, resx_dir)

    if role_info:
        print(f"Found Japanese name: '{role_info.name_ja}'")
        print(f"Found Japanese type: '{role_info.type_ja}'")
        print(f"Found {len(role_info.options)} options.")
        print(f"Found description: {'Yes' if role_info.full_description else 'No'}")
        create_role_markdown(role_info, out_dir)
    else:
        print(f"Error: Could not find role information for '{role_name_en}' in the specified .resx directory.")


if __name__ == "__main__":
    auto_cli(main)
