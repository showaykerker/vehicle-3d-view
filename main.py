import numpy as np
from components.vehicle import Vehicle
from components.road import Road
from components.canvas import Canvas
from components.camera import Camera
from components.point_manager import PointManager

def main():
	point_manager = PointManager()
	camera = Camera()
	canvas = Canvas()
	road = Road()
	ego = Vehicle()
	veh1 = Vehicle(color=(128, 128, 0), position=(10.0, 12.0, 0.0))
	veh2 = Vehicle(color=(128, 255, 0), position=(7.0, -12.0, 0.0))

	point_manager.add_road(road)
	point_manager.add_vehicle(ego)
	point_manager.add_vehicle(veh1)
	point_manager.add_vehicle(veh2)

	l, c = point_manager.get_all_links()

	camera.set_pose(position=(-2., 0., 3.), rotation=(0., np.pi/24., 0.))
	links_on_camera_frame = camera.get_links_on_camera_frame(l)
	for link, color in zip(links_on_camera_frame, c):
		canvas.add_line(link[0], link[1], color, width=2)
	canvas.show()





if __name__ == '__main__':
	main()