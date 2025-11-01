# Loops in Python

# 1. For Loop

# Iterating through a list of cloud providers

list_of_cloud = ["AWS", "Azure", "Google Cloud", "IBM Cloud", "Oracle Cloud"]
print("Iterating through the list of cloud providers:")
for cloud in list_of_cloud:
    print(cloud)
print()

# Iterating through a range of numbers

print("Iterating through a range of numbers from 0 to 4:")
for i in range(5):
    print(i)
    print()

print("Iterating through a range of numbers from 1 to 10 with a step of 2:")
for i in range(1, 11, 2):
    print(i)
    print()

print("Iterating through a range of numbers from 10 to 1 in reverse:")
for i in range(10, 0, -1):
    print(i)
    print()

