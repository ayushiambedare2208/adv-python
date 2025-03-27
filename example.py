# CALCULATE SIMPLE INTEREST

def simple_interest(p: float|int, n: int, r: float|int) -> tuple:
    """ 
    p: principle amount in IND
    n: Number of years 
    r: rate of interest in percent per annum
    outputs: amount and interest
    """
    i = (p*n*r)/ 100
    a = p + i
    return a, i

# TAKE P, N, R AS INPUT FROM THE USER 
p = float(input("Enter the Principle in INR: "))
n = int(input("Enter the Number of years: "))
r = float(input("Enter the rate of interest in % p.a: "))

# CALL THE SIMPLE INTERST FUNCTION
i , a = simple_interest(p, n, r)

# PRINT THE INTEREST AND AMOUNT
print(f"Simple Interest {i:.2f} INR")
print(f"Amount: {a:.2f} INR")

