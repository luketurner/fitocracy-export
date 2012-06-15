from sys import argv, exit

from fitocracy_export import *

if not (len(argv) == 3 and argv[1] and argv[2]):
    print("Usage: cli.py [user] [pass]")
    exit(1)

print("\n~~ Beginning Backup ~~\nUser: {0}\nPass: {1}\n".format(argv[1], 
    ''.join(['*' for i in argv[2]])))

api = APISession()
if api.login(argv[1], argv[2]):
    api.get_all_activity_data()
    api.save_activity_data("fitocracy_data.json")
else:
    print("\n ERR: Login Failed \n")
    exit(1)

print("\n ~ Gotten Activities ~ \n")
print("\n ~ Your UID: {0} ~ \n".format(api.user_id))
