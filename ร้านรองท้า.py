k=[]
n=0
print ("-------- W E L C O M E  T O --------")
print ("----- ^_^ J I S U N G Official ^_^ -----")
while True :
    a = input(' Shopping [s]\n basket   [b]\n exit     [e]\n')
    a = a.lower()
    if a=='s' :
        print (" NCT Dream   ลด 20% [n]\n Red Velvet  ลด 30% [r]\n exit               [e]\n")
        band = input('Enter band do you want : ')
        band = band.lower()
        if band=='n':
            print (" NCT Dream we boom [1]\n NCT Dream We go up[2]\n NCT Dream regulate[3]\n")
            gen = input ('Enter Album do you want : ')
            if gen =='1':
                k.append("NCT Dream we boom           890           178")
                print ("NCT Dream we boom price 890 Bath")
                print ("ลด 20% price 712 Bath\n")
                print ("--------Add to Basket--------")
                n+=890-(890*0.2)
            elif gen =='2':
                k.append("NCT Dream We go up          690           138")
                print ("NCT Dream We go up price 690 Bath")
                print ("ลด 20% price 552 Bath\n")
                print ("--------Add to Basket--------")
                n+=690-(690*0.2)
            elif gen=='3' :
                k.append("NCT Dream regulate          790           158")
                print ("NCT Dream regulate price 790 Bath")
                print ("ลด 20% price 632 Bath\n")
                print ("--------Add to Basket--------")
                n+=790-(790*0.2)
            else :
                print ("Please Check Again!!!\n")
        elif band =='r':
            print (" Red Velvet Summer Magic[1]\n Red Velvet RBB         [2]\n Red Velvet Rookie      [3]\n")
            gen = input ('Enter Album do you want : ')
            if gen =='1':
                k.append("Red Velvet Summer Magic     990           297")
                print ("Red Velvet Summer Magic 990 Bath")
                print ("ลด 30% price 693 Bath\n")
                print ("--------Add to Basket--------")
                n+=990-(990*0.3)
                #z+=n
            elif gen =='2':
                k.append("Red Velvet RBB              750           225")
                print ("Red Velvet RBB price 750 Bath")
                print ("ลด 30% price 525 Bath\n")
                print ("--------Add to Basket--------")
                n+=750-(750*0.3)
                #z+=n
            elif gen =='3':
                k.append("Red Velvet Rookie           890           267")
                print ("Red Velvet Rookie price 890 Bath")
                print ("ลด 30% price 623 Bath\n")
                print ("--------Add to Basket--------")
                n+=890-(890*0.3)
                #z+=n
            else :
                print ("Please Check Again!!!\n")
        elif brand =='e':
            print ("--------THANK YOU--------")
    elif a=='b':
        print("="*50)
        print ("    Brand                   Price         Discount  ")
        print("="*50)

        for list in k :
            print(list)
        print("     Price      : %d         Bath\n"%(n))
        print("--------THANK YOU--------")
        break
    elif a=='e':
        print ("--------THANK YOU--------")
        break
    else :
        print ("*****E R R O R*****")
        break
