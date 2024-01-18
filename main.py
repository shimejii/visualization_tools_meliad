import argparse
import sys
import utils

def npy2tablehtml(args):
    arr = utils.load_exported_db_from_npy(
        args.workdir, args.exec_mode, args.database_name, args.step, args.idx_memory)
    arr = arr[args.idx_device]
    if len(arr.shape) == 3:
        arr = arr[:,:,0]
    tableHTML = utils.ndarray2htmlTable(arr)
    name = "<p>" + args.table_name_for_html + "</p>\n"
    print(name + tableHTML)

# argv = sys.argv
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# cmd: npy2tablehtml
parser_npy2tablehtml = subparsers.add_parser('npy2tablehtml', help='see `add -h`')
parser_npy2tablehtml.add_argument("workdir", help="Working directory specified in the experiment")
parser_npy2tablehtml.add_argument("exec_mode", help="Mode used for the experiment.")
parser_npy2tablehtml.add_argument("database_name", help="Name of database to be converted")
parser_npy2tablehtml.add_argument("step", help="Target number of steps", type=int)
parser_npy2tablehtml.add_argument("idx_memory", help="Index of external memory", type=int)
parser_npy2tablehtml.add_argument("idx_device", help="Index of device", type=int)
parser_npy2tablehtml.add_argument("table_name_for_html", help="Name of the table to use for labeling when outputting to html")
parser_npy2tablehtml.set_defaults(handler=npy2tablehtml)

args = parser.parse_args()
if hasattr(args, 'handler'):
    args.handler(args)
else:
    # unkonw sub command
    parser.print_help()