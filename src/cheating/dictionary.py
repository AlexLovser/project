
def getitem(obj, name, default=None):
    for i in obj():
        if i[0] == name:
            return i[1]
        
    return default


def setitem(obj, name, value):
    for i in obj():
        if i[0] == name:
            i[1] = value
            return
    
    raise KeyError('No such key: %s' % name)


def contains(obj, name):
    for i in obj():
        if i[0] == name:
            return True
        
    return False


def values(obj):
    v_list = []

    for i in obj():
        v_list.append(i[1])

    return v_list


def keys(obj):
    k_list = []

    for i in obj():
        k_list.append(i[0])

    return k_list


def items(obj):
    return obj()


def dictionary(data):
    DATA = data
    # we could use hash() function to implement the real dictionary, but I think for performance thats will be enough

    def inner_dict(name=None, value=None, default=None):
        if not any((name, value)):
            return DATA
        elif not value:
            return getitem(DATA, name, default=default)
        else:
            return setitem(DATA, name, value)

    
    return inner_dict
