#include <iostream>
using namespace std;

class Book {
    public:
        string title;
        string author;
        int pages;
        Book(string aTitle, string aAuthor, int aPages){
            title = aTitle;
            author = aAuthor;
            pages = aPages;
        }
};

int main()
{

    Book book1("Harry Potter", "JK Rowling", 500);
    Book book2("Lord of the Rings", "Tokein", 700);

    cout << book1.title << endl;
    cout << book1.author << endl;
    cout << book1.pages << endl;
    return 0;
}
