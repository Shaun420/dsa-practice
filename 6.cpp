#include <iostream>
#include <vector>
using namespace std;

void miniMaxSum(vector<int> arr) {
	long min = 1000000001;
	vector<int>::iterator minPos;
	long max = 0;
	vector<int>::iterator maxPos;
	for (vector<int>::iterator i = arr.begin(); i != arr.end(); i++) {
		if (*i > max) {
			max = *i;
			maxPos = i;
		}
	}
	for (vector<int>::iterator i = arr.begin(); i != arr.end(); i++) {
		if (*i < min && i != maxPos) {
			min = *i;
			minPos = i;
		}
	}
	long sumOther = 0;
	for (vector<int>::iterator i = arr.begin(); i != arr.end(); i++) {
        if (i == maxPos || i == minPos)
            continue;
        sumOther += *i;
	}
	cout << (sumOther + min) << " " << (sumOther + max);
}

int main() {
	vector<int> a {5, 5, 5, 5, 5};
	miniMaxSum(a);
	return 0;
}
