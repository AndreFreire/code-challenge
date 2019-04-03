
#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;
	cin >> n;
	int e = 1;

	if(n == 4) {
		cout << "2 4 1 3";
	} else if (n == 2 || n == 3) {
		cout << "NO SOLUTION";
	} else { 
		while (n >= e) {
			cout << e << " ";
			e += 2;
		}

		e = 2;
		while (n >= e) {
			cout << e << " ";
			e += 2;
		}
	}	
}
