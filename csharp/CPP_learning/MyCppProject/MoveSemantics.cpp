#include <iostream>

class String
{ 
public:
	String() = default; //潜在问题 没有初始化成员变量

	String(const char* string)
	{
		printf("Created!\n");
		m_Size = strlen(string); //和sizeof对比 不计算\0
		m_Data = new char[m_Size];
		memcpy(m_Data, string, m_Size);
	}
	String(const String& other)
	{
		printf("Copied!\n");
		m_Size = other.m_Size;
		m_Data = new char[m_Size];
		memcpy(m_Data, other.m_Data, m_Size);
	}

	//String& operator=(const String&) // 拷贝赋值

	String(String&& other) //移动构造函数
	{
		printf("Moved!\n");
		m_Size = other.m_Size;
		m_Data = other.m_Data;

		other.m_Size = 0;
		other.m_Data = nullptr;
	}

	String& operator=(String&& other) //移动赋值操作符
	{
		printf("Moved!\n");

		if (this != &other)
		{
			delete[] m_Data; //避免内存泄露

			m_Size = other.m_Size;
			m_Data = other.m_Data;

			other.m_Size = 0;
			other.m_Data = nullptr;
		}

		return *this;
	}

	~String() 
	{
		printf("Destroyed!\n");
		delete m_Data;
	}

	void Print()
	{
		for (uint32_t i = 0; i < m_Size; i++)
			printf("%c", m_Data[i]);
		
		printf("\n");
	}
private:
	char* m_Data;
	uint32_t m_Size;

};

class Entity
{
public:
	Entity(const String& name) : m_Name(name)
	{
		printf("Entity Created!\n");
	}

	Entity(String&& name) : m_Name(std::move(name)) //(String&&)name
	{
		printf("Entity Created 2 !\n");
	}

	~Entity()
	{
		printf("Entity Destroyed!\n");
	}

	void PrintName()
	{
		m_Name.Print();
	}
private:
	String m_Name;
};

int main()
{
	Entity entity("Riku"); //目的是通过mian中输入，通过String类传递给目标Entity类
	//Entity entity((String)"Riku");
	entity.PrintName();
	std::cout << "------------------\n";


	String string = "Hello";
	std::cout << "string: "; string.Print();
	// String dest = string； //copy
	//String dest(std::move(string)); <=> String dest = (String&&)string;//参数构造
	
	std::cout << "------Start------" << std::endl;
	String dest1 = std::move(string); //调用移动函数 
	std::cout << "string: "; string.Print();
	std::cout << "dest1: "; dest1.Print();

	String dest2;
	std::cout << "------Start------" << std::endl;
	dest2 = std::move(dest1); //移动赋值操作符
	std::cout << "string: "; string.Print();
	std::cout << "dest1: "; dest1.Print();
	std::cout << "dest2: "; dest2.Print();

	std::cin.get();
}