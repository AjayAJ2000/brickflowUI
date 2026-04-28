"""
BrickflowUI CLI for scaffolding and running apps.

Commands:
  brickflowui new <name>    Scaffold a new Databricks App
  brickflowui dev           Run the local dev server with hot reload
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import typer

app = typer.Typer(
    name="brickflowui",
    help="BrickflowUI - Databricks-first Python UI framework",
    add_completion=False,
    rich_markup_mode="rich",
)

_TEMPLATES_DIR = Path(__file__).parent / "templates"


@app.command()
def new(
    name: str = typer.Argument(..., help="Name of the new Databricks App"),
):
    """
    Scaffold a new BrickflowUI Databricks App.

    Creates a folder with app.py, app.yaml, requirements.txt, and .env.example.
    """
    target = Path.cwd() / name
    if target.exists():
        typer.echo(f"[ERROR] Directory '{name}' already exists.", err=True)
        raise typer.Exit(1)

    template_dir = _TEMPLATES_DIR / "default"
    target.mkdir(parents=True)

    for template_file in template_dir.iterdir():
        if not template_file.is_file():
            continue
        content = template_file.read_text(encoding="utf-8")
        content = content.replace("{{APP_NAME}}", name)
        (target / template_file.name).write_text(content, encoding="utf-8")

    typer.echo(
        f"""
[bold green]Created BrickflowUI app:[/bold green] {name}/

  [bold]Files created:[/bold]
    {name}/app.py           -> Root app and pages
    {name}/app.yaml         -> Databricks Apps config
    {name}/requirements.txt -> Python dependencies
    {name}/.env.example     -> Environment variables template

  [bold]Next steps:[/bold]
    cd {name}
    cp .env.example .env
    # Edit .env with your DATABRICKS_HOST and DATABRICKS_TOKEN
    brickflowui dev
"""
    )


@app.command()
def dev(
    file: str = typer.Option("app.py", "--file", "-f", help="App entry point file"),
    port: int = typer.Option(8050, "--port", "-p", help="Dev server port"),
    reload: bool = typer.Option(True, "--reload/--no-reload", help="Enable hot reload"),
):
    """
    Run the local development server with hot reload.
    """
    app_file = Path.cwd() / file
    if not app_file.exists():
        typer.echo(f"[ERROR] {file} not found in current directory.", err=True)
        raise typer.Exit(1)

    typer.echo(f"[bold]BrickflowUI Dev Server[/bold] -> http://localhost:{port}")
    typer.echo("Press Ctrl+C to stop.\n")

    os.environ.setdefault("BRICKFLOWUI_DEV", "1")

    if reload:
        import uvicorn

        spec_name = app_file.stem
        sys.path.insert(0, str(Path.cwd()))

        uvicorn.run(
            f"{spec_name}:app.server",
            host="0.0.0.0",
            port=port,
            reload=True,
            reload_dirs=[str(Path.cwd())],
        )
    else:
        subprocess.run([sys.executable, file], check=False)


if __name__ == "__main__":
    app()
