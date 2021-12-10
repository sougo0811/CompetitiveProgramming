#include <iostream>
using namespace std;
int main(){
  int N;
  cin >> N;
  int a[N];
  for(int i = 0; i < N; ++i){
    cin >> a[i];
  }
  int count;
  count = 0;
  bool flg = true;
  while(flg == true){
    for(int i = 0; i < N; i++){
      if(a[i]%2 == 0){
        a[i]/=2;
      }
      else{
        flg = false;
        break;
      }
    }
    if(flg == true){count++;}
  }
  cout << count << endl;
}