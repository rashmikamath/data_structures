def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


def main():
    n=eval(input("Enter the number:"))
    result=fact(n)
    print(result)

main()