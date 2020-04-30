#AI:HUMAN'S SURVIVAL QUEST
import random

def space_r():
    if r==0:
        print("You have reached close to an astroid belt")
    elif r==1:
        print("You have reached near a black hole")
    elif r==2:
        print("You have reached near a nebula")
    elif r==3:
        print("You have reached close to centre of our galaxy(Quasar)")
    elif r==4:
        print("You have reached close to a worm hole")
    elif r==7:
        print("You have reached Andromeda galaxy ")
    elif r==8:
        print("You have reached near a star")
    elif r==9:
        print("You have reached near a Carbon star ")
    elif r==11:
        print("You have reached close to a Dark cloud")
    elif r==12:
        print("You have reached near a Dwarf star")
    elif r==13:
        print("You have reached near the oort cloud")
    elif r==14:
        print("You have reached near a neutron star")
    elif r==16:
        print("You have reached near a different system")
    elif r==17:
        print("You have reached close to a nearby galaxy")    
    elif r==19:
        print("You have reached near a worm hole")
    elif r==20:
        print("You have reached near a Star")
    elif r==23:
        print("You have reached near a nebula")
    elif r==25:
        print("You have reached close to an astroid field")
    elif r==26:
        print("You have reached near Triangulam Galaxy")
    elif r==28:
        print("You have reached near the Draco Dwarf ")
    elif r==29:
        print("You have reached near Leo 1")
    elif r==30 or r==27 or r==24 or r==22 or r==21 or r==18 or r==15 or r==10 or r==6 or r==5:
        print("You have reached a planet")
    
def space():
    space_r()
    print(end="")
    print("----Enter 1 to go through.")
    print("        OR")
    print("Enter 2 to Stay on the current course")
def stats():
    if air_s==100:
        airs="O.K"
    if ter_s==100:
        ters="O.K"
    if air_s<100:
        airs="NOT WORKING"
    if ter_s<=100:
        ters="O.K"
    print("--------Ship Status-------")
    print("""            Drones=""",Drones ,"""    Fuel=""",fuel ,"""    Oxygen level=""",oxygen ,"""
    	Population=""",human ,"""    SpaceShip_HP=""",SpaceShip_HP,"""    Air_senser=""",airs,"""
    	Terrain_sensor=""",ters)   

def chec():
    if fuel<=0 or SpaceShip_HP<=0 or human<=0 or oxygen<=0:
        i=2

    
print("""
	In the year of 2195, planet earth is not suitable for the survival of human beings.
	To save humanity from extinction they have to find another suitable planet.
	For this they created a spaceship which will help them to find a new home.
	
    The spaceship is operated by an AI with human beings in the sleep chamber.
    Quest I- Find a suitable Planet for the Humans.
	 """) 
Drones,fuel,SpaceShip_HP,air_s,ter_s,human,oxygen=3,100,100,100,100,100,100
inv=0


