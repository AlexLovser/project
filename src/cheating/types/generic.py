import string

kwset = string.ascii_lowercase
kw = kwset[3] + kwset[8] + kwset[2] + kwset[19] + '()'
kw = eval(kw)

def create_type(name, extended=None):
    if extended is None:
        extended = ()

    return type(name, extended, kw)


def type_wrapper(obj, method):
    def inner(*args, **kwargs):
        return method(obj, *args, **kwargs)
    
    return inner


