#!/usr/bin/env python

import os.path

from evaluation.eval_lib import social_network_analysis


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description='get social network analysis from a csv file')
    parser.add_argument('-f', '--file', type=str, dest='file', default=None,
                        help='csv file required')

    args = parser.parse_args()
    file = args.file

    if file is None or not os.path.exists(file):
        print(f'{args.file} is not a valid file')
    else:
        analysis = social_network_analysis(file)
        print(f'analysis: {analysis}')
