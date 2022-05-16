#include <iostream>
using namespace std;


int main()
{
	int nominaly[] = { 500, 200, 100, 50, 20, 10, 5, 2, 1 };
	int kwota = 0;
	int ile = 0;
	int i = 0;
	cout << "Podaj reszte do wyplacenia: ";
	cin >> kwota;

	while (kwota > 0){

		if (kwota > nominaly[i]) {
			ile = kwota / nominaly[i];
			kwota = kwota - (nominaly[i] * ile);
			cout << nominaly[i] << " x " << ile << endl;
		}
		i++;
	}

	

}

