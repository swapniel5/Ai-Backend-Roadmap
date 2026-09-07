"""Demonstrate abstraction with an abstract base class.

Like a Java abstract class, ``PaymentMethod`` defines a required operation
without exposing how each concrete payment method implements it.
"""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        """Require subclasses to define payment processing."""


class CreditCard(PaymentMethod):
    def pay(self, amount: float) -> str:
        """Process payment through a credit card."""
        return f"Paid {amount:.2f} using a credit card."


class Upi(PaymentMethod):
    def pay(self, amount: float) -> str:
        """Process payment through UPI."""
        return f"Paid {amount:.2f} using UPI."


def main() -> None:
    """Use different payment implementations through one abstraction."""
    payment_methods = (CreditCard(), Upi())
    for payment_method in payment_methods:
        print(payment_method.pay(499.0))


if __name__ == "__main__":
    main()
