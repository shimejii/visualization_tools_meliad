import utils
import sys

argv = sys.argv
assert len(argv) == 6, f"len(argv) is {len(argv)}"
WORKDIR = argv[1]
EXEC_MODE = argv[2]
DATABASE_NAME = argv[3]
STEP = int(argv[4])
IDX_MEMORY = int(argv[5])
TABLE_NAME = argv[6]

arr = utils.load_exported_db_from_npy(
    WORKDIR, EXEC_MODE, DATABASE_NAME, STEP, IDX_MEMORY
)
tableHTML = utils.ndarray2htmlTable(arr)
name = "<p>" + TABLE_NAME + "</p>\n"
print(name + tableHTML)

