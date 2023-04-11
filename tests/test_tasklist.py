import sys
import os
import json
import pytest
from unittest.mock import patch

from tasklist.tasklist import main


@pytest.fixture
def test_file_path():
    path = "$HOME/.tl/test.json"
    path = os.path.expandvars(path)
    return path


def test_add_task_only_task_name(test_file_path):
    if os.path.exists(test_file_path):
        os.remove(test_file_path)

    with patch(
        "sys.argv", ["tl", "-a", "Temp task name", "-f", test_file_path]
    ):
        main()

        with open(test_file_path) as f:
            data = json.load(f)
            assert data["tasks"][0]["name"] == "Temp task name"
            assert data["tasks"][0]["due_date"] is None
            assert data["tasks"][0]["priority"] is None

        if os.path.exists(test_file_path):
            os.remove(test_file_path)
