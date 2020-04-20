class Employee:
    __emp_count = 0 # class variable

    def __init__(self,name="",salary=0.0): # instance method
        self.__name = name  # instance variables, note that they are set to private with double "__" at the start
        self.__salary = salary
        Employee.__emp_count += 1

    def set_name(self,name):
        self.__name = name

    def get_name(self): # encapsulation of data members
        return self.__name

    def set_salary(self,salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def __str__(self):
        return "Name : " + self.__name + " Salary : " + str(self.__salary)

    def get_employee_count(): # class method
        return Employee.__emp_count