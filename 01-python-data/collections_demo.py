"""Demonstrate common Python collection types.

Python collections are built into the language, while Java uses types such as
ArrayList, HashSet, and HashMap from the collections framework.
"""

from collections import Counter


def main() -> None:
    """Create and use several common collection types."""
    # Lists are ordered and mutable.
    # Similar to Java's ArrayList, a Python list can grow dynamically.
    topics = ["Python", "SQL", "Python"]
    topics.append("Machine Learning")
    print("List:", topics)
    print("First topic:", topics[0])

    # Tuples are ordered and immutable.
    # A tuple is similar to a read-only list; Java has no direct built-in equivalent.
    coordinates = (19.0760, 72.8777)
    latitude, longitude = coordinates
    print("Tuple:", coordinates)
    print("Latitude:", latitude)
    print("Longitude:", longitude)

    # Sets store unique values.
    # Similar to Java's HashSet, a set removes duplicate values.
    unique_topics = set(topics)
    print("Set:", unique_topics)
    print("Has Python:", "Python" in unique_topics)

    # Dictionaries store key-value pairs.
    # Similar to Java's HashMap, a dictionary looks up values by key.
    learner = {
        "name": "Swapniel",
        "role": "Java Engineer",
        "learning": "AI",
    }
    learner["level"] = "beginner"
    print("Dictionary:", learner)
    print("Learner name:", learner["name"])

    # Counter is useful for counting repeated values.
    # Counter is a convenient Python counting utility; Java often uses a Map
    # and updates each value manually.
    topic_counts = Counter(topics)
    print("Topic counts:", topic_counts)
    print("Most common topic:", topic_counts.most_common(1)[0])


if __name__ == "__main__":
    main()
