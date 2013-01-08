# Implementation of selected features in aspect oriented programming model, by monkey-patching
# minimum required version: Python 2.2

import types

class PointCut(object):
    """
    Abstract Pointcut
    """
    pass

class Advice(object):
    """
    Abstract Advice
    """
    def apply(self):
        raise NotImplementedError()

# brain dump:
#
# We will need to check all advices, e.g.[ABCAdvice] from attribute
# maybe use a centralized dictionary

# or use a proxy that saved to the weaved target class
# We do NOT want to save all aspects as attributes to target class

def patch_method(f, advices=[], profiled=False):
    # check all advices, e.g.[ABCAdvice] from attribute
    # maybe use a centralized dictionary, or a proxy
    def new_f(*args, **kwargs):
        for advice in advices:
            advice.apply()
        print 'applied'
        if f.im_class == type:
            # TODO: find a way to avoid this
            # avoid appyling additional 'cls' in positional args
            return f(*(args[1:]), **kwargs)
        return f(*args, **kwargs)
    return types.MethodType(new_f, f.im_self, f.im_class)

patchMethod = patch_method

def patch_object(f, advices=[]):
    # TODO
    pass

def patch_class(f, advices=[]):
    # TODO
    pass

