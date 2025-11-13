# Tuple Example Program

def tuple_example():

    # defining tuple
    mix_tuple=(1,"apple", 'z', "z")
    print(f"tuple: {mix_tuple}")

    #converting it to list
    tolist=list(mix_tuple)
    print(f"converted list: {tolist}")

    # adding value to converted tuple
    tolist[0]="banana"
    print(f"revised list: {tolist}")

tuple_example()