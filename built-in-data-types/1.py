# Program to find sum of real imaginary part of two complete number
 


c1 = complex(input("Enter first complex number: "))
c2 = complex(input("Enter second complex number: "))

# Sum of real parts
real_sum = c1.real + c2.real

# Sum of imaginary parts
imag_sum = c1.imag + c2.imag

# Display result
print("Sum of real parts:", real_sum)
print("Sum of imaginary parts:", imag_sum)
