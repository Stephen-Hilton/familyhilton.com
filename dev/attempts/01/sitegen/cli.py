import argparse
from pathlib import Path
from .builder import SiteBuilder

def main():
    parser = argparse.ArgumentParser(prog="sitegen", description="Static site generator")
    parser.add_argument("command", choices=["build", "clean", "init"], help="Command to run")
    parser.add_argument("--root", default=".", help="Project root (defaults to current dir)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    sb = SiteBuilder(root)

    if args.command == "init":
        sb.init_site()
    elif args.command == "clean":
        sb.clean()
    elif args.command == "build":
        sb.build()
