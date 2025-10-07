text = '___Python;is;AWesome;___'
text = text.strip('___')
text = text.capitalize()
text = text.split(';')
print(*text)