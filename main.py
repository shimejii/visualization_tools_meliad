import argparse
import sys
import utils
import jax.numpy as jnp

def npy2tablehtml(args):
    arr = utils.load_exported_db_from_npy(
        args.workdir, args.exec_mode, args.database_name, args.step, args.idx_memory)
    arr = arr[args.idx_device]
    arr = jnp.array(arr)
    if len(arr.shape) == 1:
        tableHTML = utils.ndarray2htmlTable(arr.reshape(1, arr.shape[0]))
        name = "<p>" + args.table_name_for_html + "</p>\n"
        print(name + tableHTML)
    elif len(arr.shape) == 2:
        tableHTML = utils.ndarray2htmlTable(arr)
        name = "<p>" + args.table_name_for_html + "</p>\n"
        print(name + tableHTML)
    elif len(arr.shape) == 3:
        assert 0 <= args.dim3_idx and args.dim3_idx < arr.shape[2]
        tableHTML = utils.ndarray2htmlTable(arr[:,:,args.dim3_idx])
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
parser_npy2tablehtml.add_argument("--dim3_idx", help="Target 3D  index", type=int)
parser_npy2tablehtml.set_defaults(handler=npy2tablehtml)

args = parser.parse_args()
if hasattr(args, 'handler'):
    args.handler(args)
else:
    # unkonw sub command
    parser.print_help()