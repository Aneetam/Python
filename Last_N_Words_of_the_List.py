S=input().split()
N=int(input())
result=[]
last_four_words=S[-4:]
last_four_words_list=" ".join(last_four_words)
for word in last_four_words[::-1]:
    result.append(word)
print(result)