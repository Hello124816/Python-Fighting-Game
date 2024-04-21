from fighter import Fighter
fighter1 = Fighter("Player_1", 100, 0, 0, 20)
fighter2 = Fighter("Player_2", 150, 100, 0, 10)
print("Fighter 1 currently has HP: "+str(fighter1.hp))
print("Fighter 2 currently has HP: "+str(fighter2.hp))

fighter1.move(80,0)
fighter2.got_hit(fighter1)
print("Fighter 2 currently has HP: "+str(fighter2.hp))
#testing
