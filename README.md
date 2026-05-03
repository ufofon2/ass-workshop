# todo-cli

간단한 CLI TODO 관리 도구입니다. Python 3.11과 Typer로 작성되었습니다.

빠른 시작

```bash
poetry install
poetry run python -m src.todo_cli.main add "할 일 예시"
poetry run python -m src.todo_cli.main list
```

저장 파일: 기본적으로 현재 작업 디렉터리의 `.todo.json`에 저장됩니다.
