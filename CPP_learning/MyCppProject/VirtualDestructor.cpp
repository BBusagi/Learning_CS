#include <iostream>

using namespace std;

class Parent 
{
public:
	Parent()	{	cout << "Create Parent!" << endl;	}
	//~Parent()	{	cout << "Destoryed Parent!" << endl;	}  //no virtual
	virtual ~Parent() { cout << "Destoryed Parent!" << endl; } //with virtual

};

class Child: public Parent
{
public:
	Child()	{	cout << "Create Child!" << endl;	}
	~Child()	{	cout << "Destoryed Child!" << endl;	}
};

int main()
{
	Parent* p = new Parent();
	delete p;
	cout << "--------------------------" << endl;

	Child* c = new Child();
	delete c;
	cout << "--------------------------" << endl;

	Parent* pc = new Child();
	delete pc;
	cout << "--------------------------" << endl;

	cin.get();
}