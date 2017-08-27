import unittest
from core import Task


class TaskFeatures(unittest.TestCase):
    def test_can_create_task(self):
        _task = Task("name", 30)
        self.assertEqual(_task.name, "name")
        self.assertEqual(_task.duration, 30)
