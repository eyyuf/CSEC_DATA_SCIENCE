def add(numbers): 
    result = 0 
    for num in numbers: #iterates through the list of numbers and adds them to result
        result += num
    return result

def subtract(numbers): #iterates through the list of numbers and substratcs from result which is the first value of our list at the start
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers): #iterates through the list of numbers and multiplies them to result
    result = 1 
    for num in numbers:
        result *= num
    return result

def divide(numbers): #iterates through the list of numbers and divides from result which is the first value of our list at the start
    result = numbers[0]
    for num in numbers[1:]:
        result /= num  # assumes no zeros
    return result

def calculator():
    while True:
        #this lets us choose based on our number of choice 
        print(" Multi-Number Calculator ")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        #checks our number of choice in each iteration
        choice = input("Choose an option (1-5): ")
        if choice == '5':
            print("Exiting calculator...")
            break

        #take input from users 
        nums = input("Enter numbers separated by spaces: ")

        #change it to an intger and convert it to a list
        numbers = list(map(float,nums.split()))

        #based on the number of our choice perform the operation on our numbers
        if choice == '1':
            result = add(numbers)
        elif choice == '2':
            result = subtract(numbers)
        elif choice == '3':
            result = multiply(numbers)
        elif choice == '4':
            result = divide(numbers)
        else:
            print("Invalid choice.")
            continue

        print("Result:", result)
calculator()