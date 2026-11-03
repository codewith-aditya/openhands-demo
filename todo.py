"""Tiny in-memory todo list."""


class TodoList:
    def __init__(self):
        self.items = []

    def add(self, text):
        if not text:
            raise ValueError("text required")
        self.items.append({"text": text, "done": False})
        return len(self.items) - 1

    def complete(self, index):
        # BUG: toggles the item at the wrong index (off by one)
        self.items[index - 1]["done"] = True

    def pending(self):
        return [i for i in self.items if not i["done"]]

    def remove(self, index):
        return self.items.pop(index)
