#include <iostream>
using namespace std;

class Student {
    public:
        string name;
        string major;
        double gpa;
        Student(string aName, string aMajor, int aGpa){
            name = aName;
            major = aMajor;
            gpa = aGpa;
        }

        bool hasHonors(){
            if(gpa >= 2.0){
                return true;
            }
            return false;
        }
};

int main()
{
    Student student1("Jim", "Business", 2.4);
    Student student2("Pam", "Art", 3.6);

    cout << student1.hasHonors() << endl;
    cout << student2.hasHonors() << endl;

    return 0;
}




