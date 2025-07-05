"""import numpy as np

a = np.array([1,2,3,])
b = np.array([[1,2],[3,4]])
print(a.shape)
print(b.ndim)
print(b.dtype)"""


"""import numpy as np
np.zeros((2,3))
#np.ones((3,))
#np.eyes(3)
#np.arrange(1,10,2)
#np.linespace(0,1,5)"""

"""import numpy as arr
arr=np.array([[1,2,3],[4,5,6]])
#indexing $ slicing 
print(arr[0,1])
print(arr[:,1])

#reshape $ flatten

arr.reshape(3,2)
arr.flatten()

a = np.array([[1],[2],[3]])
b = np.array([10,20,30])
print(a+b)
"""

"""array=([0.,0.25,0.5,0.75,1])
arr = np.array([[1,2],[3,4]])
print(arr.sum())
print(arr.mean())
print(arr.max(axis=0))
print(arr.median(arr))"""

import pandas as pd 
s = pd.Series([10,20,30],index=["a","b","c"])
print(s["b"])
print(s.values)

data = {
    "Name":["Alice","Bob","Charlie"],
    "Age":[25,30,35],
    "Score":[85,90,95]
}
df=pd.DataFrame(data)
print(df.head)
#column access 
print(df["Name"])

#row access
print(df.iloc[0])
print(df.loc[0])

#conditional filtering 
print(df[df["Score"] > 85]) 
