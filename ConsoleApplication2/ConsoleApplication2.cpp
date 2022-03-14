

#include <iostream>
using namespace std;
int main()
{
    int a, b;
    cout << "Podaj pierwszą liczbę: ";
    cin >> a;
    cout << "Podaj drugą liczbę: ";
    cin >> b;
    while (a != b) {
        if (a < b) {
            b = b - a;
        }
        else {
            a = a - b;
        }
        
    }

    cout <<"Największy wspólny dzielnik: " << a;

}

