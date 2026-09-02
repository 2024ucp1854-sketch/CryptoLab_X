#include <iostream>
#include <fstream>
#include <string>

using namespace std;
// changes made by me
// Function declarations

string encrypt_text(const string& plaintext, const string& key);

string read_file(const string& filename);

void write_file(const string& filename,
                const string& text);

void frequency_analysis(const string& ciphertext);

void word_frequency_analysis(const string& ciphertext);

void pattern_analysis(const string& ciphertext);


// Required function
string apply_substitution(
    const string& ciphertext,
    const char mapping[26]
) {

    string result = "";

    for (int i = 0; i < (int)ciphertext.length(); i++) {

        char ch = ciphertext[i];

        if (ch >= 'A' && ch <= 'Z') {

            if (mapping[ch - 'A'] != '?')
                result += mapping[ch - 'A'];
            else
                result += '_';

        }
        else if (ch >= 'a' && ch <= 'z') {

            int index = ch - 'a';

            if (mapping[index] != '?')
                result += mapping[index];
            else
                result += '_';

        }
        else {

            result += ch;
        }
    }

    return result;
}
// Required function
void display_partial_plaintext(
    const string& ciphertext,
    const char mapping[26]
) {

    string partial =
        apply_substitution(ciphertext, mapping);

    cout << "\n========== PARTIAL PLAINTEXT ==========\n";

    cout << partial << endl;
}
// Required function
bool verify_solution(
    const string& plaintext,
    const string& ciphertext,
    const char mapping[26]
) {

    string key = "";

    for (int i = 0; i < 26; i++) {

        if (mapping[i] == '?')
            return false;

        key += mapping[i];
    }

    string regenerated =
        encrypt_text(plaintext, key);

    if (regenerated == ciphertext)
        return true;

    return false;
}
int main() {

  string plaintext_file = "data/plaintext.txt";
  string ciphertext_file = "data/ciphertext.txt";

    string plaintext =
        read_file(plaintext_file);

    if (plaintext.length() == 0) {

        cout << "Error: Plaintext file is empty.\n";

        return 0;
    }

    /*
       Example substitution key.

       Plain : ABCDEFGHIJKLMNOPQRSTUVWXYZ
       Cipher: QWERTYUIOPASDFGHJKLZXCVBNM
    */

    string key =
        "QWERTYUIOPASDFGHJKLZXCVBNM";

    cout << "\n========== MONOALPHABETIC SUBSTITUTION ==========\n";

    cout << "\nPlaintext loaded successfully.\n";

    string ciphertext =
        encrypt_text(plaintext, key);

    write_file(ciphertext_file, ciphertext);

    cout << "\nCiphertext generated successfully.\n";

    cout << "\nCiphertext saved to:\n";
    cout << ciphertext_file << endl;

    // Frequency analysis
    frequency_analysis(ciphertext);

    // Word analysis
    word_frequency_analysis(ciphertext);

    // Pattern analysis
    pattern_analysis(ciphertext);

    /*
       Initial cryptanalysis mapping.

       '?' means unknown.
    */

    char mapping[26];

    for (int i = 0; i < 26; i++)
        mapping[i] = '?';

    cout << "\n========== ITERATIVE CRYPTANALYSIS ==========\n";

    cout << "\nCurrent mapping is initially unknown.\n";

    display_partial_plaintext(ciphertext, mapping);

    return 0;
}