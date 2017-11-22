# Benchmarks and tests for scikit-learn PR #9147

For context, see [scikit-learn#9147](https://github.com/scikit-learn/scikit-learn/pull/9147).

1. The performance benchmark can be run with the `benchmarks/bench_text_vectorizers.py` script (included in scikit-learn repo),
 
   * before this PR: see output in [`bench_master.log`](./bench_master.log)
   * with this PR: see output in [`bench_PR.log`](./bench_PR.log)

   => no performance / memory usage impact.

2. The tests of 64 bit sparse arrays indices can be run on Linux with [`run.sh`](./run.sh). This extract text features with the 3 vectorizers present in scikit-learn on a small and a large dataset (at least 90 GB RAM needed).

   * before this PR: see output in ['results_master.log'](./results_master.log). We get 32 bit sparse array indices for a small indices and exceptions (due to overflows) for the large dataset
   * after this PR: see output in ['results_PR.log'](./results_PR.log). We get 32 bit indices for the small dataset and 64 bit indices for the large dataset for all 3 vectorizers.

