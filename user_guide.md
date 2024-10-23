# **Python Command-Line Utility for Arithmetic Operations**

This project is a simple Python utility that provides basic arithmetic functions like multiplication, addition followed by multiplication, and calculating the average of two numbers. It is designed for ease of use and can be integrated into any Python project.

## **Features**

1. **Provides basic arithmetic functions (multiplication, addition + multiplication, average).**
2. **Simple API to integrate into other Python scripts or projects.**
3. **Lightweight and efficient operations.**

## **Introduction**

The `lib.py` file contains a set of utility functions that perform various arithmetic operations. This guide explains how to use the functions provided, including `multiply`, `add_then_multiply`, and `calculate_average`.

## **Installation**

### **1. Clone the Repository:**
To use the `lib.py` module, first clone the repository that contains the file:

```bash
git clone <repository-url>
cd <repository-directory>

### **How to Use**
1. Multiplication:
Use the multiply function to multiply two numbers:

```bash
from lib import multiply
result = multiply(3, 5)
print(f"The result of multiplying 3 and 5 is: {result}")
```
Output:
```bash
The result of multiplying 3 and 5 is: 15
```
2. Add Then Multiply:
Use the add_then_multiply function to add two numbers and then multiply the result by 2:
```bash
from lib import add_then_multiply
result = add_then_multiply(4, 7)
print(f"The result of (4 + 7) * 2 is: {result}")
```
Output:
```bash
The result of (4 + 7) * 2 is: 22
```

3. Calculate Average:
Use the calculate_average function to calculate the average of two numbers:
```bash
from lib import calculate_average
result = calculate_average(10, 20)
print(f"The average of 10 and 20 is: {result}")
```
output:
```bash
The average of 10 and 20 is: 15.0
```