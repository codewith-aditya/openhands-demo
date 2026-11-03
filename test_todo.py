import unittest

from todo import TodoList


class TestTodo(unittest.TestCase):
    def test_complete_marks_the_right_item(self):
        todos = TodoList()
        todos.add("buy milk")
        todos.add("write code")
        todos.complete(1)
        self.assertTrue(todos.items[1]["done"], "index 1 should be done")
        self.assertFalse(todos.items[0]["done"], "index 0 should stay pending")

    def test_pending_excludes_completed(self):
        todos = TodoList()
        todos.add("a")
        todos.add("b")
        todos.complete(0)
        self.assertEqual([t["text"] for t in todos.pending()], ["b"])


if __name__ == "__main__":
    unittest.main()
