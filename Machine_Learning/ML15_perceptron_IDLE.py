Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> from scipy.special import expit
>>> from sklearn.datasets import load_iris
>>> from sklearn.model_selection import train_test_split
>>> from sklearn.linear_model import Perceptron, SGDClassifier
>>> 
>>> x = np.array([1,2])
>>> w = np.array([0.1,0.2])
>>> 
>>> x*w
array([0.1, 0.4])
>>> 
>>> def and_gate(x1,x2):
	w1,w2,th=0.5,0.5,0.7
	result= x1* w1 +x2 *w2
	if result > th:
		y=1
	else:
		y=0
	return y

>>> and_gate(0,0)
0
>>> def step(x):
	y = x>0
	return y.astype(np.int)

>>> x=np.arange(-5,5,0.001)
>>> y=step(x)

Warning (from warnings module):
  File "<pyshell#25>", line 3
DeprecationWarning: `np.int` is a deprecated alias for the builtin `int`. To silence this warning, use `int` by itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g. `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link for additional information.
Deprecated in NumPy 1.20; for more details and guidance: https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations
>>> def step(x):
	y = x>0
	return y.astype(np.int_)

>>> y=step(x)
>>> def step(x):
	y = x>0
	return y.astype(np.int_)

>>> y=step(x)
>>> 
>>> print(y[-10:])
[1 1 1 1 1 1 1 1 1 1]
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x000002270058B2E0>]
>>> plt.grid()
>>> plt.show()
>>> def plot_activation_fn(activation):
	""" 활성화 함수 activation을 파라미터로 전달받아, 그려 주는 함수"""
	x=np.arange(-5,5,0.0001)
	y= activation(x)
	plt.plot(x,y)
	plt.grid()
	plt.show()

	
>>> plot_activation_fn(step)
>>> # Artifical Neuron(인공뉴런) 응용
>>> X,y= load_iris(return_X_y=True)
>>> X.shape, y.shape
((150, 4), (150,))
>>> X[:5]
array([[5.1, 3.5, 1.4, 0.2],
       [4.9, 3. , 1.4, 0.2],
       [4.7, 3.2, 1.3, 0.2],
       [4.6, 3.1, 1.5, 0.2],
       [5. , 3.6, 1.4, 0.2]])
>>> data = x[:,2:4]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    data = x[:,2:4]
IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
>>> data = X[:,2:4]
>>> data[:5]
array([[1.4, 0.2],
       [1.4, 0.2],
       [1.3, 0.2],
       [1.5, 0.2],
       [1.4, 0.2]])
>>> target = (y != 0).astype(np.int_)
>>> target
array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
>>> plt.scatter(data[target ==0, 0],data[target ==0,1], label='setosa')
<matplotlib.collections.PathCollection object at 0x00000227031444F0>
>>> plt.scatter(data[target==1,0],data[target==1,1],label='non-setosa')
<matplotlib.collections.PathCollection object at 0x0000022703144910>
>>> plt.legend()
<matplotlib.legend.Legend object at 0x00000227031353A0>
>>> plt.xlabel('petal length')
Text(0.5, 0, 'petal length')
>>> plt.ylabel('petal width')
Text(0, 0.5, 'petal width')
>>> plt.show()
>>> 