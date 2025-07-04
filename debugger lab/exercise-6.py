"""Exercise 6: Using Objects

This exercise teaches you how to:
- Debug object-oriented code and examine object properties
- Navigate through object instances in the Variables panel
- Understand how object methods work during debugging
- See how object state changes during method execution

Key Learning Points:
- Objects appear in the Variables panel with expandable properties
- You can examine object attributes like name and age
- Method calls can be stepped through just like regular functions
- Object state persists across method calls
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        # When debugging, you'll see 'self' with name and age properties
        # These properties will be visible in the Variables panel

    def introduce_self(self):
        print(f"I am {self.name} and I am {self.age} years old")
        # Set a breakpoint here to see:
        # - The 'self' object with its name and age
        # - How the f-string is constructed

    def compare_to(self, other_person):
        # Set a breakpoint here to examine both objects:
        # - 'self' (the current person)
        # - 'other_person' (the person being compared to)
        
        if self.age > other_person.age:
            print(f'I am {self.age - other_person.age} years older than '
            f'{person2.name}.')
        elif self.age < other_person.age:
            print(f'I am {other_person.age - self.age} years younger than '
            f'{person2.name}.')
        else:
            print(f'I am the same age as {other_person.name}.')
        # BUG: There's a bug in this method - can you find it?
        # HINT: Look at the variable names in the f-strings

if __name__ == '__main__':
    person1 = Person('Amy', 31)
    person2 = Person('Mike', 25)
    # After these lines, you'll see two Person objects in the Variables panel
    # Each will have name and age properties

    person1.introduce_self()
    person2.introduce_self()
    person1.compare_to(person2)
    person2.compare_to(person1)
    # Expected output:
    # I am Amy and I am 31 years old
    # I am Mike and I am 25 years old
    # I am 6 years older than Mike.
    # I am 6 years younger than Amy.
    #
    # Debugging tips:
    # 1. Set breakpoints in the methods to see object state
    # 2. Examine the 'self' and 'other_person' objects
    # 3. Look for the bug in the compare_to method