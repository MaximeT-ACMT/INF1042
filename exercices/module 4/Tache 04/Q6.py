sentence = "The small sad computer forgot its dreams and cried in the silence."

words = sentence.split()
reversed_words = words[::-1]
result = " ".join(reversed_words)

print(result)