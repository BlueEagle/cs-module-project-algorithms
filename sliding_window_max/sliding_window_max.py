'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    output = []
    for i in range(len(nums)-k+1):
        window = nums[i:i+k]
        largest = False
        for j in range(len(window)):
            if not largest or window[j] > largest:
                largest = window[j]
        output.append(largest)
    print(output)
    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
