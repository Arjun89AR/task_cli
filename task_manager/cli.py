import sys

from task_manager.task_service import (
    add,
    update,
    delete,
    task_list,
    mark_in_progress,
    done,
    todo,
    in_progress,
)


def main():

    if len(sys.argv) < 2:
        print("No command supplied")
        sys.exit()

    command = sys.argv[1]

    # ADD
    if command == "add":

        if len(sys.argv) < 3:
            print("Usage: task-cli add <description>")
            sys.exit()

        description = sys.argv[2]
        add(description)

    # UPDATE
    elif command == "update":

        if len(sys.argv) < 4:
            print("Usage: task-cli update <id> <new description>")
            sys.exit()

        task_id = sys.argv[2]
        update_description = sys.argv[3]

        if not task_id.isdigit():
            print("Invalid task id")
            sys.exit()

        update(task_id, update_description)

    # DELETE
    elif command == "delete":

        if len(sys.argv) < 3:
            print("Usage: task-cli delete <id>")
            sys.exit()

        delete_id = sys.argv[2]

        if not delete_id.isdigit():
            print("Invalid task id")
            sys.exit()

        delete(delete_id)

    # MARK IN PROGRESS
    elif command == "mark-in-progress":

        if len(sys.argv) < 3:
            print("Usage: task-cli mark-in-progress <id>")
            sys.exit()

        mark_id = sys.argv[2]

        if not mark_id.isdigit():
            print("Invalid task id")
            sys.exit()

        mark_in_progress(mark_id)

    # MARK DONE
    elif command == "mark-done":

        if len(sys.argv) < 3:
            print("Usage: task-cli mark-done <id>")
            sys.exit()

        mark_done_id = sys.argv[2]

        if not mark_done_id.isdigit():
            print("Invalid task id")
            sys.exit()

        done(mark_done_id)

    # LIST
    elif command == "list":

        if len(sys.argv) == 2:
            task_list()

        elif len(sys.argv) == 3:

            status = sys.argv[2]

            if status == "done":
                done()

            elif status == "todo":
                todo()

            elif status == "in-progress":
                in_progress()

            else:
                print("Invalid status")

        else:
            print("Usage: task-cli list [done|todo|in-progress]")

    # INVALID COMMAND
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()