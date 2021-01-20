text = input()
dictionary_text = {}
for i in text:
    if i in dictionary_text:
        dictionary_text[i] += 1
    else:
        dictionary_text[i] = 1
dictionary_text = sorted(dictionary_text.items(), key=lambda x: x[0])
for letter, occurances in dictionary_text:
    print(f'{letter}: {occurances} time/s')
