// Nosecone Calculator
// Calculators and Help Menu
// v1.1 (C++)
// Written by Roman Rodriguez

#define _USE_MATH_DEFINES
#include <math.h>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <list>
using namespace std;

void haack(float length, float lng_o, float rad_o, float c) {
    cout << "0,0";
    while (true) {
        length += 0.1;
        if (length > lng_o) {
            break;
        }
        double theta = acos(1 - ((2 * length) / lng_o));
        float radius = (rad_o / sqrt(M_PI)) * (sqrt(theta - (sin(2 * theta) / 2) + (c * pow(sin(theta), 3))));
        cout << fixed << setprecision(3);
        cout << length << "," << radius << endl;
    }
}

void calculate(string shape, float rad_o, float lng_o, float length) {
    if (shape == "conic" || shape == "cn") {
        cout << "0,0" << endl;
        while (true) {
            length += 0.1;
            if (length > lng_o) {
                break;
            }
            float radius = ((length * rad_o) / lng_o);
            cout << fixed << setprecision(3);
            cout << length << "," << radius << endl;
        } 
    } else if (shape == "parabolic" || shape == "pb") {
        float k;
        cout << "K-value: "; cin >> k;
        cout << "0,0";
        while (true) {
            length += 0.1;
            if (length > lng_o) {
                break;
            }
            float radius = rad_o * (((2 * (length / lng_o)) - (k * (pow((length / lng_o), 2)))) / (2 - k));
            cout << fixed << setprecision(3);
            cout << length << "," << radius << endl;
        }
    } else if (shape == "haack" || shape == "hs") {
        string series_type;
        float c;
        cout << "C-value (vk, lv, tng): "; cin >> series_type;
        if (series_type == "vk") {
            c = 0;
            haack(length, lng_o, rad_o, c);
        }
        else if (series_type == "lv") {
            c = 1.0 / 3.0;
            haack(length, lng_o, rad_o, c);
        }
        else if (series_type == "tng") {
            c = 2.0 / 3.0;
            haack(length, lng_o, rad_o, c);
        } else {
            cout << "PLEASE ENTER A VALID C-VALUE.";
        }
    } else if (shape == "power" || shape == "ps") {
        float n;
        cout << "N-value: "; cin >> n;
        cout << "0,0";
        while (true) {
            length += 0.1;
            if (length > lng_o) {
                break;
            }
            float radius = rad_o * (pow(length / lng_o, n));
            cout << fixed << setprecision(3);
            cout << length << "," << radius << endl;
        }
    } else if (shape == "ellipse" || shape == "ep") {
        cout << "0,0";
        while (true) {
            length += 0.1;
            if (length > lng_o) {
                break;
            }
            float radius = rad_o * sqrt(1 - (pow(length, 2) / pow(lng_o, 2)));
            cout << fixed << setprecision(3);
            cout << length << "," << radius << endl;
        }
    } else if (shape == "ogive" || shape == "to") {
        cout << "0,0";
        float p = (pow(rad_o, 2) + pow(lng_o, 2)) / (2 * rad_o);
        while (true) {
            length += 0.1;
            if (length > lng_o) {
                break;
            }
            float radius = sqrt(pow(p, 2) - pow(length - lng_o, 2)) + rad_o - p;
            cout << fixed << setprecision(3);
            cout << length << "," << radius << endl;
        }
    } 
}

void helpmenu() {
    list<string> valid_names = {"conic", "cn", "parabolic", "pb", "haack", "hs", "power", "ps", "ellipse", "ep", "ogive", "to"};
    cout << "\nValid shape name entries:" << endl;
    for (string name : valid_names) {
        cout << name << " ";
    }
    cout << "\nEnter 'help' for help, or 'exit' to close the program." << endl;
}
