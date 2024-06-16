#include <iostream>
using namespace std;
/*
 cout << "Age: " << &age << endl;
 cout << "Gpa: " << &gpa << endl;
 cout << "Name: " << &name << endl;
 */

int main()
{
   int age = 19;
   double gpa = 2.7;
   string name = "Mike";

    cout << "Age: " << &age << endl;
    cout << "Gpa: " << &gpa << endl;
    cout << "Name: " << &name << endl;

    return 0;
}
