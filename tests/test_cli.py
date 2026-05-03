from typer.testing import CliRunner
from src.todo_cli.main import app


runner = CliRunner()


def test_add_list(tmp_path):
    # 저장 파일을 임시 경로로 지정하여 기본 동작 확인
    store = tmp_path / "test.json"
    r = runner.invoke(app, ["add", "hello world", "--storage", str(store)])
    assert r.exit_code == 0
    r2 = runner.invoke(app, ["list", "--storage", str(store)])
    assert r2.exit_code == 0
    assert "hello world" in r2.output
