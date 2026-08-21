# Configurable Payment Processing System
# Using Strategy Design Pattern


# Strategy Interface
class PaymentStrategy:
    def pay(self, amount):
        pass


# Concrete Strategy 1: Credit Card
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")


# Concrete Strategy 2: UPI
class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using UPI.")


# Concrete Strategy 3: PayPal
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made using PayPal.")


# Context
class PaymentProcessor:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        self.payment_strategy.pay(amount)


# Main Program
print("===== Payment Processing System =====")

amount = float(input("Enter payment amount: ₹"))

print("\nSelect Payment Method:")
print("1. Credit Card")
print("2. UPI")
print("3. PayPal")

choice = int(input("Enter your choice: "))

if choice == 1:
    strategy = CreditCardPayment()

elif choice == 2:
    strategy = UPIPayment()

elif choice == 3:
    strategy = PayPalPayment()

else:
    print("Invalid payment method.")
    exit()

# Create payment processor
processor = PaymentProcessor(strategy)

# Process payment
processor.process_payment(amount)