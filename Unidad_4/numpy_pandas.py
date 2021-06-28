import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30, 40], index = ["a", "b", "c", "d"])

print(s[1:])
print(s[:3])
