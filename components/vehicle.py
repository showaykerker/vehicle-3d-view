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

	def get_box_and_color(self):
		x, y, z = self._position
		theta = self._orientation
		l, w, h = self._size
		hd = (l ** 2 + w ** 2) ** 0.5
		alpha = np.arctan2(l, w)
		beta = np.pi / 2.0 - alpha
		angLF = theta + alpha
		angLR = angLF + beta * 2.0
		angRR = angLR + alpha * 2.0
		angRF = angRR + beta * 2.0
		hh = h / 2.0

		return [
			(x + hd * np.cos(angLF), y + hd * np.sin(angLF), z + hh / 2.0),
			(x + hd * np.cos(angLR), y + hd * np.sin(angLR), z + hh / 2.0),
			(x + hd * np.cos(angRR), y + hd * np.sin(angRR), z + hh / 2.0),
			(x + hd * np.cos(angRF), y + hd * np.sin(angRF), z + hh / 2.0),
			(x + hd * np.cos(angLF), y + hd * np.sin(angLF), z - hh / 2.0),
			(x + hd * np.cos(angLR), y + hd * np.sin(angLR), z - hh / 2.0),
			(x + hd * np.cos(angRR), y + hd * np.sin(angRR), z - hh / 2.0),
			(x + hd * np.cos(angRF), y + hd * np.sin(angRF), z - hh / 2.0),
			(x + hd * np.cos(angLF), y + hd * np.sin(angLF), z + hh / 2.0)
		], self._color