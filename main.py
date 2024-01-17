import argparse
import sys
import utils

argv = sys.argv
parser = argparse.ArgumentParser()
parser.add_argument("workdir", help="Working directory specified in the experiment")
parser.add_argument("exec_mode", help="Mode used for the experiment.")
parser.add_argument("database_name", help="Name of database to be converted")
parser.add_argument("step", help="Target number of steps", type=int)
parser.add_argument("idx_memory", help="Index of external memory", type=int)
parser.add_argument("idx_device", help="Index of device", type=int)
parser.add_argument("table_name_for_html", help="Name of the table to use for labeling when outputting to html")
args = parser.parse_args()

arr = utils.load_exported_db_from_npy(
    args.workdir, args.exec_mode, args.database_name, args.step, args.idx_memory
)
arr = arr[args.idx_device]
if len(arr.shape) == 3:
    arr = arr[:,:,0]
tableHTML = utils.ndarray2htmlTable(arr)
name = "<p>" + args.table_name_for_html + "</p>\n"
print(name + tableHTML)
