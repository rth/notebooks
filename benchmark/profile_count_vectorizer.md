# Benchmarks for issue scikit-learn/scikit-learn#7567

Run with `profile_count_vectorizer.md`

# Original implementation
HEAD is now at dee786ab2... DOC fix typo in NearestNeighbors docstring (#7545)
15it [19:54, 66.92s/it]

analyzer|ngram_range|CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---|---|---
char|(4, 4)|31.3|23.7|34.6
char_wb|(4, 4)|27.6|23.3|29.5
word|(1, 1)|5.2|4.9|5.4
word|(1, 2)|20.4|11.4|22.5
word|(1, 4)|65.8|20.9|71.6

# Improve ngram performance: method binding
HEAD is now at 874ed30cb... Improve ngram performance - method binding
15it [19:06, 63.30s/it]

analyzer|ngram_range|CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---|---|---
char|(4, 4)|29.6|22.7|33.0
char_wb|(4, 4)|26.3|22.1|28.1
word|(1, 1)|5.2|4.9|5.4
word|(1, 2)|19.6|10.3|21.7
word|(1, 4)|64.2|18.8|70.3

# Improve ngram performance: method binding + unigram list
HEAD is now at ac62e1c0c... Improve ngram performance - unigram list
15it [18:42, 61.51s/it]

analyzer|ngram_range|CountVectorizer|HashingVectorizer|TfidfVectorizer
---|---|---|---|---
char|(4, 4)|29.8|22.1|33.2
char_wb|(4, 4)|26.3|21.8|28.3
word|(1, 1)|5.2|4.8|5.4
word|(1, 2)|18.3|9.0|20.4
word|(1, 4)|63.1|17.5|68.9
