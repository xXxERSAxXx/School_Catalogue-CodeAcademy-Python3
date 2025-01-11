# OOP PROJECT
class School:
    def __init__(self, name, level, numberOfStudents):
        self._name = name
        self._level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_name(self, name):
        self._name = name

    def set_level(self, level):
        self._level = level

    def set_numberOfStudents(self, numberOfStudents):
        self.numberOfStudents = numberOfStudents

    def __repr__(self):
        return f"A {self._level} school named {self._name} with {self.numberOfStudents} students"

# testing the application
a = School("EAFIT", "High", 10000)
print(a)
print(a.get_name())
print(a.get_level())
a.set_numberOfStudents(10000)
print(a.get_numberOfStudents())

# define primaryschool
class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickup_policy):
        super().__init__(name, 'primary', numberOfStudents)
        self._pickup_policy = pickup_policy

    def get_pickupPolicy(self):
        return self._pickup_policy

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + f"The pickup policy is {self._pickup_policy}"

# PrimarySchool object and verification
b = PrimarySchool("PACHIS", 300, "Pickup Allowed")
print(b.get_pickupPolicy())
print(b)

# create a HighSchool class
class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'High', numberOfStudents)
    self._sportsTeams = sportsTeams
# getter of sportsTeams
  def get_sportsTeams(self):
    return self._sportsTeams
  def __repr__(self):
    return f"A {self._level} school named{self._name} with {self.numberOfStudents} students and teams: {self._sportsTeams}"
# test Highschool
c = HighSchool("Coliseo_highschool", 300, "Handball, Flag, Football")
print(c.get_sportsTeams())
print(c)
