import pandas as pd
import numpy as np
import jax.numpy as jnp

def ndarray2htmlTable(arr: np.ndarray) -> int:
    assert len(arr.shape) == 2
    df = pd.DataFrame(data)
    html_table = df.to_html(index=False, header=False)
    return html_table

if __name__ == "__main__":
    #例としてNumPyの2次元配列を作成
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(ndarray2htmlTable(data))
    