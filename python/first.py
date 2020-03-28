#는 한줄 주
#a_list = []
#a_list.append(5)
#a_list.append('hi')
#print(a_list)
#a_list.append([2, 3])
#print(a_list)
#print(a_list[0])

a_dict = {}
peter = {'name' : '완수', 'height' : '183cm'}
print(peter['name'])
peter['weight']= 66
print(peter['height'])

'''주석 def가 함수'''
def f(x) :
    return 4 * x -2
print(f(5))

def sum_all(a,b,c):
	return a+b+c

def mul(a,b):
	return a*b

result = sum_all(1,2,3) + mul(10,10)

print(result)

def minus(a,b):
	return a-b

result2 = minus(mul(10,10),sum_all(1,2,3))

print(result2)

def oddeven(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(oddeven(5))

def checkbob(name):
    if name == 'bob':
        return True
    else:
        return False

print(checkbob('bob'))

a = 'spartacodingclub@gmail.com'
def check_mail(s):
    return s.find('@') > -1
print(check_mail(a))

a = 'spartacodingclub@gmail.com'
def get_mail(s):
    if s.find('@') > -1 :
        return s.split('@')[1].split('.')[0]
print(get_mail(a))


