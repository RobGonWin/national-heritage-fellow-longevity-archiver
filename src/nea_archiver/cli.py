"""Focused archival method commands; public CI performs offline replay only."""
import argparse
from .nea_research import register_cli, run_cli

def main(argv=None):
    parser=argparse.ArgumentParser(prog='nea-archiver')
    register_cli(parser.add_subparsers(dest='command',required=True))
    args=parser.parse_args(argv)
    try:
        return run_cli(args)
    except (ValueError,OSError) as error:
        parser.error(str(error))
