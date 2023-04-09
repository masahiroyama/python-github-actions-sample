import os
import json
import datetime
import pytest

from tasklist.mgr.task_mgr import TaskManager


@pytest.fixture()
def task_mgr(tmpdir):
    file_name = "test.json"
    file_path = os.path.join(tmpdir, file_name)

    task_mgr = TaskManager(file_path)

    yield task_mgr


def test_create_init_data_file(task_mgr):
    data_path = task_mgr.data_path
    task_mgr.create_init_data_file(data_path)

    with open(data_path) as f:
        json_data = json.load(f)

    assert json_data["max_id"] == 0

    assert len(json_data["tasks"]) == 0


def test_add_task(task_mgr):
    task_mgr.add_task("Temp task", due_date="2025/12/31", priority="high")

    assert task_mgr.data["max_id"] == 1

    assert task_mgr.data["tasks"][0]["id"] == 0
    assert task_mgr.data["tasks"][0]["name"] == "Temp task"
    assert task_mgr.data["tasks"][0]["due_date"] == datetime.date(2025, 12, 31)
    assert task_mgr.data["tasks"][0]["priority"] == "high"
