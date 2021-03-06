
__author__ = "Felipe Zapata"

__all__ = ['chunksOf', 'concat', 'concatMap', 'dict2Setting', 'flatten',
           'lookup',
           'repeatN', 'replicate', 'settings2Dict', 'zipWith', 'zipWith3']

# ======================> Python Standard  and third-party <===================
from functools import reduce
from itertools import chain
from pymonad   import curry

# ======================> List Functions <========================


def chunksOf(xs, n):
    """Yield successive n-sized chunks from xs"""
    for i in range(0, len(xs), n):
        yield xs[i:i + n]


def concat(xss):
    """The concatenation of all the elements of a list"""
    return list(chain(*xss))


def concatMap(f, xss):
    """Map a function over all the elements of a container and concatenate the resulting lists"""
    return concat(list(map(f, xss)))


def flatten(xs):
    return reduce(lambda x, y: x + y, xs)


def repeatN(n, a):
    for x in range(n):
        yield a


def replicate(n, a):
    return list(repeatN(n, a))


@curry
def zipWith(f, xs, ys):
    """zipWith generalises zip by zipping with the function given as the first argument"""
    return [f(*rs) for rs in zip(xs, ys)]


@curry
def zipWith3(f, xs, ys, zs):
    """
    The zipWith3 function takes a function which combines three elements,
    as well as three lists and returns a list of their point-wise combination.
    """
    return [f(*rs) for rs in zip(xs, ys, zs)]


# ================> Dict Functions
from qmworks.settings   import Settings


def lookup(d, k):
    """
    Look `k` in `d` if it is not an element returns `None`.
    """
    try:
        return d[k]
    except KeyError:
        return None


def settings2Dict(s):
    """
    Transform a Settings object into a dict.
    """
    d = {}
    for k, v in s.items():
        if not isinstance(v, Settings):
            d[k] = v
        else:
            d[k] = settings2Dict(v)

    return d


def dict2Setting(d):
    """
    Transform recursively a dict into a Settings object.
    """
    r = Settings()
    for k, v in d.items():
        if isinstance(v, dict):
            r[k] = dict2Setting(v)
        else:
            r[k] = v

    return r
