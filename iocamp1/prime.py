def prime_num(n):
    l1=[2]
    for i in range(3,10,2):
        l1.append(i)
    for i in l1:
         if n%i==0:
             return False
    return True

def main():
    n=eval(input("Enter the number:"))
    result=prime_num(n)
    print (result)

main()

