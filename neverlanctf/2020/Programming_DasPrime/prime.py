import math

goalIndex = 10497

def main():
    primes = []
    count = 2
    index = 0
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                continue
        if isprime:
            primes.append(count)
            print(index, primes[index])
            index += 1
            if (index > goalIndex):
                break;
        count += 1
    print(str(0) + '. prime: ' + str(primes[0]))
    print(str(9) + '. prime: ' + str(primes[9]))
    print(str(goalIndex) + '. prime: ' + str(primes[goalIndex - 1]))

if __name__ == "__main__":
    main()
