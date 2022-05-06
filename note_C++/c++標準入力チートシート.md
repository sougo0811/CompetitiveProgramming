# C++標準入力チートシート

* [おまじない](#おまじない)

## おまじない
```
#include <bits/stdc++.h>
using namespace std;

int main(){

}
```
## 入力

### N
```
int N;
cin >> N;
```

### N,M
```
int N, M;
cin >> N >> M;
```

### N列(縦横OK)
```
  int N;
  cin >> N;
  vector<int> vec(N);
  for (int i = 0; i < N; i++) {
    cin >> vec.at(i);
  }
```

## 出力

### 1要素出力
```
  cout << A << endl;
```

### 複数要素出力
```
ベクトル vec を1要素ごとに改行して出力
  for(auto v: vec){
    cout << v << endl;
  }

リスト vec を空白区切りで出力
  for (int i = 0; i < vec.size()-1; i ++){
    cout << vec.at(i) << " ";
  }
  cout << vec.back() << endl;
```
