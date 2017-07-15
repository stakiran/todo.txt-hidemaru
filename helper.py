# -*- coding: utf-8 -*-

import datetime
import os
import sys

def file2list(filepath):
    ret = []
    with open(filepath, 'r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, 'w') as f:
        f.writelines(['%s\n' % line for line in ls] )

def abort(msg):
    print'Error: {0}'.format(msg)
    os.system('pause')
    exit(1)

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i', '--input', default=None, required=True,
        help='A input filename.')
    parser.add_argument('-y', default=None, type=int,
        help='The number of a input line.')

    parser.add_argument('--sort', default=False, action='store_true',
        help='Do sort.')

    args = parser.parse_args()
    return args

class Task:
    def __init__(self, line):
        #      01234567890123456789012345678
        fmt = 'x (X) YYYY-MM-DD YYYY-MM-DD '
        if len(line)<len(fmt):
            abort('Invalid format, length shortage "{0}".'.format(line))

        self._line = line
        self._donemark = line[0:1]
        self._prio     = line[2:5]
        self._compdate = line[6:16]
        self._createiondate = line[17:27]
        self._description = line[28:]

        # extract all options from description
        self._options = {}
        for elm in self._description.split(' '):
            if elm.find(':')==-1:
                continue
            key, value = elm.split(':')
            self._options[key] = value

    def _walk_day(self, datestr, day):
        y = int(datestr[0:4])
        m = int(datestr[5:7])
        d = int(datestr[8:10])

        dt = datetime.datetime(y, m, d)
        delta = datetime.timedelta(days=abs(day))

        if day>=0:
            newdt = dt + delta
        else:
            newdt = dt - delta

        return '{0}-{1}-{2}'.format(newdt.year, newdt.month, newdt.day)

    def _walk_compdate(self, day):
        newdt = self._walk_day(self._compdate, day)
        self._compdate = newdt

    def _walk_creationdate(self, day):
        newdt = self._walk_day(self._createiondate, day)

    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(
            self._donemark, self._prio,
            self._compdate, self._createiondate,
            self._description
        )

args = parse_arguments()

MYDIR = os.path.abspath(os.path.dirname(__file__))
infile = os.path.join(MYDIR, args.input)
lines = file2list(infile)

if args.sort:
    outfile = infile
    lines.sort()
    list2file(outfile, lines)
    exit(0)
