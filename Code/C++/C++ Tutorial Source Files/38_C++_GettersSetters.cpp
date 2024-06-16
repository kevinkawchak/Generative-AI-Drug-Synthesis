#include <iostream>
using namespace std;

class Movie {
    public:
        string title;
        string director;
        string rating;
        Movie(string aTitle, string aDirector, string aRating){
            title = aTitle;
            director = aDirector;
            rating = aRating;
        }
};

int main()
{
    Movie avengers("The Avengers", "Joss Whedon", "PG-13");

    cout << avengers.rating << endl;
    cout << avengers.director << endl;
    cout << avengers.title << endl;

    return 0;
}
