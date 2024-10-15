#!/usr/bin/env python3
from optparse import OptionParser

if __name__ == '__main__':
    usage = "[-f <full>] [-n <none>] [-r <rate>]"
    version = '%prog v1.0.0'

    parser = OptionParser(usage, version=version)

    parser.add_option('-f', '--full', dest='full', type='float', help='with tax')
    parser.add_option('-n', '--none', dest='none', type='float', help='without tax')
    parser.add_option('-r', '--rate', dest='rate', type='float', default=0.06, help='tax rate, default: 0.06')

    (options, args) = parser.parse_args()

    full = 0.0
    none = 0.0
    tax = 0.0

    if options.full and options.none:
        print('bad option, do not set both full and none')
        exit(1)
    elif options.full:
        full = options.full
        none = round((full / (1 + options.rate)), 2)
        tax = round((full - none), 2)
    elif options.none:
        full = round((options.none * (1 + options.rate)), 2)
        none = options.none
        tax = round((full - none), 2)
    else:
        print('bad option, must set full or none')
        exit(1)

    print('with tax: %.2f\nwithout tax: %.2f\ntax: %.2f' % (full, none, tax))
