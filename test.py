# script2.py
with open('login_hold.txt', 'r') as f:
    value1 = f.readline().strip()
    value2 = f.readline().strip()

print(len(value1))
print(len(value2))