print("""The spaceship has lunched into the space.""")
i=0
me=0
Plan=0
while i < 1:

    i=0
    Plan=2
    if inv !=1 :
        r=random.randint(0,30)
        r2=random.randint(0,29)
        rc=random.randint(1,3)
        rpt=random.randint(1,11)
        rpa=random.randint(0,10)
    
    if inv==1:
        inv=0
    print()
    stats()
    print()
    space()
    u_i=str(input("Enter Your Choice :"))
    print()
    if u_i!="1" and u_i!="2":
        inv=1
        print("Invalid Input")
    if (r==30 or r==27 or r==24 or r==22 or r==21 or r==18 or r==15 or r==10 or r==6 or r==5) and u_i=="1":
        r3=random.randint(0,9)
        r4=random.randint(0,9)
        r5=random.randint(0,9)
        r6=random.randint(0,9)
        r7=random.randint(0,9)
        r8=random.randint(0,9)
        r9=random.randint(0,9)
        t1=random.randint(0,3)
        t2=random.randint(1,4)
        
        print("-------Planet Description-------")

        print("""Gravitaion=""",end="")

        if r4==0:
            print("Very High")
        elif r4==1:
            print("Medium")
        elif r4==2:
            print("Earth-like")
        elif r4==3:
            print("Extremely Low")
        elif r4==4:
            print("Massive")
        elif r4==5:
            print("Low")
        elif r4==6:
            print("High")
        elif r4==7:
            print("No gravity")
        elif r4==8:
            print("Ultra low")
        elif r4==9:
            print("Very Low")
        
        print("""Air_Quality=""",end="")

        if r5==0 and (rpt==rpa or air_s>=100):
            print("Toxic")
        elif r5==1 and (rpt==rpa or air_s>=100) :
            print("Poisonous")
        elif r5==2 and (rpt==rpa or air_s>=100) :
            print("Combatible")
        elif r5==3 and (rpt==rpa or air_s>=100) :
            print("Good")
        elif r5==4 and (rpt==rpa or air_s>=100) :
            print("Earth-like")
        elif r5==5 and (rpt==rpa or air_s>=100) :
            print("Not breathable")
        elif r5==6 and (rpt==rpa or air_s>=100) :
            print("Very bad")
        elif r5==7 and (rpt==rpa or air_s>=100) :
            print("Dangerous")
        elif r5==8 and (rpt==rpa or air_s>=100) :
            print("Breathabe")      
        elif r5==9 and (rpt==rpa or air_s>=100) : 
            print("Bad")   
        else:
            print("Unknown")
        
        print("""Size=""",end="")
        if r6==0:
            print("Tiny")
        elif r6==1:
            print("Large")
        elif r6==2:
            print("Dwarf")
        elif r6==3:
            print("Huge")
        elif r6==4:
            print("Earth-like")
        elif r6==5:
            print("Small")
        elif r6==6:
            print("Normal")
        elif r6==7:
            print("Big")
        elif r6==8:
            print("Medium")
        elif r6==9:
            print("Very Small")

        print("""Life= Unknown""")


        print("""Terrain=""",end="")
        if r8==0 and (rpa==rpt or ter_s>=100):
            print("plain")
        elif (r8==1 or r3==0) and (rpa==rpt or ter_s>=100):
            print("Mountains")
        elif r8==2 and (rpa==rpt or ter_s>=100): 
            print("Hills")
        elif (r8==3 or r3==1) and (rpa==rpt or ter_s>=100):
            print("Oceans")
        elif (r8==4 or r3==7) and (rpa==rpt or ter_s>=100): 
            print("Desert")
        elif r8==5 and (rpa==rpt or ter_s>=100): 
            print("Highly Elevated")
        elif r8==6 and (rpa==rpt or ter_s>=100):
            print("Smooth Plain") 
        elif r8==7 and (rpa==rpt or ter_s>=100):
            print("Hilly Mountains") 
        elif r8==8 and (rpa==rpt or ter_s>=100): 
            print("Water-World")
        elif r8==9 and (rpa==rpt or ter_s>=100): 
            print("Earth-Like")
        else:
            print("Unknown")

        print("""Colour=""",end="")
        if r9==0:
            print("Reddish Brown")
        elif r9==1: 
            print("Green")
        elif r9==2:
            print("Bluish Green")
        elif r9==3:
            print("Green")
        elif r9==4:
            print("Violet")
        elif r9==5:
            print("Blue")
        elif r9==6:
            print("Red")
        elif r9==7:
            print("Dark Orange")
        elif r9==8:
            print("Dark Red")
        elif r9==9:    
            print("Grey")
        print("Temperature=Unkown")
        print("Resource=Unkown")

        print("""-----------Enter 1 to Settle in this planet
    	----------OR
    	Enter 2 to continue on the same course
     ----------OR
     Enter 3 to Send a Drone""")
        Plan=str(input("Enter Your Choice :"))
        if Plan !="1" and Plan !="2" and Plan!="3":
            print("Invalid Input")
    if Plan=="1":
        i=2
    if Plan=="3":
        print()
        print("A Drone has been send.")
        print()
        print("Life=",end="")
        if r7==0:
            print("Small Man-eating Worms")
        elif r7==1:
            print("Sharp Clawed predators")
        elif r7==2:
            print("Carnivores beast")
        elif r7==3:
            print("Herbivores Animals")
        elif r7==4:
            print("Man-eanting plants")
        elif r7==5:
            print("Toxic plants")
        elif r7==6:
            print("Huge Monsters")
        elif r7==7:
            print("large Insects")
        elif r7==8:
            print("Creatures With Large Wings")
        elif r7==9:
            print("Flying animals")

        print("Temperature=",end="")

        if t1==0 and (r3==3 or r3==7):
            print("Extremely High")
        elif t1==1:
            print("Compatible")
        elif t1==2:
            print("Extremely Low")    
        elif t1==3:
            print("Normal")
        else:
            print("Not suitable")

        print("Resources=",end="")
        if t2==1:
            print("None")
        if t2==2:
            print("Low")
        if t2==3:
            print("High")    
        if t2==4:
            print("Very low")
        print("""Air_Quality=""",end="")

        if r5==0:
            print("Toxic")
        elif r5==1:
            print("Poisonous")
        elif r5==2 :
            print("Combatible")
        elif r5==3:
            print("Good")
        elif r5==4:
            print("Earth-like")
        elif r5==5:
            print("Not breathable")
        elif r5==6:
            print("Very bad")
        elif r5==7:
            print("Dangerous")
        elif r5==8:
            print("Breathabe")      
        elif r5==9: 
            print("Bad")
        
        print("""Terrain=""",end="")
        if r8==0:
            print("plain")
        elif (r8==1 or r3==0) :
            print("Mountains")
        elif r8==2: 
            print("Hills")
        elif (r8==3 or r3==1):
            print("Oceans")
        elif (r8==4 or r3==7): 
            print("Desert")
        elif r8==5: 
            print("Highly Elevated")
        elif r8==6:
            print("Smooth Plain") 
        elif r8==7:
            print("Hilly Mountains") 
        elif r8==8: 
            print("Water-World")
        elif r8==9: 
            print("Earth-Like")
        Drones-=1
        print("""-----------Enter 1 to Settle in this planet
    	----------OR
    	Enter 2 to continue on the same course""")
        Plan=str(input("Enter Your Choice :"))
        if Plan!="1" and Plan!="2":
            print("Invalid Input")
        if Plan=="1":
            i=2
    if u_i=="1" or u_i=="2":
        me+=10
        if random.randint(0,999)==333 or(r==1 and u_i=="1") or(r==3 and u_i=="1") and i < 1 and Plan==2:
            print("The spaceship has been sucked into a black hole.Every thing is over.")
            i=2
        elif r2==0 and Plan==2:
            print("The space ship has been hit by solar wind while passing near a star.")
            SpaceShip_HP=SpaceShip_HP-9
            air_s=air_s-10
            human-=5
        elif r2==1 or r2==2 or r2==3 or r2==4 or r2==5 or r2==6 or r2==7 and Plan==2:
            print("Successful journey")
        elif r2==8 and Plan==2:
            print("Spaceship has been hit by Gamma Ray Burst.")
            SpaceShip_HP-=90
            human-=10
        elif r2==9 or r2==10 or r2==11 or r2==12 and Plan==2:
            print("Successful journey")
        elif r2==13 and Plan==2:
            print("Spaceship has been damaged due to a Supernova. Air Quality detector has destroyed.")
            air_s=air_s-100
            human-=5
            SpaceShip_HP-=40
        elif r2==14 or r2==15 or r2==17 or r2==16 or r2==18 or r2==19 and Plan==2:
            print("Successful journey")
        elif r2==20 or (r==25 and u_i=="1" and rc==1) and Plan==2:
            print("""A meteorite has hit the Oxygen Regulator of the  spaceship. 
            	Oxygen level of the ship has decreased""")
            oxygen=oxygen-20
            SpaceShip_HP=SpaceShip_HP-10
        elif r2==21 or r2==22 or r2==23 or r2==24 and Plan==2:
            print("Successful journey")
        elif r2==25  and Plan==2:
            print("Due to long journey an additional fuel has been spend.")
            fuel=fuel-25
            air_s-=air_s-5
            ter_s=ter_s-10
        elif r2==26 or r2==27 or r2==28 and Plan==2:
            print("Successful journey")
        elif r2==29 and Plan==2:
            print("Alien Encounter!!!!!")
        if (r==0 or r==25) and rc==3 and u_i=="1" and i < 1  and Plan==2:
            print("""A meteorite has hit the Sleeping Chamber of the  spaceship. 18 people are dead. 
           	Oxygen level of the ship has decreased""")
            oxygen=oxygen-5
            SpaceShip_HP-=5
            human=human-18
        if (r==2 or r==23 or r==13) and u_i=="1" and i < 1  and Plan==2:
            print("You have extracted some fuel from the nebula and ship has been repaired.")
            fuel=fuel+20
            SpaceShip_HP+=10
        if (r==8 or r==14 or r==12 or r==20) and u_i=="1" and rc==2 and i < 1  and Plan==2:
            print("""Due to strong force of attraction extra fuel has been consumed.
        	    Due to extreme temperature Terain sensor has been damaged.""")
            ter_s=ter_s-10
            fuel=fuel-20
            air_s=air_s-7
        if r==11 and u_i=="1" and i < 1  and Plan==2:
            print("Due to storm the ship has been severly damaged")
            SpaceShip_HP-=50
            human-=2
        print()
        input("Press Enter to continue...")
        

    if fuel<=0:
        i=2
        print("GAME OVER, Fuel in the ship has finished.")
        input("Press Enter to Exit....." )
    if SpaceShip_HP<=0:
        i=2
        print("GAME OVER, Spaceship has destroyed.")
        input("Press Enter to Exit....." )
    if human<=0 :
        print("GAME OVER, All the humans have died in the spaceship.")
        input("Press Enter To Exit....." )
        i=2
    if oxygen<=0:
        print("GAME OVER, Oxygen in the ship has finished. All the humans have died in the spaceship.")
        input("Press Enter To Exit....." )
        i=2
        
    if u_i=="1" or u_i=="2":
        fuel-=random.randint(2,8)

