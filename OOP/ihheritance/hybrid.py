class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def role(self):
        print(self.name, "is an employee")

class Project:
    def __init__(self, proj_name):
        self.proj_name = proj_name

class TeamLead(Employee, Project):
    def __init__(self, name, proj_name):
        Employee.__init__(self, name)
        Project.__init__(self, proj_name)

    def details(self):
        print(self.name, "leads project:", self.proj_name)


lead = TeamLead("Alish", "Project")
lead.role()
lead.details()
