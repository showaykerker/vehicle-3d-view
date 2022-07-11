import copy
import numpy as np

class Point:
	def __init__(self, idx, x, y, z, links, links_color=[]):
		assert type(idx) in [float, int, np.float32, np.float64], type(idx)
		assert type(x) in [float, int, np.float32, np.float64], type(x)
		assert type(y) in [float, int, np.float32, np.float64], type(y)
		assert type(z) in [float, int, np.float32, np.float64], type(z)
		assert type(links) in [list, ], type(links)
		self._idx = idx
		self._p = (x, y, z)
		self._links = copy.deepcopy(links)
		self._links_color = copy.deepcopy(links_color)

	def add_link(self, idx, color):
		assert type(idx) in [float, int, np.float32, np.float64]
		self._links.append(idx)
		self._links_color.append(color)

	def get_links(self):
		return self._links, self._links_color

	def get_xyz(self):
		return self._p

	def __str__(self):
		string = "<Class Point #{}: ({:.4f}, {:.4f}, {:.4f}), links={}>"\
			"".format(self._idx, *self._p, self._links)
		return string

class PointManager:
	def __init__(self):
		self.reset()

	def reset(self):
		self._points = []

	def add_vehicle(self, vehicle):
		box, color = vehicle.get_box_and_color()
		self._add_box(box, color)

	def add_road(self, road):
		pass

	def _add_box(self, box, color):
		assert type(box) is list
		assert len(box) == 9
		idx = len(self._points)
		start = idx
		for i in range(len(box)):
			x, y, z = box[i]
			if i == len(box) - 1:
				links = [idx - 1]
				links_color = [color]
			elif i == 0:
				links = [idx + 1]
				links_color = [color]
			else:
				links = [idx - 1, idx + 1]
				links_color = [color, color]
			self._points.append(Point(idx, x, y, z, links, links_color))

			idx += 1

		return (start, idx - 1)

	def get_links(self, idx):  # links, links_color
		return self._points[idx].get_links()

	def get_all_links(self):
		all_links = []
		link_colors = []
		for idx, p in enumerate(self._points):
			links, colors = p.get_links()
			for i, next_idx in enumerate(links):
				next_p = self._points[next_idx]
				next_color = colors[i]
				if next_idx > idx:
					all_links.append(np.array([p.get_xyz(), next_p.get_xyz()]).astype(np.float32))
					link_colors.append(next_color)
		return np.array(all_links).astype(np.float32), np.array(link_colors).astype(np.uint8)
