# Inference with scikit-learn models in pyodide

*Author:* Roman Yurchak

In this tutorial we will illustrate how to use pre-trained scikit-learn models in pyodide.

We will train a simple regression model using [the california housing
dataset](https://scikit-learn.org/stable/datasets/index.html#california-housing-dataset)
with scikit-learn, then run this trained model in the browser with pyodide.

## 1. Install dependencies locally

Fist we need install the same versions of dependencies as those included in
pyodide, as to keep the pickled model compatible. Here we will use the package
versions Pyodide 0.16.0dev0 (to be released).

```bash
conda create -n pyodide-demo python=3.8.2
conda activate pyodide-demo
pip install "cython<3.0" numpy==1.16.6
# Installing from Github releases, as .tar.gz on PyPi include Cythonized sources
# not compatible with Python 3.8. This takes a while.
pip install https://github.com/scipy/scipy/archive/v0.17.1.tar.gz
pip install scikit-learn==0.22.2 pandas==1.0.5 joblib==0.11
```

**Note:** Because the version of scipy included in pyodide is outdated, we
will need a working compiler to build numpy and scipy 0.17 for Python 3.8,

## 2. Train the model locally

We will train a pipeline consisting of a K-bins discretized and a Ridge
regression model,
```py
import pickle

import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.linear_model import Ridge

from sklearn.model_selection import train_test_split, cross_val_score

X, y = fetch_california_housing(return_X_y=True)

pipe = make_pipeline(KBinsDiscretizer(), Ridge())


print(
    "CV accuracy score: ", cross_val_score(pipe, X, y, scoring="neg_mean_squared_error")
)


pipe.fit(X, y)
```

This model has cross-valuated Mean Squared Error (MSE) of 0.78.

Then we normally would need to pickle this model to disk and load the pickled
pipeline from some HTTP server.  However, to make this demo simpler, and since
the model is quite small, here we  will simply pickle the model to a bytes
object,
```python
import pickle

print(pickle.dumps(pipe))
```
and copy-paste this string in the pyodide console.


## 3. Loading the model in pyodide

Go to [pyodide-cdn2.iodide.io/dev/full/console.html](https://pyodide-cdn2.iodide.io/dev/full/console.html), and enter
```python
import sklearn
import pickle
import pyodide
```
which will load scikit-learn package. This currently downloads ~100MB of
dependencies and can take a while.

Then create a new variable with the copy-pasted value of the pickled model,
```
stream = <paste-pickle-bytes-stream>
```
and finally re-load it with pickle,
```py
pipe = pickle.loads(stream)
```
This is the same model that we trained locally, and we can inspect all of
attributes and elements of this scikit-learn pipeline.


## 4. Applying the model in Pyodide
Lets imagine we have some data in JavaScript. Open the JS console (F12 key, tab
"console") and create a new JS variable, 
```javascript
var data = [[ 1.86, 18,  5.32,  1.17, 741, 2.1,  0.39, -121]];
```
which would correspond to 8 input features of the [California housing
dataset](https://scikit-learn.org/stable/datasets/index.html#california-housing-dataset).

We can pass this data to Pyodide with,
```py
# in pyodide
>>> from js import data
>>> type(data)
<class 'JsProxy'>
>>> import pyodide
>>> data = pyodide.as_nested_list(data)
>>> type(data)
list
```
and finally apply `model.predict` on this data,
```py
>>>  pipe.predic(data)
2.386131030582392
```

## 5. Conclusions

This tutorial offers a proof of concept of loading trained scikit-learn models in pyodide and
performing inference. 

It should be noted that addressing following points would significantly improve this workflow,
 - better packaging of scipy and LAPACK
   (https://github.com/iodide-project/pyodide/issues/240) would reduce the
   download size of dependencies by 4-5x in this example.
 - currently binary files (e.g. pickle file) need to be loaded asynchronously
   in Javascript (https://github.com/iodide-project/pyodide/issues/400) and it
   would be useful to make this possible e.g. with `pyodide.open_url`. 
