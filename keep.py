import gkeepapi
import sys
from quickstart import get_events

def create_note(keep, events):
    """
    Usage Example

    note = keep.createNote('New Note', 'Write Code')
    note.pinned = True
    note.color = gkeepapi.node.ColorValue.Red
    keep.sync()
    """
    events_list = []
    if not events:
        return
    for event in events:
        events_list.append((event['summary'], False))
        start = event['start'].get('dateTime', event['start'].get('date'))

    note = keep.createList('Schedule Note', events_list)
    note.pinned = True
    note.color = gkeepapi.node.ColorValue.Red
    keep.sync()


def main():
    with open(sys.argv[1], "r") as auth_file:
        username = auth_file.readline()
        password = auth_file.readline()

    keep = gkeepapi.Keep()
    success = keep.login(username, password)
    events = get_events()
    create_note(keep, events)

if __name__ == '__main__':
    main()
