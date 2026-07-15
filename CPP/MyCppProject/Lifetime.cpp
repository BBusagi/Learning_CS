#include <iostream>

using namespace std;

class Entity
{
public:
	Entity()
	{
		cout << "Create Entity!" << endl;
	}
	
	~Entity()
	{
		cout << "Destoryed Entity!" << endl;
	}
};

int main()
{
	{
		//Entity e; // stack
		// Entity* e = new Entity(); //heap base
	}

	cin.get();
}