import math
import matplotlib.pyplot as pp


def smoothen(data, window_size=3):
    """Smoothen the data by averaging the values in the window size"""
    if data is None:
        raise ValueError

    data_length = len(data)

    if data_length == 1:
        return data[0]

    if window_size > data_length:
        raise ValueError("The window size is greater than the length of the data")

    running_sum = [0]*data_length
    running_sum[0] = data[0]
    for i in range(1, data_length):
        running_sum[i] = running_sum[i - 1] + data[i]

    smoothened = []
    half_window_size = window_size // 2
    for i in range(0, data_length):
        left_index = max(0, i - half_window_size)
        print("Left index: " + str(left_index))
        right_index = min(data_length - 1, i + half_window_size)
        print("Right index: " + str(right_index))
        actual_window_size_used = right_index - left_index + 1
        print("Actual window size used: " + str(actual_window_size_used))

        if left_index == 0:
            window_sum = running_sum[right_index]
        else:
            window_sum = running_sum[right_index] - running_sum[left_index - 1]

        print("Window sum: " + str(window_sum))
        smoothened.append(window_sum/actual_window_size_used)

    return smoothened


original_data = [10, 30, 25, 15, 17, 38, 41, 51, 63, 70]
smoothened_data = smoothen(original_data)
print(smoothened_data)

original_plot = pp.plot([x for x in range(0, 10)], original_data, label='Original')
smoothened_plot = pp.plot([x for x in range(0, 10)], smoothened_data, label='Smoothed')
pp.show()
pp.legend(handles=[original_plot, smoothened_plot])
# pp.title()