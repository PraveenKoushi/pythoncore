print("Arg types testing ")


def super_func(*args, **kargs):
    sum_kargs = 0
    for karg in kargs.values():
        sum_kargs += karg

    print(type(sum_kargs))
    tatal = sum(args) + sum_kargs
    return(tatal)


result = super_func(1, 2, 3, 4, 5, kargs1=10, kargs2=20)
print(result)
