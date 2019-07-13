# -*- coding: utf-8 -*-

__author__ = 'Riotkit'
__email__ = 'riotkit_org@riseup.net'

import argparse
import sys
import traceback

try:
    from simverlib import SimVer

except ImportError:
    from .simverlib import SimVer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Repository path', default='.')

    parser.description = 'RiotKit\'s SimVer - Simple Version retrieving, based on GIT tags'
    parsed = parser.parse_args()

    try:
        SimVer(params=vars(parsed)).main()

    except Exception as e:
        traceback.print_exc(file=sys.stdout)

    except KeyboardInterrupt:
        print('[CTRL]+[C]')
        sys.exit(0)


if __name__ == "__main__":
    main()
