text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
prepro_text = text.replace(',', '').replace('.', '')
wlength = [len(w) for w in prepro_text.split()]
print(wlength)
