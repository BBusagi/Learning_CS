#include "RobotState.h"
#include <iostream>
#include <cstdint>

int RobotState::s_counter = 0;

RobotState::RobotState()
{
	id = s_counter++;
	std::cout << "Construct #" << id << std::endl;
}

RobotState::~RobotState()
{
	std::cout << "Destruct #" << id << std::endl;
}
//virtual ~RobotState()
//{
//	cout << "Destruct" << endl;
//}

//struct SubRobotState : RobotState()
//{
//
//};