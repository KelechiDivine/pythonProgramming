class SalesByMatch(object):

    def sock_merchant(self, numbers_of_socks, given_array: list) -> int:
        _a_distinct_elements = []
        for current_item in given_array:
            if current_item not in _a_distinct_elements:
                _a_distinct_elements.append(current_item)
        count = 0
        for current_item in _a_distinct_elements:
            count += given_array.count(current_item)//2
        return count
