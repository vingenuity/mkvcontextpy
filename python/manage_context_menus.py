#!/usr/bin/env python3

"""
Installs or uninstalls mkvcontextpy context menus.
"""

import argparse
import logging
from pathlib import Path
import sys
from typing import List

from context_menu import menus


def merge_mkvs(filenames: List[str], params: str) -> None:
    """
    Merges all of the given MKV files into a single MKV file.
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()

    for filename in filenames:
        mkv_input_path = Path(filename)
        mkv_file_name = mkv_input_path.name
        mkv_output_prefix = mkv_file_name + "_split_"

        logger.info("Splitting each chapter within '%s' into its own MKV file...", mkv_file_name)


def print_mkv_info(filenames: List[str], params: str) -> None:
    """
    Prints information about a given MKV file to the console.
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()

    for filename in filenames:
        mkv_path = Path(filename)

        logger.info("Displaying information about MKV file '%s'...", mkv_path.name)


def split_mkv_by_chapter(filenames: List[str], params: str) -> None:
    """
    Splits each chapter in a given MKV file into its own MKV file.
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()

    for filename in filenames:
        mkv_input_path = Path(filename)
        mkv_file_name = mkv_input_path.name
        mkv_output_prefix = mkv_file_name + "_split_"

        logger.info("Splitting each chapter within '%s' into its own MKV file...", mkv_file_name)


MENU_TITLE = 'mkvcontextpy'
MENU_MAPPING = [
    (MENU_TITLE,
    ['.mkv'],
    [menus.ContextCommand('Display MKV Information',
                          python=print_mkv_info),
     menus.ContextCommand('Split MKV Into Chapters',
                          python=split_mkv_by_chapter)]),
    (MENU_TITLE,
    ['DIRECTORY'],
    [menus.ContextCommand('Merge All MKV Files in Directory',
                          python=merge_mkvs)])
]


def install_menus(arguments: argparse.Namespace) -> int:
    """
    Installs mkvcontextpy context menus.
    """
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    for title, extensions, commands in MENU_MAPPING:
        for ext in extensions:
            logger.debug(f"Installing {title} context menu for extension '{ext}'...")
            menu = menus.ContextMenu(title, type=ext)
            menu.add_items(commands)
            menu.compile()
    return 0


def uninstall_menus(_: argparse.Namespace) -> int:
    """
    Uninstalls mkvcontextpy context menus.
    """
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    for title, extensions, _ in MENU_MAPPING:
        for ext in extensions:
            logger.debug(f"Uninstalling {title} context menu for extension '{ext}'...")
            menus.removeMenu(title, type=ext)
    return 0


def parse_arguments(arguments: List[str]) -> argparse.Namespace:
    """
    Parses command-line arguments into namespace data.
    """
    parser = argparse.ArgumentParser(
        description="Un/installs mkvcontextpy context menus."
    )
    subparsers = parser.add_subparsers()

    install_parser = subparsers.add_parser('install',
                                           help='Installs context menus.')
    install_parser.set_defaults(func=install_menus)

    uninstall_parser = subparsers.add_parser('uninstall',
                                             help='Uninstalls context menus.')
    uninstall_parser.set_defaults(func=uninstall_menus)

    return parser.parse_args(arguments)


if __name__ == "__main__":
    PARSED_ARGS = parse_arguments(sys.argv[1:])
    exit(PARSED_ARGS.func(PARSED_ARGS))
