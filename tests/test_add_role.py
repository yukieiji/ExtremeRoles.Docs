import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from add_role import find_role_info, create_role_markdown, format_option_name

# resx content for various roles
CREWMATE_RESX = """<root>
  <data name="Captain" xml:space="preserve"><value>キャプテン</value></data>
  <data name="CaptainSpecificOption" xml:space="preserve"><value>固有オプション1</value></data>
</root>"""
IMPOSTOR_RESX = """<root>
  <data name="Vampire" xml:space="preserve"><value>ヴァンパイア</value></data>
  <data name="VampireAnotherOption" xml:space="preserve"><value>固有オプション2</value></data>
</root>"""
NEUTRAL_RESX = """<root><data name="Jester" xml:space="preserve"><value>ジェスター</value></data></root>"""
COMBINATION_RESX = """<root><data name="Lovers" xml:space="preserve"><value>ラバーズ</value></data></root>"""
GHOST_RESX = """<root>
  <data name="Poltergeist" xml:space="preserve"><value>ポルターガイスト</value></data>
  <data name="PoltergeistSpecificOption" xml:space="preserve"><value>ゴースト固有オプション</value></data>
</root>"""


@pytest.fixture
def mock_resx_dir(tmp_path):
    """Creates a temporary directory with multiple mock resx files."""
    resx_dir = tmp_path / "resx_files"
    resx_dir.mkdir()
    (resx_dir / "Crewmate.resx").write_text(CREWMATE_RESX, encoding="utf-8")
    (resx_dir / "Impostor.resx").write_text(IMPOSTOR_RESX, encoding="utf-8")
    (resx_dir / "Neutral.resx").write_text(NEUTRAL_RESX, encoding="utf-8")
    (resx_dir / "Combination.resx").write_text(COMBINATION_RESX, encoding="utf-8")
    (resx_dir / "GhostCrew.resx").write_text(GHOST_RESX, encoding="utf-8")
    return str(resx_dir)

def test_format_option_name():
    """Tests the option name formatting function."""
    assert format_option_name("TestName") == "Test Name"
    assert format_option_name("AnotherTestName") == "Another Test Name"
    assert format_option_name("lowercase") == "lowercase"
    assert format_option_name("") == ""

def run_and_get_content(role_name: str, mock_resx_dir: str, tmp_path: str) -> str:
    """Helper function to run the script and return the generated content."""
    output_dir = tmp_path / "output"
    role_info = find_role_info(role_name, mock_resx_dir)
    assert role_info is not None
    create_role_markdown(role_info, base_dir=str(output_dir))
    expected_file = output_dir / role_info.type_ja / f"{role_info.name_ja}.md"
    assert expected_file.exists()
    return expected_file.read_text(encoding="utf-8")

def test_crew_options(mock_resx_dir, tmp_path):
    content = run_and_get_content("Captain", mock_resx_dir, tmp_path)
    assert "## オプション" in content
    assert "| スポーン数 |" in content
    assert "| 視界効果を受けるか |" in content
    assert "| Specific Option | 固有オプション1 |" in content
    assert "| キルクールタイム |" not in content

def test_impostor_options(mock_resx_dir, tmp_path):
    content = run_and_get_content("Vampire", mock_resx_dir, tmp_path)
    assert "## オプション" in content
    assert "| スポーン数 |" in content
    assert "| キルクールタイム |" in content
    assert "| Another Option | 固有オプション2 |" in content

def test_neutral_options(mock_resx_dir, tmp_path):
    content = run_and_get_content("Jester", mock_resx_dir, tmp_path)
    assert "## オプション" in content
    assert "| スポーン数 |" in content
    assert "| 視界効果を受けるか |" not in content

def test_combination_options(mock_resx_dir, tmp_path):
    content = run_and_get_content("Lovers", mock_resx_dir, tmp_path)
    assert "## オプション" in content
    assert "| スポーン数 |" in content
    assert "| 視界効果を受けるか |" not in content

def test_ghost_options(mock_resx_dir, tmp_path):
    content = run_and_get_content("Poltergeist", mock_resx_dir, tmp_path)
    assert "## オプション" in content
    assert "| スポーン数 |" not in content
    assert "| Specific Option | ゴースト固有オプション |" in content
