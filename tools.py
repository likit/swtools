def get_bmi(weight, height):
	weight = float(weight)
	height = float(height)
	assert weight > 30, "Invalid weight for adults"
	assert height > 1.0, "Invalid height for adults"
	bmi = weight/(height)**2
	return bmi
