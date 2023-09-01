#Create functions to find complements, disjoint unions, and symmetric differences
def complement(A):
    return universal.difference(A)

def disjointUnion(A,B):
    return (A.union(B)).difference(A.intersection(B))

def symmetricDifference(A,B):
    return A.union(complement(B)).difference(A.intersection(B))


#define sets
universal = {1,2,3,4,5,6,7,8,9}
U = {1,2,3,4,5}
A = {1,2,3,4,5}
B = {4,5,6,7}
C = {5,6,7,8,9}
D = {1,3,5,7,9}
E = {2,4,6,8}
F = {1,5,9}

# print results using functions by passing sets as parameters
print("C⊕D = ", disjointUnion(C,D))
print("A\B = ", disjointUnion(A,B))
print("B\A = ", disjointUnion(B,A))
print("E⊕F = ", disjointUnion(E,F))