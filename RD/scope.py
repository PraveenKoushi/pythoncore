"""
Scope in function
"""

# print("Hi - Checking scope")
#
# if True:
#     x=10
#
# print(x)

"""
Scope in function and outside
"""

# a = 20
#
#
# def confusion():
#     a = 30
#     return a
#
# print(a)
# print(confusion())


"""
local
function local
global
build in function scope
"""

a = 5


def confusion():
    a = 10

    def inconfusion():
        a = 15
        # return a

    inconfusion()
    return a


print(confusion())
