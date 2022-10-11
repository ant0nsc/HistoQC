import os
import sys

from histoqc.data import package_resource_copytree
from histoqc.ui import run_server


def main(argv=None):
    import argparse

    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(prog="histoqc.ui",description="launch server for result viewing in user interface")
    parser.add_argument('--bind', '-b', metavar='ADDRESS',
                        default='0.0.0.0',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('data_directory',
                        nargs='?',
                        default=os.getcwd(),
                        help='Specify the data directory '
                             '[default:current directory]')
    parser.add_argument('--port', type=int, default=8000,
                        help='Specify alternate port [default: 8000]')
    parser.add_argument('--deploy', metavar="OUT_DIR",
                        default=None,
                        help='Write UI to OUT_DIR')
    parser.add_argument('--resultfile', 
                        type=str,
                        default=None,
                        help='If provided, use this fixed result file rather than what is selected in the UI.')
    args = parser.parse_args(argv)

    if args.deploy:
        if not os.path.isdir(args.deploy):
            print(f"'{args.deploy}' not a directory", file=sys.stderr)
            return -1
        package_resource_copytree('histoqc.ui', 'UserInterface', args.deploy)
        return 0

    # serve the histoqc ui
    run_server(args.data_directory, host=args.bind, port=args.port, resultfile=args.resultfile)


if __name__ == "__main__":
    main()
