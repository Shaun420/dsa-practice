date1 = "01/01/2023"
date2 = "28/02/2023"

d1 = date1.split("/")
d2 = date2.split("/")
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isleapyear(year):
	return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

ans = 0
if int(d1[2]) == int(d2[2]):
	for i in range(int(d1[1]), int(d2[1]) - 1):
		if isleapyear(int(d1[2])) and i == 1:
			ans += 1
		ans += days_in_month[i]
	if int(d1[1]) == int(d2[1]):
		ans += int(d2[0]) - int(d1[0])
	else:
		ans += int(d2[0]) - 1
		ans += days_in_month[int(d1[1]) - 1] - int(d1[0])
else:
	for i in range(int(d1[1]) - 1, 11):
		if isleapyear(int(d1[2])) and i == 1:
			ans += 1
		ans += days_in_month[i]
	for j in range(int(d1[2]) + 1, int(d2[2])):
		if isleapyear(j):
			ans += 366
		else:
			ans += 365
	for i in range(0, int(d2[1]) - 1):
		ans += days_in_month[i]
	ans += int(d2[0]) - 1
	ans += days_in_month[int(d1[1]) - 1] - int(d1[0])
print("No. of days:", ans)
