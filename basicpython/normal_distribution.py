import math
import matplotlib.pyplot as plt

def normal_pdf(x, mu = 0, sigma = 1):
	sqrt_two_pi = math.sqrt(2 * math.pi)
	return math.exp(-(x-mu) ** 2 / 2 / sigma ** 2)/ (sqrt_two_pi * sigma)


if __name__ == "__main__":
	xs = [x / 10.0 for x in range(-50, 50)]
	plt.plot(xs, [normal_pdf(x, sigma = 1) for x in xs], '-', label = 'mu=0, sigma =1')
	plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0, sigma =2')
	plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], ':', label='mu=0, sigma =0.5')
	plt.plot(xs, [normal_pdf(x, sigma=1, mu = -1) for x in xs], '-.', label='mu=-1, sigma =1')
	plt.legend()
	plt.title("Various Normal PDFs")
	plt.show()
