if __name__ == "__main__":
    n=int(input())
    dict1=dict()
    for i in range(n):
        x,y=input().split()
        dict1.update({x:y})
    while True:
        try:
            name=input()
            if(name in dict1):
                print("{0}={1}".format(name,dict1[name]))
            else:
                print("Not found")
        except: break         
