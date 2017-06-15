# Benchmarks for scikit-learn/scikit-learn #

Date: *June 15, 2017*

## A. Performance benchmarks

### Using master 

========== Run time performance (sec) ===========

Computing the mean and the standard deviation of the run time over 3 runs...

CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---
21.08 (+-0.04)|14.50 (+-0.01)|21.95 (+-0.06)
17.63 (+-0.07)|13.37 (+-0.02)|18.07 (+-0.05)
3.74 (+-0.01)|3.09 (+-0.01)|3.83 (+-0.01)
13.90 (+-0.02)|7.12 (+-0.00)|14.19 (+-0.03)
46.68 (+-0.08)|13.18 (+-0.03)|47.89 (+-0.11)


=============== Memory usage (MB) ===============

CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---
777.8|570.3|802.1
537.8|407.2|546.6
172.6|178.0|218.4
798.3|220.2|801.2
3315.0|341.3|3280.2

### Using this PR

Using a subset of the 20 newsrgoups dataset (11314 documents).
This benchmarks runs in ~20 min ...
15it [17:16, 54.31s/it]

========== Run time performance (sec) ===========

Computing the mean and the standard deviation of the run time over 3 runs...

CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---
20.74 (+-0.05)|14.40 (+-0.00)|21.69 (+-0.11)
17.38 (+-0.05)|13.30 (+-0.04)|17.90 (+-0.03)
3.72 (+-0.00)|3.09 (+-0.01)|3.78 (+-0.02)
13.84 (+-0.07)|7.10 (+-0.00)|13.92 (+-0.01)
46.60 (+-0.29)|13.13 (+-0.04)|47.35 (+-0.50)


=============== Memory usage (MB) ===============

CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---
778.6|542.9|776.6
537.8|357.1|547.5
172.6|202.6|217.7
810.9|234.6|801.8
3315.0|356.3|3280.4



## B. Handling arrays > 32bit

Tested with [./run_vectorizers_32bit.py](./run_vectorizers_32bit.py)

### On master

1. Case len(X.data) < 2**31 - 1

```py
python run_vectorizers_32bit.py TfidfVectorizer 1000
Vectorizer: TfidfVectorizer
n_samples = 1000

# Resulting array (X):
 * indptr len=3 dtype=int32
 * indices len=131074 dtype=int32
 * data len=131074 dtype=float64
```


