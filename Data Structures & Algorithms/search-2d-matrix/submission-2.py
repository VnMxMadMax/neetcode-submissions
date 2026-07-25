class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix = list(matrix)
        # for i in matrix:
        #     for j in i:
        #         if j == target:
        #             return True
        #         else:
        #             continue
        # return False

        low = 0
        high = len(matrix)-1
        while low <= high:
            mid = low + (high - low)//2

            print(mid)
            # print(matrix[mid][n_low])

            n_low = 0
            n_high = len(matrix[0])-1

            if matrix[mid][n_low] == target or matrix[mid][n_high] == target:
                return True

            elif matrix[mid][n_low] < target and matrix[mid][n_high] > target:


                while n_low <= n_high:
                    print("First Condition")
                    n_mid = n_low + (n_high - n_low)//2

                    if matrix[mid][n_mid] == target:
                        return True

                    elif matrix[mid][n_mid] < target:
                        n_low = n_mid+1

                    else:
                        n_high = n_mid-1

                return False

            elif matrix[mid][n_low] < target:
                print("Second Condition")
                low = mid+1

            else:
                print("Third Condition")
                high = mid-1
        return False

