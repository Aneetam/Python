try:
    A,B=map(int,input().split())
    result=A/B
    print(result)
    
except ZeroDivisionError:
    print("Denominator can't be 0")
except ValueError:
    print("Input should be an integer")