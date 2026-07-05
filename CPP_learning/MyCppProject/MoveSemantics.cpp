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

	String(String&& other)
	{
		printf("Moved!\n");
		m_Size = other.m_Size;
		m_Data = other.m_Data;

		other.m_Size = 0;
		other.m_Data = nullptr;
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

	std::cin.get();
}