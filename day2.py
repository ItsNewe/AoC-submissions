# First, we use the following regex to split the list: ([0-9]{1,2})[-]([0-9]{1,2})[ ]([a-z]{1})\b: \b([a-zA-Z]*)
# We get 4 tokens which are, the two first numbers which consitutute the range, the single char, then the password
# We then use the following regex to order each occurence of these 4 tokens into a usable object: [($1, $2), "$3", "$4"],
#
from data import day2Data

validPws=0

#for i in day2Data:
#	charOccurences = len([j for j, char in enumerate(i[2]) if char==i[1]])
#	if i[0][0] <= charOccurences <= i[0][1]:
#		validPws+=1

for i in day2Data:
	try:
		if i[2][i[0][0]-1]==i[1] or i[2][i[0][1]-1]==i[1]:
			validPws+=1
	except(IndexError):
		print(f"{i[2]} : Index error")

print(f"KEY: {validPws}")