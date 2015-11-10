
roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
rom = [roman[i] for i in sorted(roman) ] # берем ключи в переменой роман 
digits = [1,4,5,9,10,40,50,90,100,400,500,900,1000]# нужно для того чтобы идти по каждому числу
def roman_number(n):
    romans_num = []# будет добавлять наши Рисмские цифры
    for i in reversed(digits): # заводим цикл наоборот и идем самого большего числа
        while n//i:# пока введенное число делится на числа из диджитс
            romans_num.append(roman[i])
            n-=i # уменьшаем число
    return "".join(romans_num)


def number_roman(n):
    a = 0
    emp_list = []
    new_n = [i for i in n]  # трасировка строки , убираем не нужные символы 
    t = list(filter(lambda i: i in rom,new_n))#трасировка строки , убираем не нужные символы
    n = ''.join(t)
    print(n)
    for k in roman:
        if n.count(roman[k]) > 4:
            return 'Не правильно введено'
        if n.count('V') > 1:
            return 'Wrong!!!'
    for i in n:
        for j in roman:
            if i not in rom:
                return 'Wrong!!!'
            if i==roman[j]:
                emp_list.append(j)
                a+=j
    for i in range(0,len(emp_list)-1):
        if len(emp_list) == 1:
            return a
        if emp_list[i] < emp_list[i+1]:# найти в интеренете о веществе, который находится в двух состояниях.
            return 'Wrong!!!'
    if a > 3999:
        return 'Wrong!!!'
    return a
def main():
	b = str(input('Введите start, чтобы начать: '))
	while b!='3':
		print('1.Перевести из арбскую в римскую: ')
		print('1.Перевести из римской в арбскую: ')
		print('3.Выход')
		b = str(input('Введите пункт меню: '))
		if b == '1':
			a = int(input('Введите арабское число для перевода: '))
			l = roman_number(a)
			print ('Ваше рисмское число: ',l)
		elif b == '2':
			a = int(input('Введите римское число для перевода: '))
			l = number_roman(a)
			print ('Ваше арабское число',l)
	print ('Спасибо, что воспользовались переводом чисел')
		
		
	


                
