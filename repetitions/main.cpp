using namespace std;
#include <iostream>
#include <string>
#include <sstream>

int main(){
    string s;
    cin >> s;
    int count = 1, max = 0;
    char prev = 'z';
    for(char& c : s) {
        if(c == prev) {
            count++;
        } else {
            count = 1;
            prev = c;
        } 
        if(count > max) {
            max = count;
        }
    }
    cout << max;
}
