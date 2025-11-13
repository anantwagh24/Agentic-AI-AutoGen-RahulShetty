import copy


def deep_copy():

    original = [[1,2],[3,4]]
    deep=copy.deepcopy(original)


    deep[0][0]=99
    print(f"Original: {original}")
    print(f"deep copy: {deep}")

deep_copy()