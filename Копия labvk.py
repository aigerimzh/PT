import requests
url = 'https://api.vk.com/method/users.get?user_ids=176882241&fields=bdate,blacklisted,status,occupation, groups'
response = requests.get(url)
data = response.json()
# university_name = data['response'][0]['occupation']['name']
# print(university_name)
print (data)
# uid = data['response'][0]['uid']
# url = 'https://api.vk.com/method/wall.get?owner_id=%d' % uid
# response = requests.get(url)
# data = response.json()
# post_cout = data["response"][0]
# posts = data["response"][1:]
# print(post_cout)
# for post in posts:
# 	text = post['likes']
# 	print(text)


