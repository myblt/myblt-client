#!/usr/bin/python3
import os
import sys
import requests

def upload(filename):
    r = requests.post('http://a.myb.lt/upload',
        files={'file': open(filename, 'rb')})
    print(r.json()['short_url'])
    sys.exit(0)

def main():
    filename = sys.argv[1]
    if os.path.isfile(filename):
        upload(filename)
    else:
        print('File "{}" does not exist'.format(filename), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
    print('Please provide a filename', file=sys.stderr)
    sys.exit(1)
