import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help="Enter path to json file")
    parser.add_argument('--export', action='store_true', help="Enter path to json file")
    return parser
