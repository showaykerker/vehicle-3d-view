import numpy as np

class Camera:
	def __init__(self, fx=5, fy=5, cx=300, cy=200):
		self._intrinsic_matrix = np.array([
			[fx, 0., cx],
			[0., fy, cy],
			[0., 0., 1.]
		])

	def set_pose(self, position, rotation):
		tx, ty, tz = position
		roll, pitch, yaw = rotation

		cosa = np.cos(yaw)
		sina = np.sin(yaw)
		cosb = np.cos(pitch)
		sinb = np.sin(pitch)
		cosr = np.cos(roll)
		sinr = np.sin(roll)

		self._extrinsic_matrix = np.array([
			[cosb*cosr, sina*sinb*cosr-cosa*sinr, cosa*sinb*cosr+sina*sinr, tx],
			[cosb*sinr, sina*sinb*sinr+cosa*cosr, cosa*sinb*sinr-sina*cosr, ty],
			[-sinb, sina*cosb, cosa*cosb, tz],
		]).astype(np.float32)

	def get_image_frame_coord(self, points):
		points = np.array(points)
		point_matrix = np.reshape(points, (-1, 3))
		point_matrix = np.concatenate((point_matrix, np.ones((point_matrix.shape[0], 1))), axis=1)
		# To camera coord
		res = np.matmul(self._extrinsic_matrix, point_matrix.transpose())
		# To image coord
		print(res)
		res = np.matmul(self._intrinsic_matrix, res).transpose()
		print(res)
		return res