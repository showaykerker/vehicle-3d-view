import numpy as np

class Waypoint:
	def __init__(
		self,
		x=0.0, y=0.0, heading=0.0,
		left_width=2.0, right_width=2.0):
		#
		self._x = x
		self._y = y
		self._heading = heading
		self._left_width = left_width
		self._right_width = right_width

class Road:
	def __init__(
		self,
		width=12.0,
		color=(128, 128, 255),
		start_point=(-6., 0.),
		length=500,
		heading=np.pi/6.):
		#
		self._width = width
		self._color = np.array(color)
		self._start_point = np.array(start_point)
		self._end_point = np.array(start_point) + np.array([length*np.cos(heading), length*np.sin(heading)])
		self._heading = heading

	def get_color(self):
		return self._color

	def get_left(self):
		start = self._start_point - np.array([self._width/2.0 * np.sin(self._heading), self._width/2.0 * np.cos(self._heading)])
		end = self._end_point - np.array([self._width/2.0 * np.sin(self._heading), self._width/2.0 * np.cos(self._heading)])
		return [
			(start[0], start[1], 0.),
			(end[0], end[1], 0.)
		]

	def get_right(self):
		start = self._start_point + np.array([self._width/2.0 * np.sin(self._heading), self._width/2.0 * np.cos(self._heading)])
		end = self._end_point + np.array([self._width/2.0 * np.sin(self._heading), self._width/2.0 * np.cos(self._heading)])
		return [
			(start[0], start[1], 0.),
			(end[0], end[1], 0.)
		]

	def get_center(self):
		return [
			(self._start_point[0], self._start_point[1], 0.),
			(self._end_point[0], self._end_point[1], 0.)
		]