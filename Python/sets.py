s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s) # {1, 2, 3, 4, 5}
s.add(4) 
print(s) # {1, 2, 3, 4, 5}
s.remove(5)
print(s) # {1, 2, 3, 4}

print(f"The set has {len(s)} elements.")