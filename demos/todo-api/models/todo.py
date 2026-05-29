from dataclasses import dataclass


@dataclass
class Todo:
    id: int
    title: str
    description: str
    completed: bool = False

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
