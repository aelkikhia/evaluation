#!/usr/bin/env python

from evaluation.eval_lib import array_diff


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='show array differences.')
    parser.add_argument('-c', '--current', type=int, dest='current', nargs='+',
                        default=[],
                        help='current comma separated list of elements')
    parser.add_argument('-t', '--target', type=int, dest='target', nargs='+',
                        default=[],
                        help='target comma separated list of elements')

    args = parser.parse_args()

    additions, deletions = array_diff(args.current, args.target)
    print(f'additions: {additions}')
    print(f'deletions: {deletions}')
