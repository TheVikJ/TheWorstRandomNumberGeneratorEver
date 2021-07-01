seed = 45389621.0

while True:
    if input("Random number? (y/n): ") == 'y':
        print(str((seed*4 + 43)%193))
        seed = (24319028*(((seed+17)**2)/27))%100000000
