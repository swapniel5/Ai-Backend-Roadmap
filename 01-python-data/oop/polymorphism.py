"""Demonstrate polymorphism through a shared method.

Like Java interfaces, ``Speaker`` describes a common operation. Python then
uses duck typing: an object qualifies if it provides the required method.
"""

from typing import Protocol


class Speaker(Protocol):
    def speak(self) -> str:
        """Describe the method expected from a speaker."""
        ...


class Dog:
    def speak(self) -> str:
        """Return the sound made by a dog."""
        return "Woof!"


class Cat:
    def speak(self) -> str:
        """Return the sound made by a cat."""
        return "Meow!"


class Robot:
    def speak(self) -> str:
        """Return the sound made by a robot."""
        return "Beep!"


def announce_speech(thing: Speaker) -> None:
    """Call the same method regardless of the concrete object type."""
    print(thing.speak())


def main() -> None:
    """Demonstrate one operation working with different object types."""
    for thing in (Dog(), Cat(), Robot()):
        announce_speech(thing)


if __name__ == "__main__":
    main()
