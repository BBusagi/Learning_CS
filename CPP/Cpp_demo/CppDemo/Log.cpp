#include <iostream>

void Log(char _char)
{
	std::cout << "[Riku char Log]" << _char << std::endl;
}

void Log(const char* message)
{
	std::cout << "[Riku Log]" << message << std::endl;
}

//void Log(const std::string message)
//{
//	std::cout << message << std::endl;
//}