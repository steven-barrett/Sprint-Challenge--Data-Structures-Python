import time
from binary_search_tree import Binary_Search_Tree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

BST = Binary_Search_Tree(names_1[0])
for n in names_1:
    BST.insert(n)
for i in names_2:
    if (BST.contains(i)):
        BST.insert(i)
        BST.duplicates.append(i)


# duplicates = [item for item in names_1 if item in names_2]   # Stretch, this code finishes in 1.2 seconds

# ORIGINAL CODE
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(BST.duplicates)} duplicates:\n\n{', '.join(BST.duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

