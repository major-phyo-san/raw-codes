#include <iostream>
#include <string>

using namespace std;

class Employee 
{
private:
string name;
float salary;

public:
Employee(string name, float salary)
{
name = name;
salary = salary;
}

void set_name(string name)
{
name = name;
}

string get_name()
{
cout<<name;
return *name;
}

void set_salary(float salary)
{
cout<<salary;
salary = salary;
}

float get_salary()
{
return *salary;
}

};

int main()
{

Employee e("Julie",3839.938);
e.set_name("Julie");
e.set_salary(7362.93);
cout<<e.get_name();
cout<<e.get_salary();

}