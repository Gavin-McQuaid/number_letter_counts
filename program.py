words = {
	1:'one',
	2:'two',
	3:'three',
	4:'four',
	5:'five',
	6:'six',
	7:'seven',
	8:'eight',
	9:'nine',
	10:'ten',
	11:'eleven',
	12:'twelve',
	13:'thirteen',
	14:'fourteen',
	15:'fifteen',
	16:'sixteen',
	17:'seventeen',
	18:'eighteen',
	19:'nineteen',
	20:'twenty',
	30: 'thirty',
	40:'forty',
	50: 'fifty',
	60:'sixty',
	70: 'seventy',
	80:'eighty',
	90: 'ninety',
    100:'one hundred',
    200:'two hundred',
    300:'three hundred',
    400:'four hundred',
    500:'five hundred',
    600:'six hundred',
    700:'seven hundred',
    800:'eight hundred',
    900:'nine hundred',
    1000:'one thousand',
}
total = 0 
i = 1
while i <= 1000:
	if i < 20 or i == 1000:
		number =  words[i]
	elif  i < 100:
		j = str(i)
		k = int(j[0]) * 10
		if j[1] != '0':
			m = int(j[1])
			number =  words[k] + ' ' + words[m]
		else:
			number =  words[k]
	else:
		j = str(i)
		k = int(j[0]) * 100
		m = int(j[1]) * 10
		n = int(j[2])
		if m == 0 and n == 0:
			number = words[k] 
		elif m == 10:
			m = n + m
			number =  words[k] + ' and ' + words[m]
		elif m == 0:
			number = words[k] + ' and ' + words[n]	
		elif j[2] != '0':
			
			number =  words[k] + ' and ' + words[m] + ' ' + words[n]
		else:
			number  = words[k] + ' and ' + words[m] 
	
	x = 0
	while x < len(number):
		if number[x] !=' ':
			total += 1
		x+= 1

	i += 1
	print number

print total







