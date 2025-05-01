q = 173
alpha = 19

# Alice
Xa = 8
Ya = pow(alpha, Xa, q)  # correct modular exponentiation

# Bob
Xb = 138
Yb = pow(alpha, Xb, q)  # correct modular exponentiation

# Shared keys
Ka = pow(Yb, Xa, q)
Kb = pow(Ya, Xb, q)

print(f'Xa = {Xa}')
print(f'Ya = {Ya}')
print(f'Xb = {Xb}')
print(f'Yb = {Yb}')
print(f'Ka = {Ka}')
print(f'Kb = {Kb}')


"""
OUTPUT 
Xa =
     8
Ya =
   109
K =
   135
Xb =
   138
Yb =
    71
K =
   13
"""