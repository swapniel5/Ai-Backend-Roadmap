"""Demonstrate classes and objects.

Like Java, Python uses classes as blueprints and objects as their instances.
Python does not require a separate type declaration for each field.
"""


class Student:
    """A blueprint for student objects."""

    def __init__(self, name: str, course: str) -> None:
        """Initialize one object with its starting field values."""
        self.name = name
        self.course = course

    def introduce(self) -> str:
        """Return a message describing this student."""
        return f"{self.name} is learning {self.course}."


def main() -> None:
    """Create objects and call their instance methods."""
    first_student = Student("Asha", "Python")
    second_student = Student("Ravi", "Machine Learning")

    print(first_student.introduce())
    print(second_student.introduce())


if __name__ == "__main__":
    main()
