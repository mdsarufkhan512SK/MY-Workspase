#64 Python Scope
sum1 = 50
sum2 = 30 #global variable

def saruf():
    global sum1
    sum1 = 100 # Local variable
    print(sum1)

saruf()

print(sum2)
