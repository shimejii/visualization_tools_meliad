import pandas as pd
import numpy as np
import jax.numpy as jnp
from jax._src.typing import Array

def ndarray2htmlTable(arr: np.ndarray) -> int:
    assert len(arr.shape) == 2
    df = pd.DataFrame(arr)
    html_table = df.to_html(index=False, header=False)
    return html_table

def load_exported_db_from_npy(workdir: str, exec_mode: str, database_name: str, step: int, idx_memory: int) -> Array:
    """load .npy file and return Array

    Args:
        workdir (str): Directory where the experiment took place. workdir[-1] != /
        exec_mode (str): train, test, generate, etc.
        database_name (str): _description_
        step (int): experimental step
        idx_memory (int): memory index

    Returns:
        Array: _description_
    """
    path_file = workdir + "/" + exec_mode + "_dbname_" + database_name + "_step_" +str(step) + "_memory_index_" + str(idx_memory) + ".npy"
    return jnp.load(path_file)

if __name__ == "__main__":
    #例としてNumPyの2次元配列を作成
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(ndarray2htmlTable(data))