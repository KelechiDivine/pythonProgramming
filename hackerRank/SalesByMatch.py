class SalesByMatch(object):

    def sock_merchant(self, numbers_of_socks, given_array) -> int:
        count = 0
        given_array = []
        for current_item in numbers_of_socks:
            if given_array[current_item] == given_array[current_item + 1]:
                count += 1
        return count
