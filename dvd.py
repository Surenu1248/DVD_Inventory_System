import sys,time 

def add():
    print("\033[92m ###### You have selected Adding function ######\033[0m")
    tit=input("--> Enter the Title Name:  ") 
    star=input("--> Enter the Star Name: ") 
    yor=int(input("--> Enter the Year of Release: "))
    gen1="""\033[93m ---Please select the Genre of the DVD--- 
            1) Drama
            2) Comedy
            3) Action Thriller
            4) Horror
            5) Romantic \033[0m"""
    for i in gen1:
        print(i,end="")
        sys.stdout.flush()
        time.sleep(.009)
    print("\n") 
    
    gen=int(input("--> Enter the option number--> "))
    while gen>5:
        print("You have selected Invalid Option So, Enter again-->")
        
        for i in gen1:
            print(i,end="")
            sys.stdout.flush()
            time.sleep(.009)
        print("\n") 
        gen=int(input("--> Enter the option number: "))

    s1={
        1: "Drama",
        2: "Comedy",
        3: "Action Thriller",
        4: "Horror",
        5: "Romantic"
    }
        
    str1="\033[92m-------- You have Successfully added the DVD Information --------\033[0m"
    for i in str1:
        print(i,end="")
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")
    print(" Title:","\033[1m \033[92m",tit,"\033[0m")
    print(" Star Name:","\033[1m \033[92m",star,"\033[0m")
    print(" Year Of Release:","\033[1m \033[92m",yor,"\033[0m")
    print(" Genre:","\033[1m \033[92m",s1.get(gen),"\033[0m")
    print("\n")
    main()
    return ''

def search(): 
    print("\033[92m ######  You have selected Searching function ######\033[0m")
    
    return ''
    
def modify():
    print("You have selected Modifying function")
    return ''
    
def delete():
    print("You have selected Delete function")
    return ''
    
def exit():
    print("\033[91m -------- You have selected Exit function -------- \033[0m ")
    sys.exit(1)
    return ''
    

def main():
    x="""\033[1m \033[96m -----Welcome to Smart DVD Store-----
     1) Add a DVD
     2) Search for a DVD
     3) Modify DVD
     4) Delete a DVD
     5) Exit \033[0m"""
    for i in x:
        print(i,end='')
        sys.stdout.flush()
        time.sleep(.009)
    print("\n")
    switch={
        1:add,
        2:search,
        3:modify,
        4:delete,
        5:exit
    }
    y=int(input("Enter your Option Number --> "))
    print(switch.get(y, lambda:" Invalid Option ")())

main()

