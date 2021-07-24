#include <bits/stdc++.h>
#include <iostream>
#include <cmath>
#include <map>
using namespace std;

#define ll long long int

#define FOR(i, a, b) for (long long int i = a; i < b; i++)

int main()
{

    int t;
    cin >> t;

    while (t--)
    {
        ll n;
        cin >> n;
        if (n % 3 == 1)
        {
            cout << (n / 3) + 1 << " " << n / 3;
        }
        else if (n % 3 == 2)
        {
            cout << n / 3 << " " << (n / 3) + 1;
        }
        else
        {
            cout << n / 3 << " " << n / 3;
        }
        cout << endl;
    }

    return 0;
}