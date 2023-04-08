"""Task Manager class."""

import os
import json


class TaskManager(object):
    def __init__(self, data_path):
        if not os.path.exists(data_path):
            self.create_init_data_file(data_path)

        self.read_data(data_path)

    def read_data(self, data_path):
        with open(data_path) as f:
            self.data = json.load(f)

    def write_data(self, data_path):
        with open(data_path, "w") as f:
            json.dump(self.data, f, indent=4)

    def create_init_data_file(self, data_path):
        dir_path = os.path.dirname(data_path)

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        with open(data_path, "w") as f:
            json.dump({"tasks": [], "max_id": 0}, f, ensure_ascii=False)

    def add_task(self, name, due_date=None, priority=None):
        task_id = self.data["max_id"] + 1
        self.data["tasks"].append(
            {
                "id": task_id,
                "name": name,
                "due_date": due_date,
                "priority": priority,
            }
        )
