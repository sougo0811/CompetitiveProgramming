#include <iostream>
using namespace std;
int main(){
  int a,b;
  cin >> a >> b;
  int c;
  c = a*b;
  string s;
  if (c%2 == 0){
    s = "Even";
  }else{
    s = "Odd";
  }
  cout << s << endl;
  return 0;

}