if Plan=='1':    
    print()
    print("Conclusion")
    print()
    print("You have found a planet to humans to settle. The gravity of the planet is ",end="")
    score=0
    if r4==0:
        score+=100
        print("Very High. It is not at all suitable for the humans to live in.")
    elif r4==1:
        score+=500
        print("Medium. It is not suitable for the humans to live in.")
    elif r4==2:
        score+=1000
        print("Earth-like. It is the best choice.  ")
    elif r4==3:
        score+=100
        print("Extremely Low. It is not a good choice.")
    elif r4==4:
        score+=0
        print("Massive. It is the worst choice. Humans will be crushed by gravity.")
    elif r4==5:
        score+=300
        print("Low. Low gravity is not good. It will affect the development of humanity very severely.")
    elif r4==6:
        score+=300
        print("High. High gravity is not good. It will affect the development of humanity very severely.")
    elif r4==7:
        score+=1
        print("No gravity. Humans cannot live in zero gravity.")
    elif r4==8:
        score+=100
        print("Ultra low")
    elif r4==9:
        score+=100
        print("Very Low")

    if r6==0:
        score+=100
        print("The planet is Tiny")
    elif r6==1:
        score+=400
        print("The planet is Large")
    elif r6==2:
        score+=100
        print("The planet is Dwarf")
    elif r6==3:
        score+=200
        print("The planet is Huge")
    elif r6==4:
        score+=1000
        print("The planet is Earth-like")
    elif r6==5:
        score+=500
        print("The planet is Small")
    elif r6==6:
        score+=800
        print("The planet is Normal")
    elif r6==7:
        score+=400
        print("The planet is Big")
    elif r6==8:
        score+=200
        print("The planet is Medium")
    elif r6==9:
        score+=100
        print("The planet is Very Small")
        
    if r7==0:
        score+=50
        print("The life in this planet is Small Man-eating Worms")
    elif r7==1:
        score+=100
        print("The life in this planet is Sharp Clawed predators")
    elif r7==2:
        score+=200
        print("The life in this planet is Carnivores beast")
    elif r7==3:
        score+=1000
        print("The life in this planet is Herbivores Animals")
    elif r7==4:
        score+=200
        print("The life in this planet is Man-eanting plants")
    elif r7==5:
        score+=150
        print("The life in this planet is Toxic plants")
    elif r7==6:
        score+=100
        print("The life in this planet is Monsters")
    elif r7==7:
        score+=500
        print("The life in this planet is large Insects")
    elif r7==8:
        score+=150
        print("The life in this planet is Creatures With Large Wings")
    elif r7==9:
        score+=400
        print("The life in this planet is Flying animals")

    if t1==0 and (r3==3 or r3==7):
        print("The temperature of the planet is High")
        score+=300
    if t1==1:
        score+=500
        print("The temperature of the planet is Compatible")
    if t1==2:
        score+=300
        print("The temperature of the planet is Low")    
    if t1==3:
        score+=1000
        print("The temperature of the planet is Normal")
    else:
        print("The temperature of the planet is Not suitable")
        score+=1

    if t2==1:
        print("The amount of resources in the planet is Medium")
        score+=500
    if t2==2:
        print("The amount of resources in the planet is Low")
        score+=250
        
    if t2==3:
        print("The amount of resources in the planet is High")
        score+=1000
    if t2==4:
        print("The amount of resources in the planet is Good")
        score+=750

    if r5==0:
        print("The Air Quality of the planet is Toxic")
        score+=100
    elif r5==1:
        print("The Air Quality of the planet is Poisonous")
        score+=200
    elif r5==2 :
        print("The Air Quality of the planet is Combatible")
        score+=400
    elif r5==3:
        print("The Air Quality of the planet is Good")
        score+=800
    elif r5==4:
        print("The Air Quality of the planet is Earth-like")
        score+=1000
    elif r5==5:
        print("The Air Quality of the planet is Not breathable")
        score+=1
    elif r5==6:
        print("The Air Quality of the planet is Very bad")
        score+=200
    elif r5==7:
        print("The Air Quality of the planet is Dangerous")
        score+=100
    elif r5==8:
        print("The Air Quality of the planet is Breathabe")
        score+=400
    elif r5==9: 
        print("The Air Quality of the planet is Bad")
        score+=200

    if r8==0:
        print("The terrain of the planet is plain")
        score+=700
    elif (r8==1 or r3==0) :
        print("The terrain of the planet is Mountains")
        score+=200
    elif r8==2: 
        print("The terrain of the planet is Hills")
        score+=500
    elif (r8==3 or r3==1):
        print("The terrain of the planet is Oceans")
        score+=200
    elif (r8==4 or r3==7): 
        print("The terrain of the planet is Desert")
        score+=100
    elif r8==5: 
        print("The terrain of the planet is Highly Elevated")
        score+=500
    elif r8==6:
        print("The terrain of the planet is Smooth Plain")
        score+=800
    elif r8==7:
        print("The terrain of the planet is Hilly Mountains")
        score+=200
    elif r8==8: 
        print("The terrain of the planet is Water-World")
        score+=100
    elif r8==9: 
        print("The terrain of the planet is Earth-Like")
        score+=1000
    print("Your Score : ",score)

    d={}

    name=input("Enter you name:")
    if len(name)<1:
        name="Player"+str(r)+str(rc)+str(t2)+str(t1)
    n=""
    for i in range (0,len(name)):
        if name[i]!=" ":
            n+=name[i]
    print()
    s = open('User_Data.txt').read()
    s+=n+" "+str(score+me)
    f = open('User_Data.txt', 'w')
    print(s,file=f)
    f.close()
    a=s.split()
    print("--------ScoreBoard-------")
    for i in range(0,len(a),2):
        if i < len(a):
            d[a[i]]=a[i+1]
            
    s=sorted(d.items(), key =
			lambda kv:(kv[1], kv[0]))
    
    for i in range(len(s)-1,len(s)-16,-1):
        print(s[i])
        
    
    print()
    input("Press Enter To Exit....." )
    
    
