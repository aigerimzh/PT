def count_words (text):
	text = text.lower()
	text = text.replace(",", " ")
	text = text.replace(".", " ")
	text = text.replace(":", " ")
	text = text.replace("-", " ")
	text = text.replace(";", " ")
	for n in text:
		if n.isdigit():
			text.lstrip()
		else:
			pass
	words = text.split()

	new_words = []
	for word in words:
		new_word  = ""
		if len(word) < 2:
			pass
		else:
			new_words.append(word)

	odd_words = ['и', 'в','по', 'а', 'к', 'под', 'на', 'о', 'с', 'но']
	counter = {}
	for w in new_words:
		if w in counter:
			counter[w] = counter[w] + 1
		else:
			counter[w] = 1
	for w in odd_words:
		if w in counter:
			del counter[w]
	from operator import itemgetter
	sort = sorted(counter, key=itemgetter(1), reverse=False)
	return sort

s = input()
print(count_words(s))
	
