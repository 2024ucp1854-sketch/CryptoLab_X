#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

using namespace std;

// Encrypt plaintext using monoalphabetic substitution key
string encrypt_text(const string& plaintext, const string& key) {
    string ciphertext = "";

    for (int i = 0; i < (int)plaintext.length(); i++) {
        char ch = plaintext[i];

        if (ch >= 'A' && ch <= 'Z') {
            ciphertext += key[ch - 'A'];
        }
        else if (ch >= 'a' && ch <= 'z') {
            char upper = ch - 'a' + 'A';
            ciphertext += key[upper - 'A'];
        }
        else {
            ciphertext += ch;
        }
    }

    return ciphertext;
}

// Read complete file
string read_file(const string& filename) {
    ifstream file(filename);

    string text = "";
    string line;

    while (getline(file, line)) {
        text += line;
        text += '\n';
    }

    file.close();

    return text;
}

// Write ciphertext to file
void write_file(const string& filename, const string& text) {
    ofstream file(filename);

    file << text;

    file.close();
}
