import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(50,300,size=365),
                  columns=["Square Ft Ordered"],
                  index=pd.date_range("20180101", periods=365,))
print (df)

df.to_csv('Square_ft_random.csv')