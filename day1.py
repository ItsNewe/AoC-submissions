from data import day1Data
for i in day1Data:
	j=0
	found=False #Resetting the var on each iteration of the loop because multiple corrrect keys may exist

	while(j<len(day1Data) and found!=True):
		if i+ day1Data[j]==2020:
			print(f"{i}+ {day1Data[j]}: FOUND\n Key : {i*day1Data[j]}")
			found=True #Stop the loop
							
		j+=1