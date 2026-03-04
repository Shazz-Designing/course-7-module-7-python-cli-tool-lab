import argparse
from lib.models import User, Task

users = {}


def add_task(username, task_title):
    if username not in users:
        users[username] = User(username)

    task = Task(task_title)
    users[username].add_task(task)


def complete_task(username, task_title):
    if username in users:
        users[username].complete_task(task_title)
    else:
        print("User not found.")


def main():
    parser = argparse.ArgumentParser(description="Task CLI Tool")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add-task")
    add_parser.add_argument("username")
    add_parser.add_argument("task")

    complete_parser = subparsers.add_parser("complete-task")
    complete_parser.add_argument("username")
    complete_parser.add_argument("task")

    args = parser.parse_args()

    if args.command == "add-task":
        add_task(args.username, args.task)

    elif args.command == "complete-task":
        complete_task(args.username, args.task)


if __name__ == "__main__":
    main()