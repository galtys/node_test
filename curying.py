def arimean(*args):
    return sum(args) / len(args)
def curry(func):
    # to keep the name of the curried function:
    curry.__curried_func_name__ = func.__name__
    f_args, f_kwargs = [], {}
    def f(*args, **kwargs):
        nonlocal f_args, f_kwargs
        if args or kwargs:
            f_args += args
            f_kwargs.update(kwargs)
            return f
        else:
            result = func(*f_args, *f_kwargs)
            f_args, f_kwargs = [], {}
            return result
    return f
curried_arimean = curry(arimean)
curried_arimean(2)(5)(9)(4, 5)
# it will keep on currying:
curried_arimean(5, 9)
print(curried_arimean())
# calculating the arithmetic mean of 3, 4, and 7
print(curried_arimean(3)(4)(7)())
# calculating the arithmetic mean of 4, 3, and 7
print(curried_arimean(4)(3, 7)())
