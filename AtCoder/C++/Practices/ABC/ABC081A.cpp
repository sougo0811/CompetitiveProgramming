#include <iostream>
#include <string>
using namespace std;
int main(){
  string s;
  cin >> s;
  int count = 0;
  for (int i = 0; i < s.length(); i++){
    char ch = s[i];
    if(ch == '1'){
      count += 1;
    }
  }
  std::cout << count;
  return 0;
}
