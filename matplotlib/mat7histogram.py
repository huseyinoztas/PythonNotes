import matplotlib.pyplot as plt
import numpy as np
x1=np.random.normal(0,1,1000)
x2=np.random.normal(5,2,1000)
x3=np.random.normal(-5,0.7,1000)
plt.hist(x1,alpha=0.5)
plt.hist(x2,alpha=0.5)
plt.hist(x3,alpha=0.5)
plt.show()


# x=np.random.randn(1000)
# ortanca=np.median(x)
# plt.hist(x,color="red",edgecolor="Black",rwidth=0.4)
# plt.axvline(ortanca,color="Green")
# plt.show()