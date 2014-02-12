
def on_off(intensity, eps):
	if intensity > eps:
		return 100
	else:
		return 0

def rgb(set, eps):
	return (on_off(set[0], eps), on_off(set[1], eps), on_off(set[2], eps))
	
	
