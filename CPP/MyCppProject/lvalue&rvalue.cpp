#include <iostream>

void SetValue(int value)
{

}
int main()
{
	int i = 10; // i = lvalue, 10 = rvalue
	SetValue(i); // call by lvalue
	SetValue(10); // call by rvalue

}

