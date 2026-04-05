def find_largest(numbers):
    max = numbers[0]  # we Assume first number is the largest

    # iterate through each number 
    for num in numbers:
        # if the current num is greater than the max value we update the max to be that number
        if num > max:
            max = num
    return max

numbers = input("enter values: ")

# numbers.split() changes our input of numbers to a list
# map(int,) changes the strings inside the list to int
# list() because the does not return a list we have to turn that again into a list befor applying the find_largest function 



nums = list(map(int,numbers.split()))

#apply the function to our list of numbers
res = find_largest(nums)

print(f"the largest number is: {res}")