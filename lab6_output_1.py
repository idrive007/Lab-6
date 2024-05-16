#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_total_price(product_prices, discount):
    total_price = 0
    for price in product_prices:
        total_price += apply_discount(price, discount)
    return total_price

def apply_discount(price, discount):
    if discount:
        return price * 0.9  
    else:
        return price

def calculate_total_price_with_tax(product_prices, discount, tax_rate):
    total_price = calculate_total_price(product_prices, discount)
    total_price *= (1 + tax_rate)
    return total_price


# In[ ]:




