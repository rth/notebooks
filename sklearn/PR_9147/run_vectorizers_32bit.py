
import sys

import numpy as np

from sklearn.feature_extraction.text import (TfidfVectorizer, HashingVectorizer,
                                             CountVectorizer)


vectorizer_name = sys.argv[1]
Vectorizer = eval(vectorizer_name)
n_samples = int(sys.argv[2])

vocabulary = ' '.join('{}'.format(el) for el in np.arange(10, 2**16 + 1 + 10))

def doc():
    for idx in range(n_samples):
        yield vocabulary

if vectorizer_name == 'CountVectorizer':
    pars = {}
else:
    pars = {}  

vect = Vectorizer(**pars)

print('Vectorizer:', type(vect).__name__)
print('  pars: ', pars)
print('n_samples =', n_samples)

X = vect.fit_transform(doc())

print('\n# Resulting array (X):')
for attr in ['indptr', 'indices', 'data']:
    y = getattr(X, attr)
    print(' * {} len={} dtype={}'.format(attr, len(y), y.dtype))
