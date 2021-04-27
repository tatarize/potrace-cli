"""
Copyright (C) 2001-2019 Peter Selinger.
This file is part of Potrace. It is free software and it is covered
by the GNU General Public License. See the file COPYING for details.

Python Port by Tatarize, April 2021
"""

import argparse
import sys

import pkg_resources
from PIL import Image

from potrace import Bitmap

parser = argparse.ArgumentParser()
parser.add_argument(
    "-v", "--version", action="store_true", help="prints version info and exit"
)
parser.add_argument(
    "-l", "--license", action="store_true", help="prints license info and exit"
)
parser.add_argument("filename", nargs="?", type=str, help="an input file")
parser.add_argument(
    "-o", "--output", type=str, help="write all output to this file", default="out.svg"
)

plugin_register_functions = []
for entry_point in pkg_resources.iter_entry_points("cli.backends"):
    try:
        plugin = entry_point.load()
        plugin_register_functions.append(plugin)
    except pkg_resources.DistributionNotFound:
        pass


if len(plugin_register_functions) == 0:
    """
    Fallback if entry points are not permitted.
    """
    from .backend_svg import register as svg_register

    plugin_register_functions.append(svg_register)

backends = {}
for register in plugin_register_functions:
    register(backends)

if len(backends) != 0:
    choices = [b for b in backends]
    parser.add_argument(
        "-b",
        "--backend",
        type=str,
        choices=choices,
        default="svg" if "svg" in choices else choices[0],
        help="select backend by name",
    )

choices = ["black", "white", "left", "right", "minority", "majority", "random"]
parser.add_argument(
    "-z",
    "--turnpolicy",
    type=str,
    choices=choices,
    default="minority",
    help="how to resolve ambiguities in path decomposition",
)
parser.add_argument(
    "-t",
    "--turdsize",
    type=int,
    help="suppress speckles of up to this size (default 2)",
    default=2,
)
parser.add_argument(
    "-a", "--alphamax", type=float, help="corner threshold parameter", default=1
)
parser.add_argument(
    "-n", "--longcurve", action="store_true", help="turn off curve optimization"
)
parser.add_argument(
    "-O", "--opttolerance", type=float, help="curve optimization tolerance", default=0.2
)
parser.add_argument(
    "-C",
    "--color",
    type=str,
    help="set foreground color (default Black)",
    default="#000000",
)
parser.add_argument(
    "-i",
    "--invert",
    action="store_true",
    help="invert bitmap",
)
parser.add_argument(
    "-k",
    "--blacklevel",
    type=float,
    default=0.5,
    help="invert bitmap",
)


def run():
    argv = sys.argv[1:]
    args = parser.parse_args(argv)
    turnpolicy = choices.index(args.turnpolicy)
    if args.version:
        print("Python Potrace 0.0.1")
        return
    if args.license:
        try:
            with open("LICENSE", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.endswith("\n"):
                        print(line[0:-1])
                    else:
                        print(line)
        except IOError:
            print("License not found.")
        return
    if args.filename:
        try:
            image = Image.open(args.filename)
        except IOError:
            print("Image (%s) could not be loaded." % args.filename)
            return
        bm = Bitmap(image, blacklevel=args.blacklevel)
        if args.invert:
            bm.invert()
        plist = bm.trace(
            turdsize=args.turdsize,
            turnpolicy=turnpolicy,
            alphamax=args.alphamax,
            opticurve=not args.longcurve,
            opttolerance=args.opttolerance,
        )
        if args.output:
            if hasattr(args,"backend"):
                output = backends[args.backend]
                output(args, image, plist)
            else:
                print("No backends exist to process output.")
    else:
        print("No image loaded.\n 'cli --help' for help.")
