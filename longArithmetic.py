#!/bin/env python

#Long arithmetic
tests = [("12221312312", "123"), 
		 ("1000", "1"),
		 ("000000","002323"),
		 ("123""83012830912803812038"),
		 ("123456789999912321312321312", "7538495473598435732131223"),
		 ("12983102830128309128038120380128309128309128302913", 
		  "15735421735421376921531932813752174321237198"),
		 ("1137218937901287390281739127397129837129",
		  "1289666511111111112983290830293856123154")
		 ]

def ladd(s1, s2):
	longest = max([s1, s2], key=len)
	plus_one = 0
	
	answer = ""
	for i in range(0, len(longest)):
		p1 = len(s1)-i-1
		p2 = len(s2)-i-1
		p1e = (i <= len(s1)) * len(s1)-i
		p2e = (i <= len(s2)) * len(s2)-i
		part1 = int("0" + s1[p1:p1e])
		part2 = int("0" + s2[p2:p2e])
		part_sum = str(part1 + part2 + plus_one)
		plus_one = (int(part_sum) > 9)
		answer = part_sum[plus_one:len(part_sum)] + answer
	
	answer = answer.lstrip("0")
	answer = "0" if len(answer) == 0 else answer
	return answer		
	
def lrem(s1, s2):
	longest = max([s1, s2], key=len)
	
	if len(s1) < len(s2) or (len(s1) == len(s2) and s1 < s2):
		s1, s2 = s2, s1
		sign = "-"
	else:
		sign = ""
	minus_one = 0
	
	answer = ""	
	for i in range(0, len(longest)):
		p1 = len(s1)-i-1
		p2 = len(s2)-i-1
		p1e = (i <= len(s1)) * len(s1)-i
		p2e = (i <= len(s2)) * len(s2)-i
		part1 = int("0" + s1[p1:p1e])
		part2 = int("0" + s2[p2:p2e])
		if( part1 - minus_one < part2 ):
			part_sum = str(part1 + 10 - part2 - minus_one)
			minus_one = 1
		else:
			part_sum = str(part1 - part2 - minus_one)
			minus_one = 0			
		answer = str(part_sum + answer)
	
	answer = answer.lstrip("0")
	answer = "0" if len(answer) == 0 else answer
	answer = sign + str(answer)
	return answer	

print "Testing \"+\""
for test in tests:
	my_ans = ladd(test[0], test[1])
	long_oper = long(test[0])+long(test[1])
	print "Ok" if my_ans == str(long_oper) else "Error"
	
print "\nTesting \"-\""
for test in tests:
	my_ans = lrem(test[0], test[1])
	long_oper = long(test[0])-long(test[1])
	print "Ok" if my_ans == str(long_oper) else "Error"