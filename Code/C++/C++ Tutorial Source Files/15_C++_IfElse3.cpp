#include <iostream>
#include <cmath>

using namespace std;


int main()
{

    bool isMale = false;
    bool isTall = false;

    if(isMale && isTall){
        cout << "You are a tall male";
    } else if (isMale && !isTall) {
        cout << "You are a short male";
    } else if(!isMale && isTall){
    } else {
        cout << "You are not male and not tall";
    }

    return 0;
}
