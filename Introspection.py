from inspect import getmembers, ismethod
from pprint import pprint

class obj:
    def __init__(self):
        self.num = 1

    def ret(self):
        return self.num

def introspection_info(obj):
    dict_ = {}
    dict_['type'] = str(type(obj)).replace("<class '", '').replace("'>", '')
    dict_['attributes'] = dir(obj)
    dict_['mettods_1'] = [i for i in dir(obj) if callable(getattr(obj, i))]
    dict_['methods_2'] = getmembers(obj, predicate=ismethod)
    dict_['module'] = obj_.__module__
    return dict_

if __name__ == '__main__':
    obj_ = obj()
    pprint(introspection_info(obj_))

