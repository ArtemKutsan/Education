class Employee:
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.salary = salary
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_age(self):
        return self.age
    
    def get_salary(self):
        return self.salary
    
    def set_salary(self, new_salary):
        self.salary = new_salary
    
    def display_info(self):
        print(f"Employee: {self.get_full_name()}, Age: {self.get_age()}, Salary: {self.get_salary()}")

# Пример использования класса
john_doe = Employee("John", "Doe", 30, 50000)
john_doe.display_info()
