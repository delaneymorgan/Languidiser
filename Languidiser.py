#!/usr/bin/env python
# coding=utf-8

import argparse
from openpyxl import Workbook

__version__ = "20230703-1"

# =============================================================================


def arg_parser():
    """
    parse arguments
    :return: the parsed arguments
    """
    parser = argparse.ArgumentParser(description='Languidiser - multi-language string factory.')
    parser.add_argument("-v", "--verbose", help="verbose mode", action="store_true")
    parser.add_argument("-d", "--diagnostic", help="diagnostic mode (includes verbose)", action="store_true")
    parser.add_argument("--version", action="version", version='%(prog)s {version}'.format(version=__version__))
    args = parser.parse_args()
    return args


# =============================================================================


def main():
    args = arg_parser()
    workbook = Workbook()
    sheet = workbook.active
    return


# =============================================================================


if __name__ == '__main__':
    main()
