#include <iostream>
#include <string>
#include <vector>
#include <cctype>
using namespace std;

char mat[5][5];

string cleanKey(string key) {
    string s = "";
    bool used[26] = {};

    for (char c : key) {
        c = toupper(c);
        if (c < 'A' || c > 'Z') continue;
        if (c == 'J') c = 'I';

        if (!used[c - 'A']) {
            used[c - 'A'] = true;
            s += c;
        }
    }
    return s;
}

void generate_key_matrix(string key) {
    key = cleanKey(key);
    bool used[26] = {};
    used['J' - 'A'] = true;

    string all = key;

    for (char c : key)
        used[c - 'A'] = true;

    for (char c = 'A'; c <= 'Z'; c++) {
        if (!used[c - 'A']) {
            all += c;
            used[c - 'A'] = true;
        }
    }

    int k = 0;
    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
            mat[i][j] = all[k++];
}

void display_matrix() {
    cout << "\nKey Matrix:\n\n";
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++)
            cout << mat[i][j] << " ";
        cout << endl;
    }
}

void find_position(char c, int &r, int &col) {
    if (c == 'J') c = 'I';

    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
            if (mat[i][j] == c) {
                r = i;
                col = j;
                return;
            }
}

string prepare_plaintext(string text) {
    string s = "";

    for (char c : text) {
        c = toupper(c);
        if (c >= 'A' && c <= 'Z') {
            if (c == 'J') c = 'I';
            s += c;
        }
    }

    string result = "";

    for (int i = 0; i < (int)s.length(); i++) {
        result += s[i];

        if (i + 1 < (int)s.length() && s[i] == s[i + 1]) {
            result += 'X';
        }
    }

    if (result.length() % 2 != 0)
        result += 'X';

    return result;
}

vector<string> create_digraphs(string text) {
    vector<string> pairs;

    for (int i = 0; i < (int)text.length(); i += 2)
        pairs.push_back(text.substr(i, 2));

    return pairs;
}

string playfair_encrypt(string text) {
    string result = "";

    for (int i = 0; i < (int)text.length(); i += 2) {
        char a = text[i];
        char b = text[i + 1];

        int r1, c1, r2, c2;
        find_position(a, r1, c1);
        find_position(b, r2, c2);

        if (r1 == r2) {
            result += mat[r1][(c1 + 1) % 5];
            result += mat[r2][(c2 + 1) % 5];
        }
        else if (c1 == c2) {
            result += mat[(r1 + 1) % 5][c1];
            result += mat[(r2 + 1) % 5][c2];
        }
        else {
            result += mat[r1][c2];
            result += mat[r2][c1];
        }
    }

    return result;
}

string playfair_decrypt(string text) {
    string result = "";

    for (int i = 0; i < (int)text.length(); i += 2) {
        char a = text[i];
        char b = text[i + 1];

        int r1, c1, r2, c2;
        find_position(a, r1, c1);
        find_position(b, r2, c2);

        if (r1 == r2) {
            result += mat[r1][(c1 + 4) % 5];
            result += mat[r2][(c2 + 4) % 5];
        }
        else if (c1 == c2) {
            result += mat[(r1 + 4) % 5][c1];
            result += mat[(r2 + 4) % 5][c2];
        }
        else {
            result += mat[r1][c2];
            result += mat[r2][c1];
        }
    }

    return result;
}

void digraph_frequency(string text) {
    int freq[26][26] = {};

    for (int i = 0; i + 1 < (int)text.length(); i += 2) {
        int a = text[i] - 'A';
        int b = text[i + 1] - 'A';
        freq[a][b]++;
    }

    cout << "\nDigraph Frequency:\n";

    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < 26; j++) {
            if (freq[i][j] > 0)
                cout << char('A' + i) << char('A' + j)
                     << " : " << freq[i][j] << endl;
        }
    }
}

bool verify(string plaintext, string ciphertext) {
    string encrypted = playfair_encrypt(plaintext);
    return encrypted == ciphertext;
}

int main() {
    string key, plaintext, ciphertext;

    cout << "Enter keyword: ";
    getline(cin, key);

    generate_key_matrix(key);
    display_matrix();

    cout << "\nEnter plaintext: ";
    getline(cin, plaintext);

    string prepared = prepare_plaintext(plaintext);

    cout << "\nPrepared Plaintext: " << prepared << endl;

    cout << "\nDigraphs:\n";
    vector<string> pairs = create_digraphs(prepared);

    for (string p : pairs)
        cout << p << " ";

    ciphertext = playfair_encrypt(prepared);

    cout << "\n\nCiphertext: " << ciphertext << endl;

    string decrypted = playfair_decrypt(ciphertext);

    cout << "Decrypted Text: " << decrypted << endl;

    digraph_frequency(ciphertext);

    cout << "\nVerification: ";
    if (verify(prepared, ciphertext))
        cout << "SUCCESS\n";
    else
        cout << "FAILED\n";

    return 0;
}