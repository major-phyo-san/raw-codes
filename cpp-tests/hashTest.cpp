#include <iostream>
#include <tr1/functional>
#include <string>

using namespace std;

int main()
{
    string str;
    cout<<"Input string"<<endl;
    cin>>str;
    tr1::hash<string> hash_fn;
    size_t str_hash = hash_fn(str);
    cout<<str_hash<<endl;
    return 0;
}

