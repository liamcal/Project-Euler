val = {'2':2,'3':3,'4':4,'5':5,'6':6, '7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14}
def has_flush(cards):
	return [all(cards[i][1] == cards[0][1] for i in range(len(cards))),cards[0][1]]
def has_match(c,n,x=1):
	matches = set()
	cards = c
	for i in range(len(cards)):
		c1 = cards[i]
#		print("Checking", c1)
		cur = 1
		for c2 in cards:
#			print('against',c2)
			if c1[0] ==	c2[0] and c1 != c2:
				cur += 1
#				print("match")
		if cur == n:
			matches.add(val[c1[0]])
#			print("adding", val[c1[0]])
#	print(matches,x)
	if len(matches) == x:
		return([True,max(matches)])
	else:
		return([False,0])
def has_pair(cards):
	return has_match(cards,2)
def has_2pair(cards):
	return has_match(cards,2,2)
def has_three(cards):
	return has_match(cards,3)
def has_four(cards):
	return has_match(cards,4)	
def has_fullhouse(cards):
	t = has_three(cards)
	p = has_pair(cards)
	result = t[0] and p[0]
	if result:
		return [result, max([t[1], p[1]])]
	else:
		return[result,0]
def has_straight(cards):
	nums = sorted([val[c[0]] for c in cards])
	result = all(nums[i+1] - nums[i] == 1 for i in range(len(nums)-1)) 
	if result:
		return [result, max(nums)]
	else:
		return [result, 0]
def has_straightflush(cards):
	s = has_straight(cards)
	f = has_flush(cards)
	result = s[0] and f[0]
	if result:
		return[result, s[1] ]
	else:
		return[result,0]
def max_card(cards):
	return[True, max(val[card[0]] for card in cards)]

checkers = [ has_straightflush, has_four, has_fullhouse, has_flush, has_straight, has_three,has_2pair,has_pair,max_card]

def result(cards):
	results = [(checkers[i](cards)) for i in range(len(checkers))]
#	print ("Results are",results)
	for i in range(len(checkers)):
		if results[i][0]:
			return[i,results[i][1]]
			break

def winner(p1,p2):
	r1 = result(p1)
	r2 = result(p2)
	return r1[0] < r2[0] or ( r1[0] == r2[0] and r1[1] > r2[1]) or (r1 == r2 and max(val[card[0]] for card in p1) > max(val[card[0]] for card in p2))
#hands = (open('poker.txt', 'r').read().split('\n'))
#print(has_pair([['10','k'],['10','h'],['J','h'],['K','h'],['A','c']]))
hand = input("Enter Cards for each hand: ")
c = hand.split(' ')
p1 = []
p2 = []
for i in range(5):
        p1.append(list(c[i]))
        p2.append(list(c[-(i+1)]))
p2.reverse()
print(p1,p2)
print(result(p1),result(p2))
print(winner(p1,p2))
#print(wins)
