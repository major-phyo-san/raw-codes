#include<iostream>
#include<stdlib.h>
#include<time.h>

using namespace std;

int main()
{
int firstSeed = rand()%1000;
srand(time(NULL));
int secondSeed = rand()%60;
int thirdSeed = firstSeed * secondSeed;
srand(thirdSeed);
cout<<rand()%80;
return 0;
}
