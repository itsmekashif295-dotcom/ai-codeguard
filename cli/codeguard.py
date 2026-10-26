import typer
import requests
from pathlib import Path
import json

app = typer.Typer(help="AI CodeGuard - Detect vulnerabilities in your code.")

@app.command()
def scan(
    file_path: str = typer.Argument(..., help="Path to the Python file you want to scan"),
    api_url: str = typer.Option("http://127.0.0.1:8000/scan/", help="API URL")
):
    """
    Scan a Python file for vulnerabilities.
    """
    path = Path(file_path)
    
    if not path.exists():
        typer.secho(f"❌ Error: File '{file_path}' not found!", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # File read karein
    typer.secho(f"🔍 Scanning {path.name}...", fg=typer.colors.CYAN)
    code = path.read_text(encoding="utf-8")

    # API ko request bhejein
    payload = {
        "code": code,
        "language": "python",
        "filename": path.name
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status() # Agar error (404/500) aaye to exception throw kare
        data = response.json()
    except requests.exceptions.ConnectionError:
        typer.secho("❌ Error: Could not connect to API. Is the server running?", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.secho(f"❌ API Error: {e}", fg=typer.colors.RED, bold=True)
        raise typer.Exit(code=1)

    # Result show karein
    total = data.get("total_findings", 0)
    
    if total == 0:
        typer.secho(f"✅ No vulnerabilities found in {path.name}. Your code is safe!", fg=typer.colors.GREEN, bold=True)
        return

    typer.secho(f"\n⚠️  Found {total} vulnerabilities in {path.name}:\n", fg=typer.colors.YELLOW, bold=True)

    for i, finding in enumerate(data["findings"], 1):
        sev = finding.get('severity', 'UNKNOWN')
        
        # Severity ke hisaab se color
        if sev == "HIGH":
            color = typer.colors.RED
        elif sev == "MEDIUM":
            color = typer.colors.YELLOW
        else:
            color = typer.colors.BLUE

        typer.secho(f"[{i}] Line {finding.get('line')} | {finding.get('cwe')} | ", nl=False)
        typer.secho(f"{sev}", fg=color, bold=True)
        typer.echo(f"    Description: {finding.get('description')}")
        typer.echo(f"    Confidence:  {finding.get('confidence')}\n")

if __name__ == "__main__":
    app()