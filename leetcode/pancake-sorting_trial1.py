class Solution(object):
    def pancakeSort(self, arr):
        res = []
        n = len(arr)

        for size in range(n, 1, -1):
            max_index = arr.index(size)

            if max_index != size - 1:

                if max_index != 0:
                    res.append(max_index + 1)
                    arr[:max_index+1] = arr[:max_index+1][::-1]

                res.append(size)
                arr[:size] = arr[:size][::-1]

        return res