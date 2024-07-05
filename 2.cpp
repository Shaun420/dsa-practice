#include <string>
#include <iostream>

int main() {
	std::string p = "Ex";
	std::string& q = p;
	q += "ample";
	std::cout << q << "\n";
}