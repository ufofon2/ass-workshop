from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    created_at: str = datetime.utcnow().isoformat()
    due: Optional[str] = None
    priority: Optional[str] = None

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(d: dict):
        return Task(
            id=d["id"],
            title=d["title"],
            completed=d.get("completed", False),
            created_at=d.get("created_at", datetime.utcnow().isoformat()),
            due=d.get("due"),
            priority=d.get("priority"),
        )


def next_id(items: list) -> int:
    """현재 항목들에서 사용 가능한 다음 id 반환"""
    if not items:
        return 1
    return max(item["id"] for item in items) + 1
