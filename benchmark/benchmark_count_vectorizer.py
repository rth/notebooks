
import timeit
import pandas as pd
from sklearn.feature_extraction.text import (CountVectorizer, TfidfVectorizer,
                                             HashingVectorizer)

from sklearn.datasets import fetch_20newsgroups
from tqdm import tqdm
import itertools
import numpy as np


text = fetch_20newsgroups(subset='all').data


def pandas_df_to_markdown_table(df):
    fmt = ['---' for i in range(len(df.columns))]
    df_fmt = pd.DataFrame([fmt], columns=df.columns)
    df_formatted = pd.concat([df_fmt, df])
    print(df_formatted.to_csv(sep="|", index=False))


res = []


def run_vectorizer(Vectorizer, X, **params):
    def f():
        vect = Vectorizer(**params)
        vect.fit_transform(X)
    return f


for Vectorizer, (analyzer, ngram_range) in tqdm(itertools.product(
            [CountVectorizer, TfidfVectorizer, HashingVectorizer],
            [('word', (1, 1)),
             ('word', (1, 2)),
             ('word', (1, 4)),
             ('char', (4, 4)),
             ('char_wb', (4, 4))
             ])):

    bench = {'vectorizer': Vectorizer.__name__}
    params = {'analyzer': analyzer, 'ngram_range': ngram_range}
    bench.update(params)
    dt = timeit.repeat(run_vectorizer(Vectorizer, text, **params),
                       number=1,
                       repeat=3)
    bench['time'] = "{:.1f}".format(np.mean(dt))

    res.append(bench)


df = pd.DataFrame(res).set_index(['analyzer', 'ngram_range', 'vectorizer'])
df = df['time'].unstack(level=2).reset_index()

pandas_df_to_markdown_table(df)
