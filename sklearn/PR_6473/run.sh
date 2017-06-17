set -x
time python run_vectorizers_32bit.py  CountVectorizer 100
time python run_vectorizers_32bit.py TfidfVectorizer 100
time python run_vectorizers_32bit.py HashingVectorizer 100
time python run_vectorizers_32bit.py  CountVectorizer 32769
time python run_vectorizers_32bit.py TfidfVectorizer 32769
time python run_vectorizers_32bit.py HashingVectorizer 32769
