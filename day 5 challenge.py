name = input("Enter your name: ")


l = 0

for ch in name:
    if ch != " ":
        l = l + 1


PLI = l % 3


n = int(input("Enter number of requests: "))

request = [0] * n

print("Enter the requests:")

for i in range(n):
    request[i] = int(input())


# Create lists
low_demand = [0] * n
moderate_demand = [0] * n
high_demand = [0] * n
invalid_demand = [0] * n
no_demand = [0] * n

low_i = 0
mod_i = 0
high_i = 0
invalid_i = 0
no_i = 0

valid_count = 0


for req in request:

    if req < 0:
        invalid_demand[invalid_i] = req
        invalid_i = invalid_i + 1

    elif req == 0:
        no_demand[no_i] = req
        no_i = no_i + 1
        valid_count = valid_count + 1

    elif req >= 1 and req <= 20:
        low_demand[low_i] = req
        low_i = low_i + 1
        valid_count = valid_count + 1

    elif req >= 21 and req <= 50:
        moderate_demand[mod_i] = req
        mod_i = mod_i + 1
        valid_count = valid_count + 1

    elif req > 50:
        high_demand[high_i] = req
        high_i = high_i + 1
        valid_count = valid_count + 1

final_low = [0] * n
final_mod = [0] * n
final_high = [0] * n

f_low = 0
f_mod = 0
f_high = 0

removed_count = 0


if PLI == 0:

    for i in range(mod_i):
        final_mod[f_mod] = moderate_demand[i]
        f_mod = f_mod + 1

    for i in range(high_i):
        final_high[f_high] = high_demand[i]
        f_high = f_high + 1

    removed_count = low_i


elif PLI == 1:

    for i in range(low_i):
        final_low[f_low] = low_demand[i]
        f_low = f_low + 1

    for i in range(mod_i):
        final_mod[f_mod] = moderate_demand[i]
        f_mod = f_mod + 1

    removed_count = high_i


# Rule C: Keep Only Moderate
elif PLI == 2:

    for i in range(mod_i):
        final_mod[f_mod] = moderate_demand[i]
        f_mod = f_mod + 1

    removed_count = low_i + high_i

print("Display note")

print("L value:", l)
print("PLI value:", PLI)

if PLI == 0:
    print("Applied Rule: Rule A (Remove Low Demand)")
elif PLI == 1:
    print("Applied Rule: Rule B (Remove High Demand)")
elif PLI == 2:
    print("Applied Rule: Rule C (Keep Moderate Only)")


print("\nOriginal Requests:")
for i in range(n):
    print(request[i])


print("\nLow Demand:")
for i in range(low_i):
    print(low_demand[i])

print("Moderate Demand:")
for i in range(mod_i):
    print(moderate_demand[i])

print("High Demand:")
for i in range(high_i):
    print(high_demand[i])

print("Invalid Demand:")
for i in range(invalid_i):
    print(invalid_demand[i])

print("No Demand:")
for i in range(no_i):
    print(no_demand[i])


print("\nFinal Low Demand:")
for i in range(f_low):
    print(final_low[i])

print("Final Moderate Demand:")
for i in range(f_mod):
    print(final_mod[i])

print("Final High Demand:")
for i in range(f_high):
    print(final_high[i])


print("\nTotal Valid Requests:", valid_count)
print("Removed Due to PLI:", removed_count)


