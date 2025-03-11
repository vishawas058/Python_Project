# Get input from user
try:
    decimal = int(input("Enter a decimal number: "))
    
    # Handle zero case
    if decimal == 0:
        print("Binary representation: 0")
    else:
        # Store original number for final output
        original_num = decimal
        binary = ""
        num = abs(decimal)  # Handle negative numbers
        
        # Conversion loop
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        
        # Add negative sign if original number was negative
        if original_num < 0:
            binary = "-" + binary
            
        print(f"Binary representation of {original_num} is: {binary}")
        
except ValueError:
    print("Please enter a valid integer")