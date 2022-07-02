import numpy as np
from components.vehicle import Vehicle
from components.road import Road
from components.canvas import Canvas
from components.camera import Camera

def main():
	camera = Camera()
	canvas = Canvas()
	road = Road()
	ego = Vehicle()
	veh1 = Vehicle(color=(128, 255, 0), position=(7.0, 1.0, 2.0))
	veh2 = Vehicle(color=(128, 255, 0), position=(1.0, 4.0, 2.0))

	left = road.get_left()
	canvas.add_line(left[0], left[1], road.get_color())
	right = road.get_left()
	canvas.add_line(right[0], right[1], road.get_color())
	# canvas.show()
	camera.set_pose([0., 0., 0.], [0., 0., 0.])
	camera.get_image_frame_coord([[100., 50., 0.], [10, 0, 0]])


if __name__ == '__main__':
	main()