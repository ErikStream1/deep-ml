import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	gradient = np.array(gradient)
	norm = np.linalg.norm(gradient, ord = 2)
	if norm == 0:
		return {'magnitude': norm, 'direction':[0,0], 'descent_direction': [0,0]} 
	unitVec = np.array([i / norm for i in gradient])

	return {'magnitude': norm, 'direction':unitVec, 'descent_direction': -1*unitVec} 