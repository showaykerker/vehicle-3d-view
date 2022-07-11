import numpy as np
import cv2

class Canvas:
	def __init__(self, size=(400, 600)):
		self._size = np.array([size[0], size[1], 3])
		self._canvas = np.ones(self._size, dtype="uint8") * 192

	def add_line(self, start, end, color, width=2):
		cv2.line(
			self._canvas,
			start[:2].astype(np.int32).tolist(),
			end[:2].astype(np.int32).tolist(),
			color.tolist(),
			width)

	def show(self):
		cv2.imshow("view", self._canvas)
		cv2.waitKey(0)
		cv2.destroyAllWindows()