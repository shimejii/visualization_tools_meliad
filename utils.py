import pandas as pd
import sentencepiece as spm
import numpy as np
import jax.numpy as jnp
Array = jnp.ndarray

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

def decode_tokens(path_sentencePiece_model_file: str, tokens: Array, unit_convert: str = "token") -> list:
    assert len(tokens.shape) == 2
    batch_size, num_tokens = tokens.shape
    assert unit_convert == "token" or "batch"

    # load sp model
    sp = spm.SentencePieceProcessor(model_file=path_sentencePiece_model_file)

    # Token reshape and conversion to python list
    if unit_convert == "token":
        tokens = jnp.reshape(tokens, (batch_size, num_tokens, 1))
        tokens = tokens.tolist()
        ret = []
        for i in range(len(tokens)):
            ret.append(sp.decode(tokens[i]))
        return ret
    elif unit_convert == "batch":
        tokens = tokens.tolist()
        ret = sp.decode(tokens)
        return ret

if __name__ == "__main__":
    #例としてNumPyの2次元配列を作成
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(ndarray2htmlTable(data))