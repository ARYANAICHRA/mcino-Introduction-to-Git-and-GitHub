# This script calculates yearly compound interest given principal, annual rate of interest and time period in years.
# Do not use this in production. Sample purpose only.

# Author: Upkar Lidder (IBM)

# Input:
# p, principal amount
# t, time period in years
# r, annual rate of interest

# Output:
# compound interest = p * (1 + r/100)^t


def compound_amount(p, t, r):
    """Return the compound amount after t years: A = p * (1 + r/100)^t"""
    return p * (pow((1 + r / 100), t))


def compound_interest(p, t, r):
    """Return the compound interest earned (amount - principal)."""
    return compound_amount(p, t, r) - p


if __name__ == "__main__":
    p = float(input("Enter the principal amount: "))
    t = float(input("Enter the time period: "))
    r = float(input("Enter the rate of interest: "))

    amount = compound_amount(p, t, r)
    interest = amount - p
    print("The compound amount after {:.2f} years is: {:.2f}".format(t, amount))
    print("The compound interest earned is: {:.2f}".format(interest))
