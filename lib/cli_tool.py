import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.models import Task, User

users = {}


def get_or_create_user(name):
    if name not in users:
        users[name] = User(name)
    return users[name]


def handle_add_task(args):
    user = get_or_create_user(args.user)
    task = Task(title=args.title)
    user.add_task(task)


def handle_complete_task(args):
    user = get_or_create_user(args.user)
    user.complete_task(args.title)


def handle_list_tasks(args):
    user = get_or_create_user(args.user)
    user.list_tasks()


def handle_add_user(args):
    if args.name in users:
        print("User '" + args.name + "' already exists.")
    else:
        users[args.name] = User(args.name)
        print("User '" + args.name + "' created.")


def handle_list_users(_args):
    if not users:
        print("No users found.")
    else:
        for user in users.values():
            print(str(user))


def build_parser():
    parser = argparse.ArgumentParser(prog="cli_tool", description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_add = subparsers.add_parser("add-task")
    p_add.add_argument("user")
    p_add.add_argument("title")
    p_add.set_defaults(func=handle_add_task)

    p_complete = subparsers.add_parser("complete-task")
    p_complete.add_argument("user")
    p_complete.add_argument("title")
    p_complete.set_defaults(func=handle_complete_task)

    p_list = subparsers.add_parser("list-tasks")
    p_list.add_argument("user")
    p_list.set_defaults(func=handle_list_tasks)

    p_add_user = subparsers.add_parser("add-user")
    p_add_user.add_argument("name")
    p_add_user.set_defaults(func=handle_add_user)

    p_users = subparsers.add_parser("list-users")
    p_users.set_defaults(func=handle_list_users)

    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)