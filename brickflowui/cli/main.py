"""
BrickflowUI CLI — command-line interface for scaffolding and running apps.

Commands:
  brickflowui new <name>    Scaffold a new Databricks App
  brickflowui dev           Run local dev server with hot-reload
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

import typer
app = typer.Typer(
    name="brickflowui",
    help="BrickflowUI — Databricks-first Python UI framework",
    add_completion=False,
    rich_markup_mode="rich",
)

_TEMPLATES_DIR = Path(__file__).parent / "templates"


@app.command()
def new(
    name: str = typer.Argument(..., help="Name of the new Databricks App"),
):
    """
    [bold green]Scaffold[/bold green] a new BrickflowUI Databricks App.

    Creates a folder with app.py, app.yaml, requirements.txt, and .env.example.
    """
    target = Path.cwd() / name
    if target.exists():
        typer.echo(f"[ERROR] Directory '{name}' already exists.", err=True)
        raise typer.Exit(1)

    target.mkdir()

    template_dir = _TEMPLATES_DIR / "default"

    for fn in template_dir.iterdir():
        dest = target / fn.name
        shutil.copy(fn, dest)
        # Replace placeholder app name in files
        content = dest.read_text(encoding="utf-8")
        content = content.replace("{{APP_NAME}}", name)
        dest.write_text(content, encoding="utf-8")

    typer.echo(f"""
[bold green]✓ Created BrickflowUI app:[/bold green] {name}/

  [bold]Files created:[/bold]
    {name}/app.py           → Root app & pages
    {name}/app.yaml         → Databricks Apps config
    {name}/requirements.txt → Python dependencies
    {name}/.env.example     → Environment variables template

  [bold]Next steps:[/bold]
    cd {name}
    cp .env.example .env
    # Edit .env with your DATABRICKS_HOST and DATABRICKS_TOKEN
    brickflowui dev
""")


@app.command()
def dev(
    file: str = typer.Option("app.py", "--file", "-f", help="App entry point file"),
    port: int = typer.Option(8050, "--port", "-p", help="Dev server port"),
    reload: bool = typer.Option(True, "--reload/--no-reload", help="Enable hot reload"),
):
    """
    [bold blue]Run[/bold blue] the local development server with hot-reload.
    """
    app_file = Path.cwd() / file
    if not app_file.exists():
        typer.echo(f"[ERROR] {file} not found in current directory.", err=True)
        raise typer.Exit(1)

    typer.echo(f"[bold]BrickflowUI Dev Server[/bold] → http://localhost:{port}")
    typer.echo("Press Ctrl+C to stop.\n")

    os.environ.setdefault("BRICKFLOWUI_DEV", "1")

    if reload:
        import uvicorn
        # Import the app module and get the ASGI app
        spec_name = app_file.stem
        sys.path.insert(0, str(Path.cwd()))

        # Use uvicorn reload with the module path
        uvicorn.run(
            f"{spec_name}:app.server",
            host="0.0.0.0",
            port=port,
            reload=True,
            reload_dirs=[str(Path.cwd())],
        )
    else:
        import subprocess
        subprocess.run([sys.executable, file])


if __name__ == "__main__":
    app()
