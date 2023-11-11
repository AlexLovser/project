

def create_type(name, extended=None):
    if extended is None:
        extended = ()

    return type(name, extended, {})


def type_wrapper(obj, method):
    def inner(*args, **kwargs):
        return method(obj, *args, **kwargs)
    
    return inner


