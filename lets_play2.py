import cardgame
from sys import argv

# Stacks Var 
cardgame.stack1
cardgame.stack2


print "Removing the pair cards!"

# removing pair
p1c = cardgame.stack1
n_p1c = []
for i in p1c:
    n_p1c.append(i[0][0])

p1 = list(set(n_p1c))

p2c = cardgame.stack2
n_p2c = []
for i in p2c:
    n_p2c.append(i[0][0])

p2 = list(set(n_p2c))

# Game start here
print p1
print p2
def letsplay():    
            print "Player 1 here is your card %r" % p1
            print "Select a card from player 2 from 0 to %r" % len(p2)
            select = raw_input('> ')
            i_select = p2.pop(int(select))
            
            print "You have selected card %r" % i_select
            print "Do you see duplicate with in your card %r" % p1
            ans = raw_input('(yes/no)> ')
            if ans == 'yes':
                print "Remove it from your card %r, select from 0 to %r" % (p1, len(p1) - 1)
                rm_duplicate = raw_input('> ')
                p1.pop(int(rm_duplicate))
            else:
                print "Adding to your cards!"
                p1.append(int(select))
                print p1 

            print "Player 2 here is your card %r" % p2
            print "Select a card from player 1 from 0 to %r" % len(p1)
            select = raw_input('> ')
            i_select = p1.pop(int(select))
            
            print "You have selected card %r" % i_select
            print "Do you see duplicate with in your card %r" % p2
            ans = raw_input('(yes/no)> ')
            if ans == 'yes':
                print "Remove it from your card %r, select from 0 to %r" % (p2, len(p2) - 1)
                rm_duplicate = raw_input('> ')
                p2.pop(int(rm_duplicate))
            else:
                print "Adding to your cards!"
                p2.append(int(select))
                print p2

for i in p1:
    for j in p2:
        if i == j:
            letsplay()
        else:
            if len(p1) < len(p2):
                print "Player One WIN!"
                print "Player ones card %r" % p1
                print "Player two card %r" % p2
            else:
                print "Player Two WIN!"
                print "Player two card %r" % p2
                print "Player one card %r" % p1
