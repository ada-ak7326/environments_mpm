import numpy as np
import pandas as pd
from envtest import preview_df

n_rows = 20

df = pd.DataFrame({
    'a': np.random.rand(n_rows),
    'b': np.random.randn(n_rows),
    'c': np.random.randint(0, 100, n_rows),
    'd': np.random.choice(['x', 'y', 'z'], n_rows),
})

preview_df(df)
