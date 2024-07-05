#include <iostream>
using namespace std;
int main() {
	double x, y, z;
	cout << "Enter three numbers: ";
	cin >> x >> y >> z;

	if (x >= y && x >= z) {
		cout << "Largest number is: " << x << endl;
	} else if (y >= x && y >= z) {
		cout << "Largest number is " << y << endl;
	} else {
		cout << "Largest number is " << z << endl;
	}
	return 0;
}