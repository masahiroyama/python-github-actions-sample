"""tasklist main file as sample application."""
import argparse

import tasklist

parser = argparse.ArgumentParser(description='Task List')

parser.add_argument('-a', '--add', help='add task', metavar='TASK NAME')
parser.add_argument('-l', '--list', help='list tasks', action='store_true')
parser.add_argument(
    '-v', '--version', help='show version', action='store_true'
)

args = parser.parse_args()


def main():
    """Tasklist main method."""
    if args.version:
        print('Version: {}'.format(tasklist.__version__))
        return
