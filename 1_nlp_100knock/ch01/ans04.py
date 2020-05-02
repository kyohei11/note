def select_word(i, word):
    if i in [1, 1, 5, 6, 7, 8, 9, 15, 16, 19]:
        return (word[0], i)
    else:
        return (word[:2], i)


rawtext = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
text = rawtext.replace('.', '').split()
ans = [select_word(i, word) for i, word in enumerate(text, 1)]
print(dict(ans))
