import requests
url = 'https://api.vk.com/method/users.get?user_ids=176882241&fields=bdate,blacklisted,status,occupation '
response = requests.get(url)
data = response.json()
#print(data)

# last_name = data["response"] [0] ['last_name']
# print(last_name)
# print(first_name)
url = 'https://api.vk.com/method/wall.get?owner_id=%d' % uid
print(url)
response = requests.get(url)
data = response.json()
#print(data)
post_cout = data["response"][0]
posts = data["response"][1:]
print(post_cout)
for post in posts:
	text = post['likes'] 
	print(text)
