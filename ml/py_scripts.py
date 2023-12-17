#even_squares = [x ** 2 for x in xrange(10) if x % 2 ==0]
#for idx, even_square in enumerate(even_squares):
	# print '#%d: %d' % (idx + 1, even_square)

	
def quick_sort_algo (nums, start, end):
	"""
	Incorrect approach
	"""
	if end >= start:
		pivot_elem = nums[start]
		elems_less_than_pivot_elem = [x for x in nums[start:end] if x < pivot_elem]		
		elems_greater_than_pivot_elem = [x for x in nums[start:end] if x > pivot_elem]
		pivot_elem_pos = len(elems_less_than_pivot_elem)
		nums[pivot_elem_pos] = pivot_elem
		quick_sort_algo(nums, start, pivot_elem_pos - 1)
		quick_sort_algo(nums, pivot_elem_pos + 1, end)
		

def quick_sort_algo_2 (arr):
	"""
	Correct approach taken from https://github.com/kuleshov/cs228-material/blob/master/tutorials/python/cs228-python-tutorial.ipynb
	"""
	if len(arr) <= 1:
		return arr
	
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quick_sort_algo_2(left) + middle + quick_sort_algo_2(right)


		
nums = [5,4,8,1,19,80,23,91,54]
sorted_nums = quick_sort_algo_2(nums)
print sorted_nums