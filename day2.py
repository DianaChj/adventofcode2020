d = {}
with open("day2_input.txt") as file:
    for line in file:
        k, v = line.split(':')
        if k in d:
            d[k].append(v.strip())
        else:
            d[k] = [v.strip()]


def old_policy(d):
    l = []
    for key, value in d.items():
        nums, letter = key.split()
        num1, num2 = nums.split('-')
        for val in value:
            if int(num1) <= val.count(letter) <= int(num2):
                l.append(val)
    return len(l)


def new_policy(d):
    l = []
    for key, value in d.items():
        nums, letter = key.split()
        num1, num2 = nums.split('-')
        for val in value:
            if (val[int(num1)-1] == letter and val[int(num2)-1] != letter) or (val[int(num1)-1] != letter and val[int(num2)-1] == letter):
                l.append(val)
    return len(l)


print(old_policy(d))
print(new_policy(d))
