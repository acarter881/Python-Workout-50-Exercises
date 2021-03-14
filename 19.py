#! python3

"""
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
"""

def passwd_to_dict(fileName):
    usernames = {}
    with open(fileName, 'r') as f:
        for row in f.readlines():
            if row.strip() == '' or row.startswith('#'):
                pass
            else:
                usernames[row.split(':')[0]] = int(row.split(':')[2])
    return usernames

print(passwd_to_dict('./Python/unixStyle.txt'))
