import numpy as np
import scipy.sparse
import pytest
import itertools

np.random.seed(42)

n_samples = 100
n_features = 10000


def init_arrays():
    X = scipy.sparse.rand(n_samples, n_features, format='csr')

    X.indices = X.indices.astype('int64')
    X.indptr = X.indptr.astype('int64')
    y = np.random.randint(0, 10, size=(n_samples,))
    return X, y


@pytest.mark.parametrize('norm, copy',
                         itertools.product(['l1', 'l2'],
                                           [False, True]))
def test_preprocessing_normalize(norm, copy):
    from sklearn.preprocessing import normalize

    print({"norm": norm, 'copy': copy}, ' ', end='')

    X, y = init_arrays()

    assert str(X.indices.dtype) == 'int64'

    normalize(X, norm=norm, copy=copy)


@pytest.mark.parametrize('algorithm', ['randomized', 'arpack'])
def test_decomposition_truncatedsvd(algorithm):
    from sklearn.decomposition import TruncatedSVD

    X, y = init_arrays()

    svd = TruncatedSVD(algorithm=algorithm)
    svd.fit(X)
    svd.transform(X)


@pytest.mark.parametrize('solver, penalty',
                         [#('liblinear', 'l1'),
                          #('liblinear', 'l2'),
                          ('newton-cg', 'l2'),
                          ('lbfgs', 'l2'),
                          ('sag', 'l2')])
def test_linear_model_logisticregression(solver, penalty):
    from sklearn.linear_model import LogisticRegression

    X, y = init_arrays()

    cl = LogisticRegression(penalty=penalty, solver=solver)
    cl.fit(X, y)

    cl.predict(X)


@pytest.mark.parametrize('loss, penalty',
                         itertools.product(['hinge', 'log', 'modified_huber',
                                            'squared_hinge', 'perceptron'],
                                           ['l1', 'l2', 'elasticnet']))
def test_linear_model_sgdclassifier(loss, penalty):
    from sklearn.linear_model import SGDClassifier

    X, y = init_arrays()

    cl = SGDClassifier(penalty=penalty, loss=loss)
    cl.fit(X, y)

    cl.predict(X)


@pytest.mark.parametrize('estimator_name', ['LinearRegression', 'ElasticNet'])
def test_linear_model_estimator(estimator_name):
    import sklearn.linear_model

    Estimator = getattr(sklearn.linear_model, estimator_name)

    X, y = init_arrays()

    cl = Estimator()
    cl.fit(X, y)

    cl.predict(X)
