import json
from pathlib import Path
from datetime import datetime
import typer

from .models import Task, next_id
from .storage import JSONStorage

app = typer.Typer()


def _task_to_dict(t: Task) -> dict:
    return t.to_dict()


@app.command()
def add(title: str = typer.Argument(..., help="할 일 제목"), due: str | None = None, priority: str | None = None, storage: str | None = None):
    """새 할 일 추가"""
    s = JSONStorage(Path(storage) if storage else None)
    items = s.list()
    tid = next_id(items)
    task = Task(id=tid, title=title, completed=False, created_at=datetime.utcnow().isoformat(), due=due, priority=priority)
    s.add(task.to_dict())
    typer.echo(json.dumps(task.to_dict(), ensure_ascii=False))


@app.command()
def list(storage: str | None = None):
    """할 일 목록 출력 (JSON)"""
    s = JSONStorage(Path(storage) if storage else None)
    items = s.list()
    typer.echo(json.dumps(items, ensure_ascii=False, indent=2))


@app.command()
def done(id: int = typer.Argument(..., help="완료할 항목 ID"), storage: str | None = None):
    """항목을 완료로 표시"""
    s = JSONStorage(Path(storage) if storage else None)
    ok = s.update(id, {"completed": True})
    if ok:
        typer.echo(f"marked {id} as done")
    else:
        raise typer.Exit(code=1)


@app.command()
def remove(id: int = typer.Argument(..., help="삭제할 항목 ID"), storage: str | None = None):
    """항목 삭제"""
    s = JSONStorage(Path(storage) if storage else None)
    ok = s.remove(id)
    if ok:
        typer.echo(f"removed {id}")
    else:
        raise typer.Exit(code=1)


def main():
    app()


if __name__ == "__main__":
    main()
