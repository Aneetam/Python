S=input().split()
word_count={}
for word in S:
    word_count[word]=word_count.get(word,0)+1

    
for word in sorted(word_count):
    print(f"{word}: {word_count[word]}")