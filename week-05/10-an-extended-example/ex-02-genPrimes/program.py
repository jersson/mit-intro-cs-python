def genPrimes():
    next = 2

    while True:
        if next == 2:
            yield next
            next += 1 
        else:
            tmp = True
            for i in range(2,next):
                tmp = tmp and (next % i != 0)

            if tmp:
                yield next
            next += 1

test = genPrimes()
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())
print(test.__next__())

