num_set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# Write your code here
num_set2=set(map(int,input().split()))
if num_set1.issuperset(num_set2):
    print("Superset")
if num_set1.issubset(num_set2):
    print("Subset")
if num_set1.isdisjoint(num_set2):
    print("Disjoint Set")