
import sys

import numpy as np

from sklearn.feature_extraction.text import (TfidfVectorizer, HashingVectorizer,
                                             CountVectorizer)


Vectorizer = eval(sys.argv[1])
n_samples = int(sys.argv[2])

vocabulary = ' '.join('{}'.format(el) for el in np.arange(10, 2**16 + 1 + 10))

def doc():
    for idx in range(n_samples):
        yield vocabulary

vect = Vectorizer()

print('Vectorizer:', type(vect).__name__)
print('n_samples =', n_samples)

X = vect.fit_transform(doc())

print('\n# Resulting array (X):')
for attr in ['indptr', 'indices', 'data']:
    y = getattr(X, attr)
    print(' * {} len={} dtype={}'.format(attr, len(y), y.dtype))
