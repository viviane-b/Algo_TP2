// Cassandre Hamel, 20210863
// Viviane Binet, 20244728
using namespace std;
#include "PrimeSequenceCalculator.h"
#include <vector>
#include <unordered_set>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// ce fichier contient les definitions des methodes de la classe PrimeSequenceCalculator
// this file contains the definitions of the methods of the PrimeSequenceCalculator class

PrimeSequenceCalculator::PrimeSequenceCalculator()
{
}
vector<int> generatePrimes(int N);
bool anagramPermutation(int a, int b);

bool anagramPermutation(int a, int b){//https://stackoverflow.com/questions/47798213/how-to-check-if-2-numbers-have-same-digits-and-length
    string sa = to_string(a);
    string sb = to_string(b);
    // Check if lengths are different
    if(sa.length()!= sb.length()){
        return false;
    }
    int arr[10] = {0}, i = a, j = b;
    for (; i && j; i /= 10, j /= 10) {
        arr[i % 10]++;
        arr[j % 10]--;
    }
    for (i = 0; i < 10; ++i) {
        if (arr[i] != 0){
            return false;
        }
    }
    return true;
}

vector<int> generatePrimes(int N){ //sieve from hw 1 but c++ version
    if(N < 2){
        return {};
    }
    long long limit = N;
    
    vector<char> sieve(limit + 1, 1);
    sieve[0] = 0;
    sieve[1] = 0;
    vector<int> primeSet; 

    for (long long i = 2; i <= limit; i++) {
        if (sieve[i]) { //if true
            primeSet.push_back(i); //insert prime
            for (long long j = i * i; j <= limit; j += i) { //i*i obvi not prime
                sieve[j] = 0;
            }
        }
    }
    
    return primeSet;
}

vector<vector<int>> PrimeSequenceCalculator::CalculatePrimeSequences(const int N)
{
    vector<int> primes = generatePrimes(N); 
    unordered_set<int> setPrimes(primes.begin(), primes.end()); //this is faster than a bin search hehehehehehheehe
    vector<vector<int>> special;

    for (long long i = 0; i < primes.size(); ++i) {
        int S0 = primes[i];
        for (long long j = i + 1; j < primes.size(); ++j) {
            int S1 = primes[j]; // next prime...
            int k = S1 - S0; //find k
            int S2 = S1 + k;

            // Check if S2 is prime
            if(setPrimes.find(S2) != setPrimes.end()){
                if (anagramPermutation(S0, S1) && anagramPermutation(S0, S2)) {
                    special.push_back({S0, S1, S2});
                }
            }
        }
    }
    return special;
}
