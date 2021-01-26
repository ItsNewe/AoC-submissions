from data import day7Data
import re

total=0
for i in day7Data:
	#matches = re.findall("(([a-z0-9]+)\s?),?", i)
	matches = re.findall("((.*[^ ][a-z0-9\s]+),?).+", i)
	print(matches)
	print(matches)
	for j in matches:
		for idx, k in enumerate(re.findall("([a-z0-9]+)", j)):
			#print(k)
			offset=4 if idx==0 else 0
			if j=="gold":
				print(f"gold match @ {idx}")
				if matches[offset]!="no": total+=int(matches[4])

print(total)
