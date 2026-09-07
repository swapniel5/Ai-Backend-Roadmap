"""Demonstrate encapsulation with a private attribute.

Like Java's private fields, ``__balance`` is protected from normal direct use.
Python uses properties and methods instead of Java-style getter/setter methods.
"""


class BankAccount:
    def __init__(self, owner: str, opening_balance: float = 0.0) -> None:
        """Create an account and hide its balance behind controlled operations."""
        self.owner = owner
        self.__balance = opening_balance

    def deposit(self, amount: float) -> None:
        """Add a positive amount to the account balance."""
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        """Remove money only when the amount and available balance are valid."""
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    @property
    def balance(self) -> float:
        """Expose the balance as a read-only attribute."""
        return self.__balance


def main() -> None:
    """Demonstrate safe balance changes through public methods."""
    account = BankAccount("Asha", 1_000.0)
    account.deposit(250.0)
    account.withdraw(100.0)

    print(f"{account.owner}'s balance: {account.balance:.2f}")


if __name__ == "__main__":
    main()
