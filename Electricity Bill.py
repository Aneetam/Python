N=int(input())
if( N >=0 and N <=50):
    sum=N * 2
    bill_amt=sum * 0.2
    total=sum + bill_amt
    print(total)
elif( N >=51 and N <= 150):
    
    sum=50* 2 + (N-50) * 3
    bill=sum * 0.2
    total=sum + bill
    
    print(total)
elif( N >=151 and N <= 250):
    first_50=50 *2
    second_100=100 * 3
    thrid_part=N-(100 +50)
    thrid_100=thrid_part*5
    sum=first_50+second_100+thrid_100
    bill=sum * 0.2
    total=sum +bill
    print(total)
elif( N>250):
    first_50=50 *2
    second_100=100 * 3
    third_100=100 * 5
    fourth_part=N-(50 +100 +100)
    fourth_100=fourth_part*8
    sum=first_50+second_100+third_100+fourth_100
    bill=sum * 0.2
    total=sum+bill
    print(total)