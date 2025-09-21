import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from add_role import find_role_info, create_role_markdown, RoleInfo

# Sample resx content for testing
CREWMATE_RESX_CONTENT = """<?xml version="1.0" encoding="utf-8"?>
<root>
  <data name="Captain" xml:space="preserve">
    <value>キャプテン</value>
  </data>
  <data name="CaptainAwakeTaskGage" xml:space="preserve">
    <value>キャプテンに覚醒するタスク進捗率</value>
  </data>
  <data name="CaptainFullDescription" xml:space="preserve">
    <value>これは詳細な説明文です。</value>
  </data>
</root>
"""

@pytest.fixture
def mock_resx_dir(tmp_path):
    """Creates a temporary directory with a mock resx file."""
    resx_dir = tmp_path / "resx_files"
    resx_dir.mkdir()
    (resx_dir / "Crewmate.resx").write_text(CREWMATE_RESX_CONTENT, encoding="utf-8")
    return str(resx_dir)

def test_find_role_info_returns_dataclass(mock_resx_dir):
    """Tests that find_role_info returns a RoleInfo object with correct data."""
    role_info = find_role_info("Captain", mock_resx_dir)

    assert isinstance(role_info, RoleInfo)
    assert role_info.name_ja == "キャプテン"
    assert role_info.type_ja == "クルー"
    assert role_info.full_description == "これは詳細な説明文です。"
    assert len(role_info.options) == 1
    assert role_info.options[0]['name'] == "CaptainAwakeTaskGage"

def test_find_role_info_not_found_returns_none(mock_resx_dir):
    """Tests that find_role_info returns None when a role is not found."""
    role_info = find_role_info("NonExistentRole", mock_resx_dir)
    assert role_info is None

def test_full_script_execution_with_dataclass(mock_resx_dir, tmp_path):
    """An integration-style test for the main execution path with the dataclass."""
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()

    role_info = find_role_info("Captain", mock_resx_dir)
    assert role_info is not None

    create_role_markdown(role_info, base_dir=str(docs_dir / "追加役職"))

    expected_file = docs_dir / "追加役職" / "クルー" / "キャプテン.md"
    assert expected_file.exists()
    content = expected_file.read_text(encoding="utf-8")

    assert "これは詳細な説明文です。" in content
    assert "| AwakeTaskGage | キャプテンに覚醒するタスク進捗率 |" in content
