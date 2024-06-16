#include <iostream>
using namespace std;

class AI {
    public:
        void makeArchitecture(){
            cout << "AI has a less complex architecture" << endl;
        }
        void makeParameter(){
            cout << "AI architecture has parameters" << endl;
        }
        void makeLearning(){
            cout << "AI parameters allow for learning" << endl;
        }
};

class GenAI : public AI {
    public:
        void makeArchitecture(){
            cout << "GenAI has a more complex architecture" << endl;
        }
        void makeLearning(){
            cout << "GenAI parameters allow for enhanced learning" << endl;
        }
};

int main()
{
    AI ai;
    ai.makeParameter();
    ai.makeLearning();
    ai.makeArchitecture();

    GenAI genai;
    genai.makeParameter();
    genai.makeLearning();
    genai.makeArchitecture();

    return 0;
}
