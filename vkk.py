import requests
screen_name = 'id176882241'
url = "https://api.vk.com/method/users.get?user_ids=%s" % screen_name
r = requests.get(url)
data = r.json()
last_name = data['response'][0]['last_name']
first_name = data['response'][0]['first_name']
uid = data['response'][0]['uid']
url = "https://api.vk.com/method/friends.get?user_id=%s&fields= followers_count,last_seen" % uid
r = requests.get(url)
data = r.json()
users = data['response']
#print(users)
top_count = 0
l = []
for user in users:
	if "followers_count" in user:
		followers_count = user['followers_count']
		l.append(followers_count)
print(max(l))
