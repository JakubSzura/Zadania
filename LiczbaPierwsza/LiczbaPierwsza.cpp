
#include <iostream>
using namespace std;

int main()
{
	int lp = 0;
	int p = 2;
	int d;
	int n;

	cout << "do której liczby:" << endl;
	cin >> n;
	bool t;
	while (lp < n) {
		t = true;
		for (d = 2; d < p ; d++) {
			
			if (p % d == 0) 
			{
				t = false;
				break;
			}
		if ( t )
		{
			cout << p << " ";
			lp++;
		}
		p++;
	}
	cout << endl;
	return 0;
}





}







