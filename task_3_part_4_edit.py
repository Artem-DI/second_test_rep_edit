import json


#d = {}
#with open('use.json', 'w') as f:
	#json.dump(d, f)

action = input('Регистрация/Вход:\n')
action = action.lower()




if action == 'вход':
	login = input('Введите логин:\n')
	passwd = input('Введите пароль:\n')
	def login_function(login, passwd):
		with open('use.json', 'r') as f:
			data_2 = json.load(f)
			if (login, passwd) in data_2.items():
				print('Добро пожаловать')
			else:
				print('Неверный логин или пароль') 
			#if passwd != data_2.values() and login != data_2.keys():
			#	print('Неверный логин или пароль')
			#else:
			#	print('Добро пожаловать')
	login_function(login, passwd)
else:
	login = input('Придумайте логин:\n')
	passwd = input('Придумайте пароль:\n')
	def register(login, passwd):		
		with open('use.json', 'r') as f:
			data = json.load(f)
			if login in data.keys():
				print('Логин занят')
			if login not in data.keys():
				with open('use.json', 'w') as f:
					data[login] = passwd
					json.dump(data, f)

	register(login, passwd)

	


	
