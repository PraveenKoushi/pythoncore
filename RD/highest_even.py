print("Higest Even find")


def higest_even(*li):
    result = 0
    for val in li:
        print(val)
        if val%2==0:
            print(f'even {val}')
            if val > result:
                result = val

    print(f'highest even is {result}')


higest_even(11, 2, 15, 16, 18, 0)
