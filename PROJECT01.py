# -*- coding: utf-8 -*-
"""
COP1047C - PROJECT I
Income Tax Calculator
Yohanny Pena
"""
gross_income = float(input("Enter Gross Income: "))
dependents = int(input("Enter the Number of Dependents: "))

income_tax = (gross_income - 10000 - dependents*(3000)) * 0.20

print(f'The income tax is ${income_tax:.1f}')