'''function'''
def calculate_donuts_cost(a, b, c, d):
    # Calculate the number of batches needed to get at least d donuts
    batches_needed = (d + c - 1) // c

    total_cost = batches_needed * (b * a)

    max_donuts = batches_needed * (b + c)

    return total_cost, max_donuts

a = int(input())
b = int(input())
c = int(input())
d = int(input())

min_cost, max_donuts = calculate_donuts_cost(a, b, c, d)

print(min_cost, max_donuts)
