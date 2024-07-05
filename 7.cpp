#include <iostream>
#include <string>
using namespace std;

string timeConversion(string s) {
	string output = "";
	int hrs = stoi(s.substr(0, 2));
	string remaining = s.substr(2, 6);
	char format = s[s.size() - 2];
	if(format == 'A' && hrs == 12) {
		hrs = 0;
	}
	if(format == 'P') {
		hrs += 12;
	}
	if(hrs >= 24) {
		hrs -= 24;
	}
	string hrs_str = to_string(hrs);
	if(hrs_str.size() == 1) {
		hrs_str = hrs_str.insert(0, "0");
	}
	output = hrs_str + remaining;
	return output;
}

int main() {
	string a = "12:45:54PM";
	cout << timeConversion(a);
	return 0;
}
