def sort_work_in_sentences(sentences):
   words = sentences.split()
   print(words)
   words.sort(key=str.lower)
   print(words)
   sorted_sentences = ' '.join(words)
   return sorted_sentences

sentence = "This is a man world"
sorted_sentence = sort_work_in_sentences(sentence)
print(sorted_sentence)

