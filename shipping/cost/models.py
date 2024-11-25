from django.db import models

# Create your models here.
class ShippingCost(models.Model):
    weightField = models.FloatField(default=0)
    unitField = models.IntegerField(default=0)
    price = 0
    
    def calculate_price(self):
        if self.weightField > 0 and self.weightField <= 0.1: 
            # print('Shipping cost is 1$')
            self.price = 1
        elif self.weightField>0.1 and self.weightField<=5: 
            # print('shipping cost is 5$')
            self.price = 5
        elif self.weightField>5 and self.weightField <=10: 
            # print('Shipping cost is 10$')
            self.price = 10 
        elif self.weightField>10 and self.weightField <=15: 
            # print('Shipping cost is 15$')
            self.price = 15 
        elif self.weightField>15 and self.weightField <20: 
            # print('Shipping cost in 20$')
            self.price = 20
        elif self.weightField>20:
            # print("Not Supported!")
            self.price = None
        return self.price

    print(price)
    # PriceField = models.FloatField(d)