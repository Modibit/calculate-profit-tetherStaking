month=int(input("enter number of month you want calculate : "))
value=int(input("enter the value you want to stake every month : "))
yearly_profit=float(input("enter percent of profit 10%=10 : "))
yearly_profit=1+yearly_profit/100
sum=0
pay=0
for i in range(month):
    print(f"month : {i+1}")
    profit=yearly_profit
    sum+=value
    pay+=value
    if(i//12>0):
        if(i//12>1):
            for i in range(1,i//12):
                profit*=profit
                sum+=value*(profit-1)
        else:
            sum+=value*(profit-1)
        print(f"profit : {value*profit-value}")
        
    print(f"stake: {value}\nsum(last year + now) : {(value*profit)}\n")
    print(f"your money : {sum}\npaymented : {pay}\ntotal profit:{sum-pay}\n\n<<<---->>>\n")