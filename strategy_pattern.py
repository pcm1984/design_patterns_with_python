from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        """Process the payment of a given amount."""
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}.")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing bank transfer payment of ${amount}.")

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Set or change the payment strategy at runtime."""
        self._strategy = strategy

    def execute_payment(self, amount):
        """Delegate the payment to the strategy."""
        self._strategy.pay(amount)

if __name__ == "__main__":
    # Initialize payment context with a default strategy
    payment_context = PaymentContext(CreditCardPayment())

    # Process a payment using a credit card
    payment_context.execute_payment(100.0)

    # Switch to PayPal payment dynamically
    payment_context.set_strategy(PayPalPayment())
    payment_context.execute_payment(200.0)

    # Switch to bank transfer
    payment_context.set_strategy(BankTransferPayment())
    payment_context.execute_payment(300.0)

