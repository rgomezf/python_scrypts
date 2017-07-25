prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print (key)
    print ("price: %s" % prices[key])
    print ("stock: %s" % stock[key])
    
total = 0
for key in prices:
    print ("price x stock: %s" % (prices[key] * stock[key]))
    total += (prices[key] * stock[key])

print ("Total: %s" % total)

# Bill calculation
def compute_bill(food): 
    total = 0
    for item in food:
        total = total + item 
    return total

# List exercise

n = [3, 5, 7]

for i in range(0, len(n)):
    print(n[i])

def print_list(x):
    for y in range(0, len(x)):
        print (x[y])

print_list(n)
