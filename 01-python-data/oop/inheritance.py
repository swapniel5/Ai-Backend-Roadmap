"""Demonstrate inheritance.

Like Java's ``extends``, Python inheritance lets child classes reuse parent
behavior and override methods when their behavior needs to differ.
"""


class Vehicle:
    def __init__(self, brand: str) -> None:
        """Initialize the field shared by all vehicle types."""
        self.brand = brand

    def move(self) -> str:
        """Return the default movement behavior."""
        return f"{self.brand} vehicle is moving."


class Car(Vehicle):
    def move(self) -> str:
        """Override the parent behavior for a car."""
        return f"{self.brand} car is driving on the road."


class Boat(Vehicle):
    def move(self) -> str:
        """Override the parent behavior for a boat."""
        return f"{self.brand} boat is sailing on the water."


def main() -> None:
    """Create child objects and call their inherited or overridden methods."""
    print(Vehicle("Generic").move())
    print(Car("Toyota").move())
    print(Boat("Yamaha").move())


if __name__ == "__main__":
    main()
