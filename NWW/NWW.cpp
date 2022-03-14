

#include <iostream>
using namespace std;
int main()
{
    int a, b, ilo,nww;


    cin >> a;
    cin >> b;

    ilo = a * b;
    while (a != b) {

        if (a < b) {
            b = b - a;
        }
        else {
            a = a - b;
        }
      

    }
    nww = ilo / a;

    cout << nww;


}

