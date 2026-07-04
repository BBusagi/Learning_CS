#include <iostream>

#if _DEBUG
#define ENV 0
#elif NDEBUG
#define ENV 1
#endif

int main()
{
	std::cout << "ENV" << std::endl;
	std::cout << "文件: " << __FILE__ << " 行: " << __LINE__ << std::endl;
	std::cout << "编译于: " << __DATE__ << " " << __TIME__ << std::endl;
	std::cout << "C++ 标准: " << __cplusplus << std::endl;
	std::cout << "------------------" << std::endl;
}