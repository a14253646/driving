country = input('what is your country:')
age = input("how old are you: ")
age = int(age)
if country == 'taiwan' :
	if age >=18 :
		print('您可以考駕照')
	else:
		print('您不能考駕照')	