import shutil
import uuid
from pathlib import Path

from typer.testing import CliRunner

from brickflowui.cli.main import app


runner = CliRunner()


def test_cli_help_only_shows_supported_commands():
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "new" in result.output
    assert "dev" in result.output
    assert "info" not in result.output
    assert "--template" not in result.output


def test_new_command_scaffolds_default_app(monkeypatch):
    repo_root = Path(__file__).resolve().parents[1]
    scratch_dir = repo_root
    app_name = f"sample_app_{uuid.uuid4().hex[:8]}"

    try:
        monkeypatch.setattr(Path, "cwd", lambda: scratch_dir)
        result = runner.invoke(app, ["new", app_name], catch_exceptions=False)

        assert result.exit_code == 0
        assert (scratch_dir / app_name / "app.py").exists()
        assert (scratch_dir / app_name / "app.yaml").exists()
        assert (scratch_dir / app_name / "requirements.txt").exists()
        assert (scratch_dir / app_name / ".env.example").exists()
    finally:
        shutil.rmtree(scratch_dir, ignore_errors=True)
