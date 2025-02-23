S = input()
if len(S) <= 1:
    result = S  # No commas needed if the string has only one or zero characters
else:
    result = ""
    for i in range(len(S) - 1):
        result += S[i] + ","
    result += S[-1]

print( result)