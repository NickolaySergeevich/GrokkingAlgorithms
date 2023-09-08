class BinarySearch:
    """Class for implementing binary search options"""

    @staticmethod
    def search_num(nums: tuple | list, num_need: int) -> int | None:
        """Binary search for a number in a sorted tuple | list"""
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess == num_need:
                return mid
            elif guess > num_need:
                high = mid - 1
            else:
                low = mid + 1

        return None


def main() -> None:
    """Tests"""
    nums = (1, 2, 3, 4, 5, 6)
    print(BinarySearch.search_num(nums, 3))
    print(BinarySearch.search_num(nums, -5))


if __name__ == '__main__':
    main()
