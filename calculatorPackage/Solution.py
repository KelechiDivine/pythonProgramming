def solution(numbers, target):
    number_map = {
        numbers[index]:
            index for index in range(len(numbers))
    }

    for iterate in number_map:
        half_num = target - iterate
        if number_map.get(half_num):
            first_index = number_map[iterate]
            second_index = number_map[half_num]
            return first_index, second_index