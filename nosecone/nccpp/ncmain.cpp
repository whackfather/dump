// Nosecone Calculator
// UI and Error Catching
// v2.1
// Written by Roman Rodriguez

#include <iostream>
#include <algorithm>
#include <string>
#include "nccalcs.hpp"
using namespace std; 

int main() {
    bool leave;
    list<string> valid_names = {"conic", "cn", "parabolic", "pb", "haack", "hs", "power", "ps", "ellipse", "ep", "ogive", "to"};
    cout << "Welcome to the Nosecone Radius Calculator." << endl;
    cout << "Enter 'help' for help, or 'exit' to close the program." << endl;
    cout << "Valid shape name entries:" << endl;
    for (string name : valid_names) {
        cout << name << " ";
    }
    while (true) {
        string shape;
        cout << "\nEnter shape name: "; cin >> shape;
        if (shape == "exit") {
            cout << "Closing program." << endl;
            exit(0);
        } else if (shape == "help") {
            helpmenu();
        } else if (find(valid_names.begin(), valid_names.end(), shape) != valid_names.end()) {
            string rad_init;
            cout << "Enter radius (INCHES ONLY): "; cin >> rad_init;
            if (rad_init == "exit") {
                cout << "Closing program." << endl;
                exit(0);
            } else if (rad_init == "help") {
                helpmenu();
                rad_init = 1;
                leave = true;
            }
            try {
                float rad_o = stof(rad_init);
            }
            catch (...) {
                cout << "PLEASE ENTER A VALID RADIUS." << endl;
                leave = true; 
            }
            if (leave) {
                leave = false;
            } else {
                float rad_o(stof(rad_init));
                float lng_o(rad_o * 10);
                float length(0);
                calculate(shape, rad_o, lng_o, length);
            }
        } else {
            cout << "PLEASE ENTER A VALID SHAPE NAME.";
        }
    }
    return 0;
}
