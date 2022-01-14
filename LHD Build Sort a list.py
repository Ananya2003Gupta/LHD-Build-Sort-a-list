# Shortest Menu driven program possible :)
def asc(l):
    print("List in ascending order:",sorted(l)) #returns list in ascending order

def desc(l):
    print("List in descending order:",sorted(l)[::-1]) # returns the reverse of the ascending ordered list

def menu():
    while True:
        print("""MENU :
1.Sort list in Ascending order
2.Sort list in Descending order
3.Exit""")
        c=int(input("Enter your choice:"))
        if c==3:
            print("Thanks for running the program :)")
            break
        elif c==1 or c==2:
            l=eval(input("Enter the list in the following format(example) : [1,2,3,4,5] :"))
            if c==1:
                asc(l)
            elif c==2:
                desc(l)
        else:
            print("Wrong input :( Try again!")
            
menu()
