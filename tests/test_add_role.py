import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from add_role import find_role_info, create_role_markdown

# resx content for a Crewmate role with specific options
CREWMATE_RESX = """<root>
  <data name="Captain" xml:space="preserve"><value>キャプテン</value></data>
  <data name="CaptainSpecificOption" xml:space="preserve"><value>固有オプション1</value></data>
</root>"""

@pytest.fixture
def mock_resx_dir(tmp_path):
    """Creates a temporary directory with a mock resx file."""
    resx_dir = tmp_path / "resx_files"
    resx_dir.mkdir()
    (resx_dir / "Crewmate.resx").write_text(CREWMATE_RESX, encoding="utf-8")
    return str(resx_dir)

def test_specific_options_use_value_for_both_columns(mock_resx_dir, tmp_path):
    """
    Tests that role-specific options use the <value> text for both the
    'Option Name' and 'Description' columns in the generated table.
    """
    docs_dir = tmp_path / "docs"
    role_info = find_role_info("Captain", mock_resx_dir)
    assert role_info is not None

    create_role_markdown(role_info, base_dir=str(docs_dir / "追加役職"))

    expected_file = docs_dir / "追加役職" / "クルー" / "キャプテン.md"
    content = expected_file.read_text(encoding="utf-8")

    # Check that the common option is formatted normally
    assert "| スポーン数 | 何人この役職にアサインされるか |" in content

    # Check that the specific option has the same value in both columns
    specific_option_value = "固有オプション1"
    expected_row = f"| {specific_option_value} | {specific_option_value} |"
    assert expected_row in content
