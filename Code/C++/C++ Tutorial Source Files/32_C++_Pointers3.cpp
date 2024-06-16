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
   int *pAge = &age;
   double gpa = 2.7;
   double *pGpa = &gpa;
   string name = "Mike";
   string *pName = &name;

   cout << pAge << endl;
   cout << pGpa << endl;
   cout << pName << endl;

   return 0;
}
