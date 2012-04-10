def sieveOfEratostenes(n):
    """sieveOfEratostenes(n): return the list of the primes < n."""
    # Code from: <dickinsm@gmail.com>, Nov 30 2006
    # http://groups.google.com/group/comp.lang.python/msg/f1f10ced88c68c2d
    if n <= 2:
        return []
    sieve = range(3, n, 2)
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]
#------------------------------------------------------------------------

n = int (raw_input("Please, input N:"))
primes = sieveOfEratostenes(n)
answer = []

i = 0
while primes[i] < n ** 0.5:
	j = i
	add = primes[i] ** 2
	while add < n:
		answer.append(add)
		j += 1
		add = primes[i] * primes[j]
	i += 1 

answer.sort()

print "Subprimes are:"
print answer

