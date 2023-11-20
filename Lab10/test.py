def calculate_progressive_tax(income):
    if income <= 150000:
        tax = 0  # Exempt from tax for income up to 150,000 Baht
    elif income <= 300000:
        tax = (income - 150000) * 0.05  # 5% tax rate for income between 150,001 and 300,000 Baht
    elif income <= 500000:
        tax = (150000 * 0.05) + ((income - 300000) * 0.10)  # 5% up to 150,000 + 10% for income between 300,001 and 500,000 Baht
    elif income <= 750000:
        tax = (150000 * 0.05) + (200000 * 0.10) + ((income - 500000) * 0.15)  # 5% up to 150,000 + 10% for income between 300,001 and 500,000 + 15% for income between 500,001 and 750,000 Baht
    elif income <= 1000000:
        tax = (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + ((income - 750000) * 0.20)  # Continue adding the tax rates for each bracket
    elif income <= 2000000:
        tax = (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + ((income - 1000000) * 0.25)
    elif income <= 4000000:
        tax = (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (1000000 * 0.25) + ((income - 2000000) * 0.30)
    else:
        tax = (150000 * 0.05) + (200000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (1000000 * 0.25) + (2000000 * 0.30) + ((income - 4000000) * 0.35)

    return tax

# Example usage
income = float(input("Enter your annual income in Baht: "))
tax_owed = calculate_progressive_tax(income)
print(f"Your tax owed: {tax_owed:.2f} Baht")
