
using namespace std;
#include <iostream>

bool Funkcja(string wyraz1,string wyraz2){
	int dl1 = size(wyraz1);
	int dl2 = size(wyraz2);
	
	if (dl1 != dl2) {
		return false;
	}



	char licz[123] = {};

	for (int i = 0; i < dl1; i++) {
		licz[wyraz1[i]]++;
	}

	for (int i = 0; i < dl1; i++) {
		licz[wyraz2[i]]++;
	}

	for (int i = 0; i < 127; i++) {
		if (licz[i] != 0) {
			return false;
		}
	}
	return true;
}


int main()
{

	string wyraz1;
	string wyraz2;

	char licz[123];

	bool anag;

	cout << "Podaj pierwszy wyraz: ";
	cin >> wyraz1;

	cout << "Podaj drugi wyraz: ";
	cin >> wyraz2;

	
	Funkcja(wyraz1,wyraz2);

	if (Funkcja(wyraz1, wyraz2)) {
		cout << "Podane wyrazy nie sa anagramami";
	}
	else {
		cout << "Podane wyrazy sa anagramami";
	}

}