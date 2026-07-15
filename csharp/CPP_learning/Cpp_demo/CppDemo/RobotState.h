#pragma once
#include <cstdint>

struct RobotState
{
	uint32_t tick; //4b
	float pos_x, pos_y, pos_z; //4b*3
	float quat_x, quat_y, quat_z, quat_w; //4b*4
	float vel_x, vel_y, vel_z; //4b*3
	uint8_t status; //1b

private:
	int id; //4b
	static int s_counter;

public:
	RobotState();
	~RobotState();
};