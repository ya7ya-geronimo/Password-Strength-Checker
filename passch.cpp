#include <iostream>
#include <cctype>
#include <cmath>
#include <set>
using namespace std;

double calculateEntropy(const string& password) {
    int charset = 0;

    bool hasUpper = false, hasLower = false;
    bool hasDigit = false, hasSpecial = false;

    for (char c : password) {
        if (isupper(c)) hasUpper = true;
        else if (islower(c)) hasLower = true;
        else if (isdigit(c)) hasDigit = true;
        else hasSpecial = true;
    }

    if (hasLower) charset += 26;
    if (hasUpper) charset += 26;
    if (hasDigit) charset += 10;
    if (hasSpecial) charset += 32;

    if (charset == 0) return 0;
    return password.length() * log2(charset);
}

int main() {
    string password;
    int score = 0;
    bool hasUpper = false, hasLower = false;
    bool hasDigit = false, hasSpecial = false;

    set<string> commonPasswords = {
        "password", "123456", "qwerty", "admin",
        "welcome", "letmein", "iloveyou"
    };

    cout << "Enter password: ";
    cin >> password;

    // Common password check
    if (commonPasswords.count(password)) {
        cout << "\n? Very Weak Password\n";
        cout << "Reason: Common password detected\n";
        return 0;
    }

    // Length check
    if (password.length() >= 12)
        score += 25;
    else if (password.length() >= 8)
        score += 15;
    else
        cout << "• Use at least 8 characters\n";

    // Character checks
    for (char c : password) {
        if (isupper(c)) hasUpper = true;
        else if (islower(c)) hasLower = true;
        else if (isdigit(c)) hasDigit = true;
        else hasSpecial = true;
    }

    if (hasUpper) score += 15;
    else cout << "• Add uppercase letters\n";

    if (hasLower) score += 15;
    else cout << "• Add lowercase letters\n";

    if (hasDigit) score += 15;
    else cout << "• Add numbers\n";

    if (hasSpecial) score += 15;
    else cout << "• Add special characters\n";

    // Entropy calculation
    double entropy = calculateEntropy(password);
    if (entropy > 60) score += 15;

    if (score > 100) score = 100;

    cout << "\nScore: " << score << "/100\n";
    cout << "Entropy: " << entropy << " bits\n";

    if (score < 40)
        cout << "Strength: Weak\n";
    else if (score < 70)
        cout << "Strength: Medium\n";
    else
        cout << "Strength: Strong\n";

    return 0;
}