class Person:
    def __init__(self, lastName: str, age: int, married: bool):
        self.lastName = lastName
        self.age = age
        self.married = married

    def getLastName(self) -> str:
        return self.lastName

    def getAge(self) -> int:
        return self.age

    def isMarried(self) -> bool:
        return self.married

class PersonFilter(Protocol):
    def apply(self, person: Person) -> bool:
        return self.filter(person)

class AdultFilter(PersonFilter):
    # Implement Adult filter
    def __init__(self):
        self.filter = lambda x: x.age >= 18

class SeniorFilter(PersonFilter):
    # Implement Senior filter
    def __init__(self):
        self.filter = lambda x: x.age >= 65

class MarriedFilter(PersonFilter):
    # Implement Married filter
    def __init__(self):
        self.filter = lambda x: x.married

class PeopleCounter:
    def __init__(self):
        self.filter: PersonFilter = None

    def setFilter(self, filter: PersonFilter) -> None:
        self.filter = filter

    def count(self, people: List[Person]) -> int:
        # Implement method here
        count = 0
        for p in people:
            if self.filter is None or (self.filter is not None and self.filter.apply(p)):
                count += 1
        return count
    
