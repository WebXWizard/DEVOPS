# List - List is a built-in data structure in Python that is used to store multiple items in a single variable.

# Creating a List

list_of_cloud = ["AWS", "Azure", "GCP", "IBM Cloud", "Oracle Cloud", "DigitalOcean"]

print("List of Cloud Providers: ", list_of_cloud)


# Indexing and Accessing Elements

print("First Cloud Provider: ", list_of_cloud[0])  # Accessing first element
print("Third Cloud Provider: ", list_of_cloud[2])  # Accessing third element


# Insert Cloud Provider at 0th Index

list_of_cloud[0] = "New AWS"
print("After Insertion: ", list_of_cloud)


# Methods of List

# 1. Append() - Adds an element at the end of the list

list_of_cloud.append("Linode")
print("After Append: ", list_of_cloud)

# 2. Insert() - Inserts an element at the specified position

list_of_cloud.insert(2, "Alibaba Cloud")
print("After Insert: ", list_of_cloud)

# 3. Remove() - Removes the first item with the specified value

list_of_cloud.remove("IBM Cloud")
print("After Remove: ", list_of_cloud)

# 4. Pop() - Removes the element at the specified position

popped_cloud = list_of_cloud.pop(3)
print("After Pop: ", list_of_cloud)
print("Popped Cloud Provider: ", popped_cloud)

# 5. Sort() - Sorts the list in ascending order

list_of_cloud.sort()
print("After Sort: ", list_of_cloud)

# 6. Reverse() - Reverses the order of the list

list_of_cloud.reverse()
print("After Reverse: ", list_of_cloud)

# 7. Length - Returns the number of items in the list

length_of_list = len(list_of_cloud)
print("Length of List: ", length_of_list)

# 8. Slicing - Accessing a subset of the list

sliced_list = list_of_cloud[1:4]
print("Sliced List (index 1 to 3): ", sliced_list)

# 9. Iterating through a List


print("Iterating through the List:")
for cloud in list_of_cloud:
    print(cloud)


# 10. Checking Membership - Check if an item exists in the list


if "AWS" in list_of_cloud:
    print("AWS is in the list of cloud providers.")
else:
    print("AWS is not in the list of cloud providers.")


# 11. Clearing a List - Removes all items from the list

list_of_cloud.clear()
print("After Clearing the List: ", list_of_cloud)

# 12. Copying a List - Creates a copy of the list

list_of_cloud = ["AWS", "Azure", "GCP"]
copied_list = list_of_cloud.copy()
print("Copied List: ", copied_list)


# 13. Extending a List - Adds elements from another list to the end of the current list

additional_clouds = ["Vultr", "Hetzner"]
list_of_cloud.extend(additional_clouds)
print("After Extending the List: ", list_of_cloud)
print("Final List of Cloud Providers: ", list_of_cloud)

# 14. Finding Index - Returns the index of the first occurrence of a value
index_of_gcp = list_of_cloud.index("GCP")
print("Index of GCP: ", index_of_gcp)
# 15. Counting Occurrences - Returns the number of times a value appears in the list
count_of_aws = list_of_cloud.count("AWS")
print("Count of AWS in the List: ", count_of_aws)
# End of list.py
# 16. Nested Lists - Lists can contain other lists as elements
nested_list = [["AWS", "Azure"], ["GCP", "IBM Cloud"], ["Oracle Cloud", "DigitalOcean"]]
print("Nested List: ", nested_list) 
print("Accessing element from Nested List: ", nested_list[1][0])  # Accessing "GCP"
# 17. List Comprehensions - A concise way to create lists
squared_numbers = [x**2 for x in range(6)]
print("List of Squared Numbers using List Comprehension: ", squared_numbers)
# 18. Converting a String to a List - Using split() method
string_of_clouds = "AWS,Azure,GCP,IBM Cloud,Oracle Cloud,DigitalOcean"
list_from_string = string_of_clouds.split(",")
print("List from String: ", list_from_string)
# 19. Joining a List into a String - Using join() method
joined_string = ", ".join(list_from_string)
print("Joined String from List: ", joined_string)
# 20. Sorting with a Custom Key - Using sort() with a key function
list_of_cloud.sort(key=len)  # Sort by length of the cloud provider name
print("List Sorted by Length of Names: ", list_of_cloud)

# End of list.py