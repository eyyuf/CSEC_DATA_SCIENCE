def reverses(s):
    r_string = ""

    # iterate through the string starting form the last index
    for i in range (len(s)-1,-1,-1):

        # then add them to the empty string starting from last index to give us a reversed string
        r_string += s[i]
    return r_string

# easier method using slicing
def s_reverse(strs):
    # (staring from the last iterate to the begining)
    return strs[::-1]



#get an input from users
stringg = input("enter any string: ")

reversed_string = reverses(stringg)

r_string = s_reverse(stringg)


print(f"from using for loop: {reversed_string}")
print(f"from using slicing: {r_string}")

