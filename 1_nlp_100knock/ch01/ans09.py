import random


def word_change(word):
    if len(word) <= 4:
        return word
    else:
        start = word[0]
        end = word[-1]
        change = random.sample(word[1:-1], len(word[1:-1]))
        return ''.join([start] + change + [end])


text = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
ans = [word_change(word) for word in text.split()]
print(ans)
