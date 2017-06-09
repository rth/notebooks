
import timeit
import pandas as pd
from sklearn.feature_extraction.text import (CountVectorizer, TfidfVectorizer,
                                             HashingVectorizer)

from sklearn.datasets import fetch_20newsgroups
from tqdm import tqdm
import itertools
import numpy as np

import cProfile, pstats, io

text = fetch_20newsgroups(subset='all').data

cp = cProfile.Profile()
cp.enable()

vect = TfidfVectorizer(ngram_range=(1, 2))
vect.fit_transform(text)

s = io.StringIO()
sortby = 'tottime'
ps = pstats.Stats(cp, stream=s).sort_stats(sortby)
ps.print_stats(100)
print(s.getvalue())
