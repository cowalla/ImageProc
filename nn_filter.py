def pixeldiff(p1, p2):
	return (abs(p1[0] - p2[0]), abs(p1[1] - p2[1]), abs(p1[2] - p2[2]))

	
def nn(d1, d2, d3, d4, d5, d6, d7, d8):
	pixeldiff(pixeldiff(pixeldiff(d1, d2), pixeldiff(d3, d4)), pixeldiff(pixeldiff(d5, d6), pixeldiff(d7, d8)))



