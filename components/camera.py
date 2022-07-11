import numpy as np

class Camera:
	def __init__(self,
		fx=500, fy=50, cx=200, cy=300,
		position=(0., 0., 0.), rotation=(0., 0., 0.)):
		self._fx = fx
		self._fy = fy
		self._cx = cx
		self._cy = cy
		self.set_pose(position, rotation)

	def get_pose(self):
		return self._position, self._rotation

	def set_pose(self, position, rotation):
		self._position = np.array(position).astype(np.float32)
		self._rotation = np.array(rotation).astype(np.float32)

	def _to_camera_frame(self, points):
		# points.shape (-1, 3)
		new_points = points[:, :3] - self._position.reshape((-1, 3))
		roll, pitch, yaw = self._rotation
		rot_x = np.array([
			[1.,             0.,           0.            ],
			[0.,             np.cos(-roll), np.sin(roll)   ],
			[0.,             np.sin(-roll), np.cos(-roll)  ],
		]).astype(np.float32)
		rot_y = np.array([
			[np.cos(-pitch), 0.,           np.sin(-pitch)],
			[0.,             1.,           0.            ],
			[np.sin(pitch),  0.,           np.cos(-pitch)]
		]).astype(np.float32)
		rot_z = np.array([
			[np.cos(-yaw),   np.sin(yaw),  0.            ],
			[np.sin(-yaw),   np.cos(-yaw), 0.            ],
			[0.,             0.,           1.            ]
		]).astype(np.float32)
		new_points = np.matmul(rot_x, new_points.transpose())
		new_points = np.matmul(rot_y, new_points)
		new_points = np.matmul(rot_z, new_points)
		return new_points

	def _to_image_frame(self, points):
		# points.shape (3, -1)
		image_frame = np.zeros((points.shape[1], 2)).astype(np.float32)
		image_frame[:,1] = (-points[2,:] / points[0, :] * self._fx).reshape((-1,)) + self._cx
		image_frame[:,0] = (-points[1,:] / points[0, :] * self._fy).reshape((-1,)) + self._cy
		return image_frame

	def get_points_on_camera_frame(self, points):
		points = np.array(points)
		point_matrix = np.reshape(points, (-1, 3))

		# To camera coord
		points_on_camera_frame = self._to_camera_frame(point_matrix)
		# To image coord
		points_on_image_frame = self._to_image_frame(points_on_camera_frame)

		return points_on_image_frame

	def get_links_on_camera_frame(self, links):
		links_flatten = links.reshape((-1, 3))
		points_on_camera_frame = self.get_points_on_camera_frame(links_flatten)
		points_on_camera_frame = points_on_camera_frame.reshape((-1, 2, 2))
		return points_on_camera_frame
