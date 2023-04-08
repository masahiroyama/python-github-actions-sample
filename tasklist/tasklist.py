"""tasklist main file as sample application."""
import os
import argparse

import tasklist
from .mgr.task_mgr import TaskManager

parser = argparse.ArgumentParser(description="Task List")

parser.add_argument("-a", "--add", help="add task", metavar="TASK NAME")
parser.add_argument("-l", "--list", help="list tasks", action="store_true")
parser.add_argument(
    "-f",
    "--file",
    help="specify task data path",
    metavar="TASK DATA FILE",
    default="$HOME/.tl/task.json",
)
parser.add_argument(
    "-v", "--version", help="show version", action="store_true"
)

args = parser.parse_args()


def main():
    """Tasklist main method."""

    if args.version:
        print("Version: {}".format(tasklist.__version__))
        return

    data_path = os.path.expandvars(args.file)
    tmgr = TaskManager(data_path)

    if args.add:
        tmgr.add_task(args.add)
        tmgr.write_data(data_path)
