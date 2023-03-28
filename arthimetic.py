class arthimetic:
    def add(x, y):
        # add two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("inputs should be integers or floats")
        
        return x + y
    
    def subtract(x, y):
        # subtract two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("inputs should be integers or floats")
        
        return x - y
    
    def multiply(x, y):
        # multiply two numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("inputs should be integers or floats")
        
        return x * y
    
    def divide(x, y):
        # divid two numbers
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("inputs should be integers or floats")
        
        return x / y