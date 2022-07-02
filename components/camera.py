import numpy as np

class Camera:
	def __init__(self, fx=5, fy=5, cx=300, cy=200):
		self._intrinsic_matrix = np.zeros((3, 4)).astype(np.float32)
		self._intrinsic_matrix[0, 0] = fx
		self._intrinsic_matrix[1, 1] = fy
		self._intrinsic_matrix[0, 2] = cx
		self._intrinsic_matrix[1, 2] = cy
		self._intrinsic_matrix[2, 2] = 1.0

		self._extrinsic_matrix = np.zeros((4, 4)).astype(np.float32)

	def set_extrinsic_matrix(self, param):
		self._extrinsic_matrix = param.copy()

	def set_position(self, x, y, z):
		self._position = np.array([[x, y, z, 1]])
		self._extrinsic_matrix[3, 0] = x
		self._extrinsic_matrix[3, 1] = y
		self._extrinsic_matrix[3, 2] = z
		self._extrinsic_matrix[3, 3] = 1.0

	def set_rotation(self, row, pitch, yaw):
		rx = np.zeros((4, 4))
		ry = np.zeros((4, 4))
		rz = np.zeros((4, 4))
		rx[0, 0] = 1.0; rx[3, 3] = 1.0
		ry[0, 0] = 1.0; ry[3, 3] = 1.0
		rz[0, 0] = 1.0; rz[3, 3] = 1.0
		rx[1:3, 1:3] = np.array([
			[np.cos(row), -np.sin(row)],
			[np.sin(row), np.cos(row)]
		])
		ry[0, 0] = np.cos(pitch)
		ry[0, 2] = np.sin(pitch)
		ry[2, 0] = -np.sin(pitch)
		ry[2, 2] = np.cos(pitch)
		rz[:2, :2] = np.array([
			[np.cos(yaw), -np.sin(yaw)],
			[np.sin(yaw), np.cos(yaw)]
		])
		T = np.zeros((4, 4)).astype(np.float32)
		T[:, -1] = self._position.copy()

		self._extrinsic_matrix = np.matmul(rx, ry)
		self._extrinsic_matrix = np.matmul(self._extrinsic_matrix, rz)
		self._extrinsic_matrix = np.matmul(self._extrinsic_matrix, T)

	def get_image_frame_coord(self, point):
		point_vector = np.append(point, 1)
		# To camera coord
		res = np.matmul(self._extrinsic_matrix, point_vector.reshape((4, 1)))
		# To image coord
		res = np.matmul(self._intrinsic_matrix, res).flatten()
		return res