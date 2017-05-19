import vk 
session = vk.Session(access_token = 'c8933f6a6d4d2c4b775d234042d141d8be17130ec54eb709d22ada73d21e046ae240a7e4826779e9b036b')
api = vk.API(session)
l = api.friends.get()
print(l)
r = api.status.set(text = "HELLO")
print (r)
