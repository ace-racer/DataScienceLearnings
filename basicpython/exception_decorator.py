import sys

def exception_handling(func):
	print "Entering exception handling decorator module"
	def log_exception(*args, **kwargs):
		try:			
			return func(*args, **kwargs)
		except:
			print ("Error encountered: " + str(sys.exc_info()[0]))
			# raise
	return log_exception

@exception_handling
def divide(a, b):
	print "Performing " + str(a) + "/" + str(b)
	return a/b
	
print divide(10, 2)
print divide(10, 0)