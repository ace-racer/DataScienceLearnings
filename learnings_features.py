import math
import sys

# Learn the features of Python which are only in Python
def compute_hcf(a, b):
	"""Computes the HCF of positive integers a and b """
	if a > 0 and b > 0:		
		
		# Swap values if a is greater than b
		if a > b:
			a, b = b, a					
		
		#	Create list with factors of smaller value (a)
		a_factors_tuples = [ (f, a//f) for f in xrange(1, int(math.sqrt(a)) + 2) if a % f == 0]
		a_factors_tuples.append((1, a))
		
		#	Create set with factors of larger value (b)
		b_factors_tuples_set = { (f, b//f) for f in xrange(1, int(math.sqrt(b)) + 2) if b % f == 0 }
		b_factors_tuples_set.add((1, b))
		print "Factors of {0}: ".format(b) + str(b_factors_tuples_set)
		
		print "Factors of {0}: ".format(a) + str(a_factors_tuples)
		
		# unzip the factors of a into 2 tuples
		a_factors_left, a_factors_right = zip(*a_factors_tuples)
		
		# convert the tuples to lists and then concatenate the lists
		a_factors = list(a_factors_left) + list(a_factors_right)
		
		# sort the factors of the smaller number in descending order
		a_factors_sorted = sorted(a_factors, reverse = True)
		print "Sorted Factors of {0}: ".format(a) + str(a_factors_sorted)
		
		# list comprehension - and using tuples
		common_factors = [ a_factor 
						   for a_factor in a_factors_sorted 
						   for b_factor_tuple in b_factors_tuples_set
						   if a_factor in (b_factor_tuple[0], b_factor_tuple[1]) ]
						   
		# the first common factor is the HCF
		return common_factors[0]
		
		
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
hcf = compute_hcf(num1, num2)
print "HCF of {0} and {1} is {2} ".format(str(num1), str(num2), str(hcf))