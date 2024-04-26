#include <iostream>
#include <iomanip>
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include <openssl/sha.h>
#include <iostream>
#include <iomanip>
using namespace std;

void calculateSHA1(const string& message) {
    unsigned char hash[SHA_DIGEST_LENGTH]; // SHA-1 produces a 160-bit (20-byte) hash value
    
    // Calculate SHA-1 hash
    SHA1(reinterpret_cast<const unsigned char*>(message.c_str()), message.length(), hash);
    
    // Print the hash value
    cout << "SHA-1 Hash of the message: ";
    for(int i = 0; i < SHA_DIGEST_LENGTH; i++) {
        cout << hex << setw(2) << setfill('0') << static_cast<int>(hash[i]);
    }
    cout << endl;
}

int main() {
    string message;
    
    // User input
    cout << "Enter the message to be hashed: ";
    getline(cin, message);
    
    // Calculate and display SHA-1 hash
    calculateSHA1(message);
    
    return 0;
}

using namespace std;

void calculateSHA1(const string& message) {
    unsigned char hash[SHA_DIGEST_LENGTH]; // SHA-1 produces a 160-bit (20-byte) hash value
    
    // Calculate SHA-1 hash
    SHA1(reinterpret_cast<const unsigned char*>(message.c_str()), message.length(), hash);
    
    // Print the hash value
    cout << "SHA-1 Hash of the message: ";
    for(int i = 0; i < SHA_DIGEST_LENGTH; i++) {
        cout << hex << setw(2) << setfill('0') << static_cast<int>(hash[i]);
    }
    cout << endl;
}

int main() {
    string message;
    
    // User input
    cout << "Enter the message to be hashed: ";
    getline(cin, message);
    
    // Calculate and display SHA-1 hash
    calculateSHA1(message);
    
    return 0;
}
