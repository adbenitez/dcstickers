"""Command line interface"""

import argparse
import os

from emoji import demojize

from dcstickers import signal

from . import __version__


def main() -> None:
    args = get_parser().parse_args()
    stickers_dir = get_stickers_dir(args.dcdir)
    for pack in args.pack:
        print("Installing {} ...".format(pack))
        download_pack(pack, stickers_dir)


def download_pack(pack: str, stickers_dir: str) -> None:
    if signal.is_pack(pack):
        pack_name, stickers = signal.get_stickers(pack)
    else:
        raise ValueError("Unsupported pack URL.")

    pack_dir = os.path.join(stickers_dir, pack_name)
    os.mkdir(pack_dir)

    for sticker in stickers:
        name = "{}.{}+{}.webp".format(
            sticker.id, demojize(sticker.emoji, delimiters=("", "")), sticker.emoji
        )
        with open(os.path.join(pack_dir, name), "wb") as file:
            file.write(sticker.image_data)


def get_stickers_dir(path: str = None) -> str:
    """Get sticker directory.

    :param path: Delta Chat configuration folder, by default ~/.config/DeltaChat is tried.
    """
    if not path or not os.path.exists(path):
        path = os.path.expanduser("~/.config/DeltaChat")
    if not os.path.exists(path):
        path = os.path.expanduser("~/.var/app/chat.delta.desktop/config/DeltaChat")
    if not os.path.exists(path):
        raise ValueError("Delta Chat configuration folder not found.")

    stickers = os.path.join(path, "stickers")
    if not os.path.exists(stickers):
        os.mkdir(stickers)

    accounts = os.path.join(path, "accounts")
    if os.path.exists(accounts):
        for acc in os.listdir(accounts):
            acc = os.path.join(accounts, acc, "stickers")
            if not os.path.exists(acc):
                os.symlink(stickers, acc, target_is_directory=True)

    return stickers


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=__name__.split(".")[0],
        description="Sticker pack download and installation tool for Delta Chat application",
    )
    parser.add_argument("pack", metavar="PACK", nargs="+", help="sticker pack URL")
    parser.add_argument(
        "-d",
        "--deltachat-dir",
        dest="dcdir",
        metavar="DELTACHAT-DIR",
        help="path to the DeltaChat configuration folder (by default it is auto-detected)",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=__version__,
        help="show program's version number and exit.",
    )

    return parser
