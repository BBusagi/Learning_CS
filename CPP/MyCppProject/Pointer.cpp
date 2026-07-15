# include <iostream>

using namespace std;

void Increment(int* value)
{
	(*value)++;
}

int main()
{
	int a = 5;

	Increment(&a);

	cout << a << endl;
	cin.get();
}