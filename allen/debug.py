import ipdb
import IPython

def bin_bug():
    IPython.embed()
    assert False

def ipy():
    ipdb.set_trace()
    assert False
