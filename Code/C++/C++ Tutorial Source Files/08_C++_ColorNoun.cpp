#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    string color, pluralNoun, celebrity;

    cout << "enter a color: ";
    getline(cin, color);
    cout << "enter a plural noun: ";
    getline(cin, pluralNoun);
    cout << "enter a celebrity: ";
    getline(cin, celebrity);

    cout << "Roses are " << color << endl;
    cout << pluralNoun << " are blue" << endl;
    cout << "I love " << celebrity << endl;

    return 0;
}
