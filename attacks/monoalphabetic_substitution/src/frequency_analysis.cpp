#include <iostream>
#include <string>

using namespace std;

struct LetterFrequency {
    char letter;
    int count;
    double percentage;
};

// Sort frequency manually in descending order
void sort_frequency(LetterFrequency freq[], int n) {

    for (int i = 0; i < n - 1; i++) {

        for (int j = i + 1; j < n; j++) {

            if (freq[j].count > freq[i].count) {

                LetterFrequency temp = freq[i];
                freq[i] = freq[j];
                freq[j] = temp;
            }
        }
    }
}

// Required function
void frequency_analysis(const string& ciphertext) {

    int count[26];

    for (int i = 0; i < 26; i++) {
        count[i] = 0;
    }

    int total_letters = 0;

    // Count each ciphertext letter
    for (int i = 0; i < (int)ciphertext.length(); i++) {

        char ch = ciphertext[i];

        if (ch >= 'A' && ch <= 'Z') {
            count[ch - 'A']++;
            total_letters++;
        }
        else if (ch >= 'a' && ch <= 'z') {
            count[ch - 'a']++;
            total_letters++;
        }
    }

    LetterFrequency freq[26];

    for (int i = 0; i < 26; i++) {

        freq[i].letter = 'A' + i;
        freq[i].count = count[i];

        if (total_letters > 0)
            freq[i].percentage =
                (count[i] * 100.0) / total_letters;
        else
            freq[i].percentage = 0;
    }

    sort_frequency(freq, 26);

    cout << "\n========== FREQUENCY ANALYSIS ==========\n";

    cout << "Letter\tCount\tPercentage\n";

    for (int i = 0; i < 26; i++) {

        cout << freq[i].letter << "\t"
             << freq[i].count << "\t"
             << freq[i].percentage << "%\n";
    }

    cout << "\nMost frequent ciphertext letters:\n";

    for (int i = 0; i < 5; i++) {

        cout << freq[i].letter
             << " (" << freq[i].count << " occurrences)\n";
    }
}