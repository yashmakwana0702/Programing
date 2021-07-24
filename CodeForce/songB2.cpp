

#include <bits/stdc++.h>
using namespace std;

#define pb push_back;
#define mp make_pair;
#define Debug(x) cout << #x " = " << (x) << endl;
#define SORT(a) sort(a.begin(), a.end())
#define SORTR(a) sort(a.rbegin(), a.rend())
#define REV(a) reverse(a.begin(), a.end())
#define mod 1000000007;
#define pi 3.141592653589793238;
#define ll long long int
#define ull unsigned long long
#define FOR(i, a, b) for (long long int i = a; i < b; i++)
#define FORI(i, a, b) for (int i = a; i >= b; i--)

typedef vector<int> VI;
typedef vector<ll> VL;
typedef pair<int, int> PI;
typedef pair<ll, ll> PL;
typedef vector<PI> VPI;
typedef vector<PL> VPL;

int main()
{

    int t;
    cin >> t;

    while (t--)
    {
        string s;
        cin >> s;
        int n = s.length();
        int a[26];
        memset(a, 0, sizeof(a));
        FOR(i, 0, n)
        a[s[i] - 'a']++;
        int cnt = 0;
        int odd = 0;
        FOR(i, 0, 26)
        {
            if (a[i] >= 2)
            {
                cnt++;
            }
            else if (a[i] == 1)
            {
                odd++;
            }
        }

        cout << cnt + (odd / 2) << "\n";
    }

    return 0;
}
