# Based on demo 5 from demo_gentex_im128_randcams.hdf5, which is in PickCounterToCab

It has 204 frames(images), T dimensions, we used there as a reference the robot0_agentview_left_image

The gripper is from -1 to 1, when it closing it becomes 1, otherwise it is -1, when it is open.

abs_pos represents the grip position(scaled) of the robot in XYZ coordinates

abs_rot_6d represents the rotation that contains two vectors of dimensions of three, which the first vector is used for x̂, which represents the hand's x coordinate, while the second vector is used for ŷ, which represents the hand's y coordinate.
The ẑ is calculated as the cross product between x̂ and ŷ

abs_rot_axis_angle is used with [rx ry rz], where the angle θ₀ is calculated as the norm of these coordinates, and then the u₀ represents the coordinate sdivdded by the angle.
Rotation by angle θ₀ around u₀

Camera used is going to be robot0_agentview_left_image, with its pos/quat/fovy.

Pos represents the position of the camera, while quat is the camera rotation used as a unit quaternion (w, x, y, z), w is used for the angle.
And fovy is used for how to camera's lens angle (how wide it is)