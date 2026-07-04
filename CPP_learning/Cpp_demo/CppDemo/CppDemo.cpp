// CppDemo.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include "RobotState.h" //only include head file
#include <iostream>

#if _DEBUG
void Log(const char* message);
void Log(char _char);

#elif NDEBUG
#define Log(...)
#endif


int main()
{


	Log("T");
	Log('T');
	std::cout << "Hello Riku" << std::endl;
	
	std::cout << "------Start------" << std::endl;
	{
		RobotState a;
	}
	std::cout << "------End------" << std::endl << "\n";;

	std::cout << "------Start------" << std::endl;
	RobotState* b = new RobotState();
	{
		std::cout << sizeof(b) << std::endl; //当前为指针
		std::cout << sizeof(*b) << std::endl; //解指针 当前指向b
		std::cout << sizeof(&b->status) << " + " << sizeof(&b->tick) << std::endl; //当前为地址
		std::cout << sizeof(b->status) << " + " << sizeof(b->tick) << std::endl;
	}
	std::cout << "------End------" << std::endl << "\n";;

	std::cout << "------Start------" << std::endl;
	{
		RobotState d;
		RobotState& c = d;
		c.tick = 111;
		std::cout << d.tick << std::endl;
 
	}
	std::cout << "------End------" << std::endl;

	delete b;

	std::cin.get();
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
