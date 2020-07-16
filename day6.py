if __name__ == "__main__":
    n=int(input())
    lst=list()
    for i in range(n):
        a=input()
        lst.append(a)
    for j in range(len(lst)):
        p=lst[j]
        x=p[::2]
        y=p[1::2]
        print(x,y)
        
