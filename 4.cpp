#include <iostream>
using namespace std;
int main() {
	int n;
	cout << "Enter a number:" << endl;
	cin >> n;
	(n % 2 == 0) ? (cout << n << " is even number." << endl) : (cout << n << " is odd number." << endl);

	return 0;
}