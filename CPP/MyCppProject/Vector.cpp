#include <iostream>
#include <string>
#include <vector>

static int s_AllocationCount = 0;
static int s_CopyCount = 0;
static int s_MoveCount = 0;

void* operator new(size_t size)
{
	std::cout << "Allocated" << size << "bytes \n";
	s_AllocationCount++;
	return malloc(size);
}

struct Vertex
{
	float x, y, z;

	Vertex(float x, float y, float z) :x(x), y(y), z(z)
	{
	}

	Vertex(const Vertex& vertex) :x(vertex.x), y(vertex.y), z(vertex.z)
	{
		s_CopyCount++;
		std::cout << "Copied!" << std::endl;
	}

	Vertex(Vertex&& vertex) :x(vertex.x), y(vertex.y), z(vertex.z)
	{
		s_MoveCount++;
		std::cout << "Moved!" << std::endl;
	}
};

std::ostream& operator << (std::ostream& stream, const Vertex& vertex)
{
	stream << vertex.x << ", " << vertex.y << ", " << vertex.z;
	return stream;
}

void Function(const std::vector<Vertex>& vertics) //通过引用来传递目标值
{

}

int main()
{
	std::vector<Vertex> vertices;
	vertices.reserve(3); //优化2

	//vertices.push_back(Vertex(1,2,3));
	//vertices.push_back({ 10,15,150 });
	//vertices.push_back({ 20,25,250 });

	vertices.emplace_back(1,2,3); //优化1
	vertices.emplace_back(10,15,150);
	vertices.emplace_back(20,25,250);

	for (int i = 0; i < vertices.size(); i++)
		std::cout << vertices[i] << std::endl;
	std::cout << "-------------------------\n";

	for (Vertex& v : vertices)
		std::cout << v << std::endl;
	std::cout << "-------------------------\n";

	//vertices.clear();
	//vertices.erase(vertices.begin() + 1);
	//
	//for (Vertex& v : vertices)
	//	std::cout << v << std::endl;
	//std::cout << "-------------------------\n";

	std::cout << s_AllocationCount << " allocations\n";
	std::cout << s_CopyCount << " copied\n";
	std::cout << s_MoveCount << " moved\n";
	
	std::cin.get();
}