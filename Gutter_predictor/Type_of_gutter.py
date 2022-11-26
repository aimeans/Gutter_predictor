import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,4,size=365),
                  columns=["Gutter Type"],
                  index=pd.date_range("20180101", periods=365,))
print (df)

df.to_csv('Gutter_type.csv')