# Benchmarks for sklearn Ngram optimization (scikit-learn/scikit-learn#7567)
Run with `benchmark_count_vectorizer.py`
## Original version

HEAD is now at dee786ab2... DOC fix typo in NearestNeighbors docstring (#7545)
15it [19:45, 65.94s/it]

analyzer|ngram_range|CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---|---|---
char|(4, 4)|30.70(±0.02)|23.17(±0.15)|33.99(±0.03)
char_wb|(4, 4)|27.58(±0.02)|23.08(±0.09)|29.39(±0.02)
word|(1, 1)|5.20(±0.03)|4.83(±0.02)|5.43(±0.02)
word|(1, 2)|20.38(±0.01)|11.14(±0.04)|22.45(±0.01)
word|(1, 4)|65.77(±0.01)|20.47(±0.08)|71.53(±0.02)

## PR: method binding

HEAD is now at 874ed30cb... Improve ngram performance - method binding
15it [19:05, 63.29s/it]

analyzer|ngram_range|CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---|---|---
char|(4, 4)|29.57(±0.02)|22.54(±0.14)|32.93(±0.05)
char_wb|(4, 4)|26.36(±0.02)|22.23(±0.08)|28.21(±0.02)
word|(1, 1)|5.19(±0.02)|4.93(±0.02)|5.42(±0.03)
word|(1, 2)|19.59(±0.03)|10.33(±0.03)|21.63(±0.00)
word|(1, 4)|64.13(±0.03)|18.85(±0.09)|69.89(±0.03)

## PR: method binding + unigram list

HEAD is now at ac62e1c0c... Improve ngram performance - unigram list
15it [18:38, 61.44s/it]

analyzer|ngram_range|CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---|---|---
char|(4, 4)|29.58(±0.03)|22.07(±0.13)|32.93(±0.06)
char_wb|(4, 4)|26.33(±0.01)|21.88(±0.08)|28.21(±0.02)
word|(1, 1)|5.19(±0.00)|4.81(±0.02)|5.40(±0.01)
word|(1, 2)|18.24(±0.01)|8.97(±0.03)|20.32(±0.02)
word|(1, 4)|62.80(±0.02)|17.45(±0.07)|68.76(±0.05)

## PR: method binding + unigram list + list comprehension

HEAD is now at 49cb19c5a... Ngram list comprehension
15it [18:30, 60.94s/it]

analyzer|ngram_range|CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---|---|---
char|(4, 4)|28.94(±0.05)|21.54(±0.14)|32.37(±0.05)
char_wb|(4, 4)|26.40(±0.02)|21.95(±0.10)|28.42(±0.01)
word|(1, 1)|5.20(±0.02)|4.84(±0.03)|5.44(±0.02)
word|(1, 2)|18.19(±0.02)|8.91(±0.05)|20.25(±0.03)
word|(1, 4)|62.41(±0.01)|17.15(±0.08)|68.23(±0.01)

## PR: method binding + list comprehension


HEAD is now at 94e7298c8... Remove unigram shortcut
15it [18:51, 62.38s/it]

analyzer|ngram_range|CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---|---|---
char|(4, 4)|29.11(±0.02)|21.98(±0.17)|32.38(±0.02)
char_wb|(4, 4)|26.39(±0.01)|22.09(±0.10)|28.37(±0.01)
word|(1, 1)|5.21(±0.02)|4.91(±0.02)|5.43(±0.02)
word|(1, 2)|19.18(±0.01)|10.10(±0.05)|21.25(±0.01)
word|(1, 4)|63.20(±0.03)|18.32(±0.05)|69.08(±0.02)

