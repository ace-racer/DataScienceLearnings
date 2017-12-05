import gzip
import sys
import multiprocessing

CHUNK_SIZE = 16384


def worker(start_word_list_with_target):
	try:		
		start, word_list, target = start_word_list_with_target
		print "Worker... Start: {0}, Length of word list: {1} and Target: {2}".format(start, len(word_list), target)				
		location = start + word_list.index(target)		
		return location
	except ValueError:		
		return None
		

def read_gzip_file_contents(filename):
	try:
		return gzip.open(filename, 'rb')
	except:
		print "An exception occurred while trying to read the GZIP file: " + filename
		raise		
		
		
		
if __name__ == "__main__":
	words = [word.split()[0] for word in read_gzip_file_contents("words.gz")]
		
	target = sys.argv[1]
	print "Word to look for {0}".format(target)
	
	pool = multiprocessing.Pool(processes = 2)		
	start_words_list_with_target = [(start, words[start : start + CHUNK_SIZE], target) for start in range(0, len(words), CHUNK_SIZE)]		
	results = pool.map(worker, start_words_list_with_target)
	pool.close()
	pool.join()
	
	
	idx = [r for r in results if r is not None]	
	print "{0}th word is {1}".format(idx[0], target)
	