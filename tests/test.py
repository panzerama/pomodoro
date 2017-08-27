import unittest
from core import Task, User


class TaskFeatures(unittest.TestCase):
    def test_can_create_task(self):
        _task = Task("name", 30)
        self.assertEqual(_task.name, "name")
        self.assertEqual(_task.duration, 30)
        self.assertEqual(_task.notes, "")

class UserFeatures(unittest.TestCase):
    def test_can_create_user(self):
        _user = User("John Doe", "john.doe@example.com")
        self.assertEqual(_user.name, "John Doe")
        self.assertEqual(_user.email, "john.doe@example.com")

