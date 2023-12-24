# give an aaray with some integer type value. Write a python script to sort array values.
# from array import *

# a1 = array("i", [50, 43, 5, 16, 77, 4, 9])
# x = sorted(a1)
# print(x)

# given a list of hetrogeneous elements. Write a python script to remove all the non int values from the list.
# l1 = ["amit", 28, 0.9, "null", 9, 75, 7343, 90]
# updated_l1 = [x for x in l1 if isinstance(x, int)]
# print(updated_l1)

# write a python script to calculate avg. of elements of LIST.
# num = [1, 2, 3, 4, 5, 6, 7]
# total = sum(num)

# average = total / len(num)

# print("List: ", num)
# print("average:", average)

# write a python script to create a list of n prime numbers.




# write a python script to create a list of first n terms of fibonacci series..
def generate_fibonacci(n):
    """Generate a list of the first n terms of the Fibonacci series."""
    fibonacci_list = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_list.append(a)
        a, b = b, a + b

    return fibonacci_list

# Example: Generate the first 10 terms of the Fibonacci series
n = 10
fibonacci_sequence = generate_fibonacci(n)

# Print the result
print(f"The first {n} terms of the Fibonacci series are:", fibonacci_sequence)
