# Written for practice from Joel Grus book: Data Science from Scratch First Principal

from matplotlib import pyplot as plt
from collections import Counter


def decile(grade):
    return (grade / 10) * 10


grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
histogram = Counter(decile(grade) for grade in grades)
plt.bar([x for x in histogram.keys()],
        histogram.values(),
        8)
plt.axis([-5, 105, 0, 5])
plt.xticks([10 * i for i in range(11)])
plt.xlabel("Decile")
plt.ylabel(" # of Students")
plt.title("Distribution of exam 1 grades")
plt.show()


