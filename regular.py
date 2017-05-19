
import re 

p = re.compile('^\w+\.?\w+@(gmail\.com|mail\.ru|yandex\.ru|icloud\.com)$') #email
print(p.match('fdsk324@yandex.ru'))

p = re.compile('^(7|\+7|8)( |-)?\(?(70[0,1,2,5,7,8]|71[2,3,7,8]|72[1,5,6,7]|747|750|751|76[0-4]|77[1,5,6,7,8])\)?( |-)?\d\d\d( |-)?\d\d( |-)?\d\d$') #Kazakhstan mobile phone
print(p.match('8(702)218-90-78'))

p = re.compile('^(7|\+7|8)( |-)?\(?(7292|72934|72938|7122|71237|72775|72831|72772|72771|72839|72774|7282|72835|72833|72834)( |?)\d\d( |-)?\d\d( |-)?\d\d)$')  #Kazakhstan city phone
print(p.match('8(7292)315825'))


p = re.compile('^\d\d(0[0-9]|1[0-2])(0[0-9]|1[0-9]|2[0-9]|3[0-1][1-31])([1-6])\d\d\d\d\d$') #IIN

p = re.compile('^([A-Z]|[a-z])\d\d\d([A-Z]|[a-z])([A-Z]|[a-z])([A-Z]|[a-z])$') #old state vehicle number
print(p.match('H577Hhg'))

p = re.compile('^\d\d\d([A-Z]|[a-z])([A-Z]|[a-z])([A-Z]|[a-z])(0[1-9]|1[0-6])$') #new stste vehicle number 
print(p.match('856JKH14'))

