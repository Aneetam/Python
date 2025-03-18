words=input().split(" ")
K=int(input())
filtered_words=[]
for word in words:
    if len(word)!=K:
        filtered_words.append(word)
print(" ".join(filtered_words))