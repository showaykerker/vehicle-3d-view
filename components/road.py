import numpy as np
class Road:
	def __init__(
		self,
		width=4.0,
		color=(128, 128, 255),
		start_point=(0, 5),
		end_point=(180, 5)):
		#
		self._width = width
		self._color = np.array(color)
		self._start_point = np.array(start_point)
		self._end_point = np.array(end_point)

	def get_color(self):
		return self._color

	def get_left(self):
		start = self._start_point - np.array([0., self._width/2.0])
		end = self._end_point - np.array([0., self._width/2.0])
		return np.array([start, end]).astype("int")

	def get_right(self):
		start = self._start_point + np.array([0., self._width/2.0])
		end = self._end_point + np.array([0., self._width/2.0])
		return np.array([start, end]).astype("int")