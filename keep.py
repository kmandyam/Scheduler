import gkeepapi
import sys

with open(sys.argv[1], "r") as auth_file:
    username = auth_file.readline()
    password = auth_file.readline()

keep = gkeepapi.Keep()
success = keep.login(username, password)

note = keep.createNote('HAHA', 'Eat breakfast')
note.pinned = True
note.color = gkeepapi.node.ColorValue.Red
note.checked = True
keep.sync()
