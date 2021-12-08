class WorldPopulationGrowth(object):
    
    def four_numbers_encrypting(self, first_integer:int, second_integer:int,
                                third_integer:int, fourth_integer:int):
        
        first_result = first_integer + 7
        second_result = second_integer + 7
        third_result = third_integer + 7
        fourth_result = fourth_integer + 7
        
        print(f"Your input: {first_integer} {second_integer} {third_integer} {fourth_integer}")
        
        sum = first_result + second_result + third_result + fourth_result
        get_the_remainder_after_dividing_the_digit_value_by_ten = sum % 10
        
        print(f"The remainder is: {get_the_remainder_after_dividing_the_digit_value_by_ten}")
        
        # swap logic
        swap_var = first_integer
        swap_var_2 = second_integer
        
        first_integer = third_integer
        third_integer = swap_var
        
        second_integer = fourth_integer
        fourth_integer = swap_var_2
        
        print(f"Encrypted values after swapping: {first_integer} {second_integer} "
              f"{third_integer} {fourth_integer}")
