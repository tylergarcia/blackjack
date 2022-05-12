import random
import sys
import os
from rich import print

'''
- Look at force-implementing best practices by viewing them like all of the many times in the music/mixing days that I kicked myself for not just learning the right way first. 
    - To do this you must ensure that when it's time to implement a best practice, it's within your practical ability to do so. 
      Once it becomes a choice of whether or not to take the extra time, take the extra time. 
      Like editing drums and NOT checking all of the crossfades
      Like writing a program and NOT making a skeleton pseudocode outline
'''
while True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_score = 0
    dealer_score = 0
    player_hand = []
    dealer_hand = []

    def print_graphic():
        print('''[bold red]
        .------.            _     _            _    _            _    
        |A_  _ |           | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
            
            [/bold red]''')


    def deal_card_dealer():
        global dealer_hand, dealer_score
        if len(dealer_hand) > 0:
            card_choose = random.randint(0, len(cards)-1)
            dealer_hand.append(cards[card_choose])
        if len(dealer_hand) == 0:
            card_choose = random.randint(0, len(cards)-1)
            dealer_hand.append(cards[card_choose])
            card_choose = random.randint(0, len(cards)-1)
            dealer_hand.append(cards[card_choose]) 
        dealer_score = sum(dealer_hand)
        
        print('[gray]-------------------------[/]')
        if len(dealer_hand) == 2:
            print('\nDealer\'s first card:' + ' [X] [' + str(dealer_hand[1]) + ']')
        if len(dealer_hand) == 3:
            print('\nDealer\'s third card:' + ' [' + str(dealer_hand[0]) + '] [' + str(dealer_hand[1]) + '] [' + str(dealer_hand[2]) + ']')
        if len(dealer_hand) == 4:
            print('\nDealer\'s fourth card:' + ' [' + str(dealer_hand[0]) + '] [' + str(dealer_hand[1]) + '] [' + str(dealer_hand[2]) + '] [' + str(dealer_hand[3]) + ']')
        print('[gray]-------------------------[/]')
        check_scores()

    def deal_card_player():
        global player_score, player_hand
        if len(player_hand) > 0:
            card_choose = random.randint(0, len(cards)-1) 
            player_hand.append(cards[card_choose])
        if len(player_hand) == 0:
            card_choose = random.randint(0, len(cards)-1) 
            player_hand.append(cards[card_choose])
            card_choose = random.randint(0, len(cards)-1) 
            player_hand.append(cards[card_choose])
        player_score = sum(player_hand)

        print('[gray]-------------------------[/]')
        if len(player_hand) == 2:
            print('\nYour cards:' + ' [' + str(player_hand[0]) + '] [' + str(player_hand[1]) + ']' + '\nYour current score: ' + str(player_score))    
        if len(player_hand) == 3:
            print('\nYour cards:' + ' [' + str(player_hand[0]) + '] [' + str(player_hand[1]) + '] [' + str(player_hand[2]) + ']' + '\nYour current score: ' + str(player_score))
        if len(player_hand) == 4:
            print('\nYour cards:' + ' [' + str(player_hand[0]) + '] [' + str(player_hand[1]) + '] [' + str(player_hand[2]) + '] [' + str(player_hand[3]) +']' + '\nYour current score: ' + str(player_score))
        print('[gray]-------------------------[/]')
        check_scores()

    def final_score():
        # os.system('clear')
        print('\n***Final score***\n\nDealer: ' + str(dealer_score) + '\nPlayer: ' + str(player_score))
        if player_score > dealer_score and player_score < 22:
            print('[bold green]You win!!![/]')
        if player_score < dealer_score and dealer_score < 22:
            print('[bold red]Sorry, you lose[/]')
        if player_score == dealer_score:
            print('[bold yellow]Tie![/]')
        print('Enter [bold blue]X[/] to exit, or [bold blue]N[/] for a new game.')
        exit_answer = input()
        if exit_answer == 'x' or exit_answer == 'X':
            sys.exit()
        elif exit_answer == 'n' or exit_answer == 'N':
            pass

    # perhaps modify to check for low threshold of score?
    def check_scores():
        if player_score == 21:
            print('\n\n:spade_suit:[bold red]You got Blackjack![/bold red]:spade_suit:')
            final_score()
        elif dealer_score == 21:
            print('\n\n[bold red]Dealer got Blackjack.[/bold red]')
            final_score()
        elif player_score > 21:
            print('\n\n[bold red]You BUST with ' + str(player_score))
            final_score()
        elif dealer_score > 21:
            print('\n\n[bold red]Dealer BUST with ' + str(dealer_score))
            final_score()
        else:
            pass
        
    #                     #
    # MAIN RUN OF PROGRAM #
    #                     # 

    '''
    newgame_answer = input('Would you like to play a game of Blackjack? Answer \'y\' or \'n\': ')
    if newgame_answer == 'y' or 'Y':
        pass
    else:
        sys.exit()
    '''

    print_graphic()

    deal_card_player()

    deal_card_dealer()

    # Asking player for hit
    hit_answer = input('\nWould you like another card? Enter Y or N: ')
    if hit_answer == 'Y' or hit_answer == 'y':
        # os.system('clear')
        deal_card_player()
    elif hit_answer == 'n' or hit_answer == 'N':
        check_scores()
    if dealer_score < player_score:
        deal_card_dealer()
    elif dealer_score == 15 or dealer_score == 16:
        if random.randint(0,9) >= 5:
            deal_card_dealer()
        else:
            pass 
    elif dealer_score > 16:
        print('\n[red]Dealer stays.[/]')
        exit    

    check_scores()
    final_score()

