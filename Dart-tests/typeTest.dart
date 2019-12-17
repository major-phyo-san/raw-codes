class Person{
String firstName;

}

void main(){
Object emp = Person();
if(emp is Person){
emp.firstName = 'Bob';
print(emp.firstName);
}
dynamic emp2 = Person();
(emp2 as Person).firstName = "Alice";
print(emp2.firstName);
}