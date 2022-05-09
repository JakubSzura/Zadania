

#include <iostream>
using namespace std;





int main()
{
    char tab[1000];
    int klucz;
    int dl;


    cout << "Podaj wyraz skladajacy sie z malych liter: ";
    cin >> tab;

    cout << "Podaj klucz z przedzialu [-26..26]: ";
    cin >> klucz;

    dl = strlen(tab);

    if (!(klucz >= -26 && klucz <= 26)) {
        return(0);
    }

    if (klucz >= 0) {
        for (int i = 0; i < dl; i++) {
            if (tab[i] + klucz <= 'z') {
                tab[i] += klucz;

            }
            else {
                tab[i] = tab[i] + klucz - 26;
            }
        }
    }
    else {
        for (int i = 0; i < dl; i++) {
            if (tab[i] + klucz >= 'a') {
                tab[i] += klucz;
            }
            else {
                tab[i] = tab[i] + klucz + 26;
            }
        }
    }

    cout << tab;


}
