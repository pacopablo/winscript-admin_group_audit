__author__ = 'John Hampton <pacopablo@pacopablo.com>'

import sys
import win32net as w32n
import win32security as w32s

if __name__ == '__main__':
    if len(sys.argv) < :
        print("you must specify at least one server to query")
    else:
        for server in sys.argv[1:]:
            users = w32n.NetLocalGroupGetMembers(server, 'Administrators', 2)[0]
            for u in users:
                print u['domainandname']
# If you want to print the SID also, uncomment the following line
#                print w32s.ConvertSidToStringSid(u['sid'])
                continue
            continue
    sys.exit(0)


