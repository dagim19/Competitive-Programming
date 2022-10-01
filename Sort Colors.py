class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        RED = 0
        WHITE = 1
        BLUE = 2

        number_of_reds = 0
        number_of_whites = 0
        number_of_blues = 0
        for i in range(len(nums)):
            if nums[i] == RED:
                number_of_reds = number_of_reds + 1
            elif nums[i] == WHITE:
                number_of_whites = number_of_whites + 1
            else:
                number_of_blues = number_of_blues + 1

        for i in range(len(nums)):
            if number_of_reds > 0:
                nums[i] = RED
                number_of_reds = number_of_reds - 1
            elif number_of_whites > 0:
                nums[i] = WHITE
                number_of_whites = number_of_whites - 1
            else:
                nums[i] = BLUE
