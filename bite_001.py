def sum_numbers(numbers=None):
    if numbers==None:
        return sum(range(101))
    elif not numbers:
        return 0
    else:
        for i in numbers:
            return sum(numbers)

print(sum_numbers([1,2]))
