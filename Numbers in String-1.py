S=input()
digits=[int(char)for char in S if char.isdigit()]
total_sum=sum(digits)
average=round(total_sum/len(digits),2)
print(total_sum)
print(average)