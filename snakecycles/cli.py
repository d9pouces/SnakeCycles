# -*- coding: utf-8 -*-
"""Core shell application.
Parse arguments and logger, use translated strings.
"""
from __future__ import unicode_literals

import optparse

__author__ = 'mgallet'

__all__ = ['main']


def main():
    """Main function, intended for use as command line executable.

    Returns:
      * :class:`int`: 0 in case of success, != 0 if something went wrong

    """
    parser = optparse.OptionParser()
    options, args = parser.parse_args()

    return_code = 0  # 0 = success, != 0 = error
    # complete this function
    return return_code


if __name__ == '__main__':
    import doctest

    doctest.testmod()
