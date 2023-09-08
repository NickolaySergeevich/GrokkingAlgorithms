class RecursiveAlgorithms:
    """
    Examples of recursive algorithms
    Mine and from the book
    """

    @staticmethod
    def sum_nums_mine(nums: tuple | list) -> int:
        """Recursive sum of numbers (int and float)"""
        if len(nums) == 1:
            return nums[0]

        return nums[0] + RecursiveAlgorithms.sum_nums_mine(nums[1:])

    @staticmethod
    def sum_nums(nums: tuple | list) -> int:
        """Recursive sum of numbers (int and float)"""
        if not nums:
            return 0

        return nums[0] + RecursiveAlgorithms.sum_nums(nums[1:])

    @staticmethod
    def count_elems_mine(elems: tuple | list) -> int:
        """Recursive number of list elements"""
        if not elems:
            return 0

        return 1 + RecursiveAlgorithms.count_elems_mine(elems[1:])

    @staticmethod
    def max_num_mine(nums: tuple | list) -> int:
        """Recursive maximum number (int and float)"""
        if len(nums) == 1:
            return nums[0]

        another_max_num = RecursiveAlgorithms.max_num_mine(nums[1:])
        if nums[0] > another_max_num:
            return nums[0]
        else:
            return another_max_num

    @staticmethod
    def max_num(nums: tuple | list) -> int:
        """Recursive maximum number (int and float)"""
        if len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]

        sub_max = RecursiveAlgorithms.max_num(nums[1:])
        return nums[0] if nums[0] > sub_max else sub_max

    @staticmethod
    def binary_search_num_mine(nums: tuple | list, num_need: int) -> int | None:
        """Binary search for a number in a sorted tuple | list"""
        len_nums = len(nums)

        if len_nums == 1:
            if nums[0] == num_need:
                return 0
            else:
                return None
        elif len_nums == 0:
            return None

        low, high = 0, len_nums - 1
        mid = (low + high) // 2
        guess = nums[mid]
        if guess == num_need:
            return mid
        elif guess > num_need:
            return RecursiveAlgorithms.binary_search_num_mine(nums[:mid], num_need)
        else:
            return mid + RecursiveAlgorithms.binary_search_num_mine(nums[mid + 1:], num_need) + 1


def main() -> None:
    """Tests"""
    nums = (14, 15, -1, 200, 36, -2, 0)

    print(RecursiveAlgorithms.sum_nums_mine(nums))
    print(RecursiveAlgorithms.sum_nums(nums))
    print(RecursiveAlgorithms.count_elems_mine(nums))
    print(RecursiveAlgorithms.max_num_mine(nums))
    print(RecursiveAlgorithms.max_num(nums))

    nums = (1, 2, 3, 4, 5, 6)
    print(RecursiveAlgorithms.binary_search_num_mine(nums, 1))
    print(RecursiveAlgorithms.binary_search_num_mine(nums, 5))
    print(RecursiveAlgorithms.binary_search_num_mine(nums, -200))


if __name__ == '__main__':
    main()
