nums = []

with open("input.txt") as file:
    lines = file.readlines()
    nums = [line.rstrip() for line in lines]

gamma = ""
epsilon = ""
for i in range(len(nums[0])):
    i_digits = [num[i] for num in nums]
    ones = i_digits.count("1")
    if ones > 500:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"


gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print("Gamma: ", gamma)
print("Epsilon: ", epsilon)
print("Mult: ", gamma * epsilon)


# Part 2 Recursive function


"""
Base Case: If num(0) == num(1): return with the one with 1 in its postion
Recusrive Case: Rerturn a list of the specfied value and next postion

"""

nums = []

with open("input.txt") as file:
    lines = file.readlines()
    nums = [line.rstrip() for line in lines]

def oxygen_and_co2(numbers, pos, co2):
    pos_digits = [num[pos] for num in numbers]
    ones = pos_digits.count("1")
    half = len(numbers)/2
    more_common = "1" if ones >= half else "0"
    if co2:
        # The less common one
        more_common = "1" if ones < half else "0"

    new_numbers = [num for num in numbers if num[pos] == more_common]
    if len(new_numbers) == 1:
        return int(new_numbers[0], 2)

    return oxygen_and_co2(new_numbers, pos+1, co2)

oxygen_rating = oxygen_and_co2(nums, 0, False)
co2_rating = oxygen_and_co2(nums, 0, True)
print("Oxygen: ", oxygen_rating)
print("CO2: ", co2_rating)
print("Mult: ", oxygen_rating * co2_rating)






    