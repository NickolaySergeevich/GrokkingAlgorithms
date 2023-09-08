class SelectionSort:
    """A class with everything you need to implement selection sorting"""

    @staticmethod
    def _find_smallest(nums: list) -> int:
        """Finding the minimum number in a list of numbers"""
        smallest_num = nums[0]
        smallest_num_index = 0

        for index in range(1, len(nums)):
            if nums[index] < smallest_num:
                smallest_num = nums[index]
                smallest_num_index = index

        return smallest_num_index

    @staticmethod
    def sort_nums(nums: list) -> list:
        """
        Selection sort for integers
        As a result of the work, the transferred list becomes empty
        """
        new_nums = list()

        for index in range(len(nums)):
            smallest_num = SelectionSort._find_smallest(nums)
            new_nums.append(nums.pop(smallest_num))

        return new_nums


def main() -> None:
    """Tests"""
    nums = [1, 15, 16, -5, 0]
    print(*SelectionSort.sort_nums(nums))


if __name__ == '__main__':
    main()
