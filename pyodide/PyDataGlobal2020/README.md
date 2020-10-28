# Install the same versions as pyodide 0.16

conda create -n pyodide-demo python=3.8.2
conda activate pyodide-demo
pip install numpy==1.15.4
pip install https://github.com/scipy/scipy/archive/v0.17.1.tar.gz
pip install scikit-learn==0.20.1
pip install pandas joblib==0.11
export SKLEARN_SITE_JOBLIB=True
