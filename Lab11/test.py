text = "Amazon"
sorted_text = ''.join(sorted(text, key=lambda x: (x.lower(), x)))
print(sorted_text)