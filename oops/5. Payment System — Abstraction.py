# 5. Payment System — Abstraction Concept: Abstraction Create an abstract class or interface Payment. Implement CreditCardPayment, UPIPayment and CashPayment.
# Each payment type must implement pay(amount). The user should interact with the payment through the abstraction without depending on the internal payment process.
from abc import ABC,abstractmethod
class Payment:
   @abstractmethod
   def pay(self,amt):
     pass
class creditcard(payment):
  def pay(self,amt):
    print(amt,"paid using creditcard")
class upi(payment):
  def pay(self,amt):
    print(amt,"paid using UPI")
class cash(payment):
  def pay(self,amt):
    print(amt,"paid using cash")
c=creditcard()
u=upi()
ca=cash()
c.pay(10000)
u.pay(70000)
ca.pay(20000)
