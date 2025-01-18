# Payment Processing System (Strategy Design Pattern)

This Python project demonstrates the **Strategy Design Pattern** using a payment processing system. The code showcases how to dynamically select and switch between different payment methods (Credit Card, PayPal, Bank Transfer) while adhering to **SOLID principles**.

## **Key Concepts Used**

### **1. Abstract Base Class (ABC)**
- The `abc` module in Python is used to define abstract base classes.
- Abstract base classes allow you to define interfaces that must be implemented by concrete subclasses.

In this code, we define a `PaymentStrategy` class as an abstract base class.

#### Code Example:
```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        """Process the payment of a given amount."""
        pass
```

- **`@abstractmethod`**: Marks a method that must be implemented by all subclasses of the abstract class.
- If a subclass does not implement all abstract methods, Python will raise a `TypeError`.

### **2. Concrete Implementation**
Concrete subclasses of `PaymentStrategy` implement the `pay` method to define specific payment processing logic:

```python
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}.")

class BankTransferPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing bank transfer payment of ${amount}.")
```

### **3. Context Class**
The `PaymentContext` class uses a strategy object to delegate the payment process:

```python
class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        self._strategy.pay(amount)
```

## **How to Run the Code**
1. Clone this repository.
2. Run the script:

```bash
python main.py
```

Example output:
```
Processing credit card payment of $100.0.
Processing PayPal payment of $200.0.
Processing bank transfer payment of $300.0.
```

## **What Else Can ABC Offer?**
The `abc` module provides additional tools for working with abstract base classes:

1. **`@abstractproperty`**: Define abstract properties that subclasses must implement.
   ```python
   from abc import ABC, abstractproperty

   class Shape(ABC):
       @abstractproperty
       def area(self):
           pass
   ```

2. **isinstance and issubclass Checks**: Abstract base classes can be used for type checking.
   ```python
   isinstance(obj, ABC)
   issubclass(SomeClass, ABC)
   ```

## **Benefits of Using ABC in This Project**
- Enforces a consistent interface for all payment strategies.
- Prevents the instantiation of incomplete or improperly defined subclasses.
- Ensures that the design pattern is implemented robustly, avoiding runtime errors.

---
Feel free to modify the `PaymentStrategy` class or add new payment methods to extend the system!

