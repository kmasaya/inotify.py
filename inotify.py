#!/usr/bin/python
# coding: UTF-8

import os
import sys
import time
from optparse import OptionParser

argv = sys.argv
argc = len( argv) - 1
mtimes = {}

def scan( options):
    if not os.path.isdir( options.scan_directory):
        print "%s is not directory." % ( options.scan_directory,)
        sys.exit( 0)

    while True:
        time.sleep( options.scan_interval)

        renew = False
        for ( root, dirs, files) in os.walk( options.scan_directory):
            for filename in files:
                filepath = os.path.join( root, filename)
                if options.filename.endswith( filename):
                    continue
                if not os.path.exists( filepath):
                    continue
                mtime = os.path.getmtime( filepath)
                if filepath not in mtimes:
                    mtimes[filepath] = mtime
                    if options.scan_log:
                        print "%s is new" % ( filepath,)
                if mtime != mtimes[filepath]:
                    mtimes[filepath] = mtime
                    print "%s is renew" % ( filepath,)
                    renew = True

        if renew:
            latest = 0
            for k, v in mtimes.items():
                if mtimes[k] > latest:
                    latest = mtimes[k]

            if options.file:
                open( options.filename, "w").write( str( latest))

def parser_option():
    parser = OptionParser()

    parser.add_option( "-f", "--file", dest="file", help="output file", action="store_true", default=False)
    parser.add_option( "-o", "--filename", dest="filename", help="output filename", default="inotifypy.log")
    parser.add_option( "-d", "--directory", dest="scan_directory", help="scan directory", default="./")
    parser.add_option( "-i", "--interval", dest="scan_interval", help="scan interval", default=3)
    parser.add_option( "-l", "--log", dest="scan_log", help="scan renew print log", default=True)

    return parser.parse_args( argv[1:])

def main():
    ( options, args) = parser_option()

    scan( options)


if __name__ == "__main__":
    main()
