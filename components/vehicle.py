import numpy as np

class Vehicle:
	def __init__(
		self,
		length=4.63,
		width=1.78,
		height=1.43,
		color=(255, 0, 0),
		position=(0.0, 0.0, 0.0),
		orientation=0.0):
		#
		self._size = np.array((length, width, height))
		self._color = np.array(color)
		self._position = np.array(position)
		self._orientation = orientation

	def move_to(self, position=(0.0, 0.0, 0.0)):
		self._position = np.array(position)


	def get_position(self):
		return self._position.copy()

	def get_orientation(self):
		return self._orientation