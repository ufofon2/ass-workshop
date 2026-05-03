from pathlib import Path
import json
from typing import List, Optional


class JSONStorage:
    def __init__(self, path: Optional[Path] = None):
        # 기본 저장 파일은 작업 디렉터리의 .todo.json
        self.path = Path(path) if path else Path.cwd() / ".todo.json"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def _read(self) -> List[dict]:
        if not self.path.exists():
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except Exception:
                return []

    def _write(self, items: List[dict]):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)

    def list(self) -> List[dict]:
        return self._read()

    def add(self, item: dict):
        items = self._read()
        items.append(item)
        self._write(items)

    def update(self, id: int, patch: dict) -> bool:
        items = self._read()
        changed = False
        for it in items:
            if it.get("id") == id:
                it.update(patch)
                changed = True
                break
        if changed:
            self._write(items)
        return changed

    def remove(self, id: int) -> bool:
        items = self._read()
        new_items = [it for it in items if it.get("id") != id]
        if len(new_items) == len(items):
            return False
        self._write(new_items)
        return True
