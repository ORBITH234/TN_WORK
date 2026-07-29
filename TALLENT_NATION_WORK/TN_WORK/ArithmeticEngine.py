# ArithmeticEngine
# Instructions

# Implement arithmetic_engine(a, b). Return a dictionary with three keys: "sum", "product", and "power". The sum is a + b, the product is a * b, and the power is a ** b.

# Python Dictionary Syntax

#     A Python dictionary is wrapped in curly braces: {}.

#     Key-value pairs are separated by a colon (:), and multiple entries are separated by commas (,):

# {"key1": value1, "key2": value2}

def arithmetic_engine(a, b):
    return {"sum": a+b, "product": a*b, "power": a**b}
