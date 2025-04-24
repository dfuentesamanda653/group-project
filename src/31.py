def sum_of_first_n_numbers(n):
    if n <= 0:
        return "The input should be a positive integer."
    else:
        return sum(range(1, n+1))

print(sum_of_first_n_numbers(int(input("Enter the number:"))))
