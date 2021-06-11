def odd_or_even(comm, nums):
    if comm == 'Odd':
        odd = []
        for el in nums:
            if el % 2 == 1:
                odd.append(el)
            total = sum(odd) * len(nums)
        return total

    elif comm == 'Even':
        even = []
        for el in nums:
            if el % 2 == 0:
                even.append(el)
            total = sum(even) * len(nums)
        return total


command = input()
numbers = [int(el) for el in input().split()]
print(odd_or_even(command, numbers))
