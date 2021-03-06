from cards import Cards, Deck, Player, Dealer

blackjack = """\033[1;33m
__________.__                 __          ____.              __    
\______   \  | _____    ____ |  | __     |    |____    ____ |  | __
 |    |  _/  | \__  \ _/ ___\|  |/ /     |    \__  \ _/ ___\|  |/ /
 |    |   \  |__/ __ \   \___|    <  /\__|    |/ __ \   \___|    < 
 |______  /____(____  /\___  >__|_ \ \________(____  /\___  >__|_ \  
        \/          \/     \/     \/               \/     \/     \/  
\033[1;m
"""

symbols= """\033[1;31m
		                               _
		       ,'`.    _  _    /\    _(_)_
		      (_,._)  ( `' )  <  >  (_)+(_)
		        /\     `.,'    \/      |
\033[1;m
"""


print blackjack
print symbols
name = raw_input("What is your name? ")
chip = input("How many starter chips do you want? ")
while type(chip)!= int: 
	chip = input("Please put a intenger. Dummy. ")
bet = input("How much do you want to wager each time? ")
while type(bet) != int: 
	bet = input("Please put a intenger. Dummy. ")
myDeck = Deck()
player = Player(name, chip, bet)
dealer = Dealer()

def start_game():
	myDeck.create()
	myDeck.shuffle()
	myDeck.deal(player, dealer)

def lose():
	player.chips-=player.bet
	print """
 __   _____  _   _   _     ___  ____  _____     _______           _______  
 \ \ / / _ \| | | | | |   / _ \/ ___|| ____|   / /_   _|         |_   _\ \ 
  \ V / | | | | | | | |  | | | \___ \|  _|    | |  | |             | |  | |
   | || |_| | |_| | | |__| |_| |___) | |___   | |  | |             | |  | |
   |_| \___/ \___/  |_____\___/|____/|_____|  | |  |_|    _____    |_|  | |
                                               \_\       |_____|       /_/ 
"""
	print "You lost \033[1;31m{}\033[1;m chips. You currently have \033[1;31m{}\033[1;m\n".format(player.bet, player.chips)
	if player.chips<=0: 
		print """
                              )                 
 (                         ( /(                 
 )\ )      )    )     (    )\())  )     (  (    
(()/(   ( /(   (     ))\  ((_)\  /((   ))\ )(   
 /(_))_ )(_))  )\  '/((_)   ((_)(_))\ /((_|()\  
(_)) __((_)_ _((_))(_))    / _ \_)((_|_))  ((_) 
  | (_ / _` | '  \() -_)  | (_) \ V // -_)| '_| 
   \___\__,_|_|_|_|\___|   \___/ \_/ \___||_|   
                                                
"""
		print "\033[1;41mYou have no more chips. Get out!\033[1;m"
		exit()
def win():
	player.chips+=player.bet
	print """
Y)    yy  O)oooo  U)    uu    W)      ww I)iiii N)n   nn 
 Y)  yy  O)    oo U)    uu    W)      ww   I)   N)nn  nn 
  Y)yy   O)    oo U)    uu    W)  ww  ww   I)   N) nn nn 
   Y)    O)    oo U)    uu    W)  ww  ww   I)   N)  nnnn 
   Y)    O)    oo U)    uu    W)  ww  ww   I)   N)   nnn 
   Y)     O)oooo   U)uuuu      W)ww www  I)iiii N)    nn 
                                                         
                                                         
"""
	print "You gained \033[1;32m{}\033[1;m chips. You currently have \033[1;32m{}\033[1;m\n".format(player.bet, player.chips)
def the_game():
	myDeck.reset(player, dealer)
	start_game()

	print "Your total value is \033[1;33m{}\033[1;m".format(player.sum)
	if dealer.sum == 21 and player.sum == 21:
		print "Double black jack! You tied!"

		return
	elif dealer.sum == 21: 
		print "Dealer got black jack! Game ends. You a loser"
		lose()
		return 
	elif player.sum == 21: 
		print "You got a black jack! Game ends."
		win()
		return

	answer2 = raw_input("\nDo you want to hit or stay? (H = hit; S = stay)")
	while answer2.upper() == 'H':
		player.hit(myDeck)
		print "Your total value is \033[1;33m{}\033[1;m".format(player.sum)
		hand_sum = player.sum
		if hand_sum>21: 
			print "You're a Loser!"
			lose()
			return
		else: 
			answer2 = raw_input("\nDo you want to hit or stay? (H = hit; S = stay)")
	if answer2.upper() == 'S':
		player.stay()
		while(dealer.sum < 17): 
			dealer.hit(myDeck)
		if dealer.sum > 21: 
			print "Dealer bust at \033[1;31m{}\033[1;m! Player wins!".format(dealer.sum)
			win()
			return
		elif dealer.sum > player.sum: 
			print "Dealer wins \033[1;31m{}-{}\033[1;m. You lost. Loser".format(dealer.sum, player.sum)
			lose()
			return
		elif dealer.sum < player.sum:
			print "You win \033[1;31m{}-{}\033[1;m. You're not a loser. I guess".format(player.sum, dealer.sum)
			win()
			return
		else: 
			print "You tied \033[1;31m{}-{}\033[1;m. That's weird".format(player.sum, dealer.sum)
			return


answer = raw_input("\nAre you ready to start the game? (Y/N)")
while(answer.upper() == 'Y'):
	the_game()
	answer = raw_input("Do you want to play again? (Y/N)")



