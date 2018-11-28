import gkeepapi
import sys

def create_note(keep):
    """
    Usage Example

    note = keep.createNote('New Note', 'Write Code')
    note.pinned = True
    note.color = gkeepapi.node.ColorValue.Red
    keep.sync()
    """
    note = keep.createNote('Test Note', 'Testing Scheduler')
    note.color = gkeepapi.node.ColorValue.Purple
    keep.sync()


def main():
    with open(sys.argv[1], "r") as auth_file:
        username = auth_file.readline()
        password = auth_file.readline()

    keep = gkeepapi.Keep()
    success = keep.login(username, password)

    create_note(keep)

if __name__ == '__main__':
    main()
