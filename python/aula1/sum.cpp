#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
    long n = atoi(argv[1]);

    long sum = 0;
    for (long i = 0; i < n; ++i) {
        sum += i;
    }

    cout << "The sum is: " << sum << endl;

    return 0;
}

