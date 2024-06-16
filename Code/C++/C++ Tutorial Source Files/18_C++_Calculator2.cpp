#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int num1, num2;
    char op;

    cout << "Enter first number: ";
    cin >> num1;
    cout << "Enter operator: ";
    cin >> op;
    cout << "Enter second number: ";
    cin >> num2;
    int result;
    if(op == '+'){
        result = num1 + num2;
    } else if(op == '-'){
        result = num1 - num2;
    } else if(op == '/'){
        result = num1 / num2;
    } else if(op == '*') {
        result = num1 * num2;
    } else {
        cout << "Invalid Operator";
    }
    cout << result;
    return 0;
}
