#include <iostream>
using namespace std;

int main() {
    int N, A, B;
    cin >> N >> A >> B;
    int sum;
    sum = 0;
    for (int i = 0; i <= N; ++i) {
        int val;
        val = 0;
        int j;
        j = i;
        while(j!= 0){
            val+= j% 10;
            j /= 10;
        }
        if (A <= val && val <= B) {
            sum += i;
        }
    }
    cout << sum << endl;
}
