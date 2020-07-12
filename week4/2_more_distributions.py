#If all numbers are equally likely to be drawn then it is flat horizontal line called uniform distribution.
#Normal Distribution called Gaussian or Bell curve.
# Number which has the highest probability is drawn at zero.
# mean is always zero


# Standard deviation is that how different the value is from the mean

#Bimodal Distribution : mixure of two normal distributions

import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt


x=np.random.binomial(6,0.5,100)
# plt.plot(x)
plt.show()
y=np.random.normal(1,0.4,100)
plt.hist(y,histtype='step',bins=50)
plt.show()
print(x.mean())

