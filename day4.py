from data import day4Data
import re 

valid=0

#Part one
for i in day4Data:
	if( i.__contains__("byr")
	and i.__contains__("iyr")
	and i.__contains__("eyr")
	and i.__contains__("hgt")
	and i.__contains__("hcl")
	and i.__contains__("ecl")
	and i.__contains__("pid")):

	#Part two
		if (re.compile("[0-9]{4}").match(i['byr']) and 1920 <= int(i["byr"]) <= 2002 and
			re.compile("[0-9]{4}").match(i['iyr']) and 2010 <= int(i["iyr"]) <= 2020 and
			re.compile("[0-9]{4}").match(i['eyr']) and 2020 <= int(i["eyr"]) <= 2030 and
			re.compile("[0-9]*[a-zA-Z]{2}").match(i['hgt']) and
			re.compile("[#][0-9a-f]{6}").match(i['hcl']) and
			re.compile("[0]*[0-9]{9}").match(i['pid']) and
				(i["ecl"] == "amb" or
				i["ecl"] == "blu" or
				i["ecl"] == "brn" or
				i["ecl"] == "gry" or
				i["ecl"] == "grn" or
				i["ecl"] == "hzl" or
				i["ecl"] =="oth")):

			if( (i["hgt"][-2:]=="cm" and 150 <= int(re.compile("[0-9]*").match(i["hgt"]).group(0)) <= 193) or
				(i["hgt"][-2:]=="in" and 59 <= int(re.compile("[0-9]*").match(i["hgt"]).group(0)) <= 76)):
				valid+=1

print(f"KEY: {valid}")