class Sort:

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]

        left = [x for x in arr[:-1] if x <= pivot]
        right = [x for x in arr[:-1] if x > pivot]

        return self.quick_sort(left) + [pivot] + self.quick_sort(right)


# ----- User Input -----

arr = list(map(int, input("Enter unsorted array elements: ").split()))

sorter = Sort()

merge_result = sorter.merge_sort(arr.copy())
quick_result = sorter.quick_sort(arr.copy())

print("Original array:", arr)
print("Merge Sort:", merge_result)
print("Quick Sort:", quick_result)