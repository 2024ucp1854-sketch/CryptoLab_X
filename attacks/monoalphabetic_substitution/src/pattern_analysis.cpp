#include <iostream>
#include <string>

using namespace std;

// Convert a word to uppercase
string upper_word(string word) {

    for (int i = 0; i < (int)word.length(); i++) {

        if (word[i] >= 'a' && word[i] <= 'z')
            word[i] = word[i] - 'a' + 'A';
    }

    return word;
}

// Check whether character is alphabetic
bool is_letter(char ch) {

    return (ch >= 'A' && ch <= 'Z') ||
           (ch >= 'a' && ch <= 'z');
}

// Required function
void word_frequency_analysis(const string& ciphertext) {

    string words[5000];
    int word_count = 0;

    string current = "";

    for (int i = 0; i <= (int)ciphertext.length(); i++) {

        char ch;

        if (i < (int)ciphertext.length())
            ch = ciphertext[i];
        else
            ch = ' ';

        if (is_letter(ch)) {

            if (ch >= 'a' && ch <= 'z')
                ch = ch - 'a' + 'A';

            current += ch;

        }
        else {

            if (current.length() > 0) {

                words[word_count] = current;
                word_count++;

                current = "";
            }
        }
    }

    cout << "\n========== WORD FREQUENCY ANALYSIS ==========\n";

    cout << "\nOne-letter words:\n";

    for (int i = 0; i < word_count; i++) {

        if (words[i].length() == 1)
            cout << words[i] << " ";
    }

    cout << "\n\nTwo-letter words:\n";

    for (int i = 0; i < word_count; i++) {

        if (words[i].length() == 2)
            cout << words[i] << " ";
    }

    cout << "\n\nThree-letter words:\n";

    for (int i = 0; i < word_count; i++) {

        if (words[i].length() == 3)
            cout << words[i] << " ";
    }

    cout << "\n\nRepeated words:\n";

    for (int i = 0; i < word_count; i++) {

        bool already_printed = false;

        for (int k = 0; k < i; k++) {

            if (words[k] == words[i]) {
                already_printed = true;
                break;
            }
        }

        if (already_printed)
            continue;

        int occurrences = 0;

        for (int j = 0; j < word_count; j++) {

            if (words[i] == words[j])
                occurrences++;
        }

        if (occurrences > 1) {

            cout << words[i]
                 << " -> "
                 << occurrences
                 << " times\n";
        }
    }
}

// Generate pattern such as ABBA, ABC, ABA etc.
string get_pattern(string word) {

    int mapping[26];

    for (int i = 0; i < 26; i++)
        mapping[i] = -1;

    int next_number = 0;

    string pattern = "";

    for (int i = 0; i < (int)word.length(); i++) {

        int index = word[i] - 'A';

        if (mapping[index] == -1) {

            mapping[index] = next_number;
            next_number++;
        }

        pattern += char('A' + mapping[index]);
    }

    return pattern;
}

// Required function
void pattern_analysis(const string& ciphertext) {

    string words[5000];
    int word_count = 0;

    string current = "";

    for (int i = 0; i <= (int)ciphertext.length(); i++) {

        char ch;

        if (i < (int)ciphertext.length())
            ch = ciphertext[i];
        else
            ch = ' ';

        if (is_letter(ch)) {

            if (ch >= 'a' && ch <= 'z')
                ch = ch - 'a' + 'A';

            current += ch;

        }
        else {

            if (current.length() > 0) {

                words[word_count++] = current;
                current = "";
            }
        }
    }

    cout << "\n========== PATTERN ANALYSIS ==========\n";

    for (int i = 0; i < word_count; i++) {

        if (words[i].length() >= 2) {

            cout << words[i]
                 << " -> "
                 << get_pattern(words[i])
                 << endl;
        }
    }
}