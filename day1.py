with open("day1_input.txt") as file:
    input_list = [int(line.strip()) for line in file]


def two_sum_to_2020(input_list, sum_to_find):
    temp_set = set()
    for i in range(len(input_list)):
        temp = sum_to_find - input_list[i]
        if temp in temp_set:
            print(input_list[i], '+', temp, '=', sum_to_find, '; result =', input_list[i]*temp)
        temp_set.add(input_list[i])


def three_num_sum_to_2020(input_list, sum_to_find):
    temp_set = set()
    for i in range(len(input_list)):
        temp = sum_to_find - input_list[i]
        for j in range(i+1, len(input_list)):
            if (temp - input_list[j]) in temp_set:
                print(input_list[i], '+', input_list[j], '+', temp - input_list[j], '=', sum_to_find, '; result =', input_list[i]*input_list[j]*(temp - input_list[j]))
            temp_set.add(input_list[j])


two_sum_to_2020(input_list, 2020)
three_num_sum_to_2020(input_list, 2020)



