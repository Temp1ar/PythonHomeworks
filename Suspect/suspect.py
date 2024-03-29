n, m = map(int, raw_input().split(" "))
suspects = [0] + [int(raw_input()) for i in xrange(n)]
counter = [0] * len(suspects)

for i in suspects:
    if i > 0:
        counter[i] += 1
    if i < 0:
        counter[abs(i)] -= 1
        m -= 1

c = sum([int(i == m) for i in counter])

for i in xrange(1, n + 1):
    ok = 0
    if suspects[i] > 0:
        ok = -1 if counter[suspects[i]] != m else int(c == 1)
    if suspects[i] < 0:
        ok = 1 if counter[abs(suspects[i])] != m else -1 * int(c == 1)
    print "Lie" if ok < 0 else "Truth" if ok > 0 else "Not defined"