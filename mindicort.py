
from time import time

import time
from utils import *

# player_dict = {}


team_a, team_b, player_order = create_teams_distribute_cards()
start_position = 0
hukum = None
hukum_flag = False
while True:
    if not player_order[start_position]['hand']:
        break # we break the loop when starting postion player has no cards left

    # we change the player order based on starting position, which is decided based on who won the last hand
    player_order = re_org_turn(
        start=start_position,
        player_list=player_order
    )

    # Logic for single round (hand), where every players puts in a single card on the table
    table_cards = []
    round_color = None
    heavy_weight = {}
    for index, player in enumerate(player_order):
        clear_screen()
        print_table(
            card_list=table_cards,
            teams = [team_a, team_b],
            round_color=round_color,
            hukum=hukum
        )
        print(f"{player['name']}'s turn!!")
        print_hand(player['hand'])
        
        while True:
            # if the players turn is not the first one and he does not have round color card
            if round_color and round_color not in [_crd['color'] for _crd in player['hand']]:
                # if the hukum is not revealed then hukum will be revealed
                if not hukum_flag:
                    hukum = choose_hukum()
                    print("Hukum Revealed:", hukum)
                    # if player has hukum, we force them to choose one
                    if hukum in [_crd['color'] for _crd in player['hand']]:
                        while True:
                            hukum_input = input("Choose one of your hukum cards: ")
                            _selected_card = determine_card(hukum_input)
                            card_found = False
                            if _selected_card['color']==hukum:
                                for card in player['hand']:
                                    if hukum == _selected_card['color']:
                                        if card['value'] == _selected_card['value']:
                                            card_found = True
                                            valid_card = card
                            
                            if card_found:
                                weight = valid_card['weight']
                                break
                    # if player does not hukum and hukum is revealed
                    else:
                        while True:
                            non_hukum_input = input("Tu Gaand mara 😂😂 aur card choose kar koi bhi: ")
                            _selected_card = determine_card(non_hukum_input)
                            card_found = False
                            for card in player['hand']:
                                if card['color'] == _selected_card['color']:
                                    if card['value'] == _selected_card['value']:
                                        card_found = True
                                        valid_card = card
                            if card_found:
                                # player has to chose hyde because the round color is hukum and he does not have hukum
                                weight = 0
                                break
                            else:
                                print("Kem Gaand bali gai?? Card barabar choose kar ni!!")
                
                    # if no errors we break the input loop for hukum revealing logic
                    player['hand'].remove(valid_card)
                    hukum_flag = True
                    if valid_card['color']==hukum:
                        weight = weight + HUKUM_WEIGHT
                    heavy_weight.update({
                        weight : index
                    })
                    break


            card_input = input("Choose a card from your hand: ")
            try:
                _selected_card = determine_card(card_input)
                card_found = False
                for card in player['hand']:
                    if card['color'] == _selected_card['color']:
                        if card['value'] == _selected_card['value']:
                            card_found = True
                            valid_card = card

                # logic for checking if selected card is from the hand or not
                if not card_found:
                    print("Chose card from your own hand, MF!!")
                    continue

                # logic for checking if the selected card is from the same color or not
                
                # if it is first turn or sub sequent turns
                if not round_color:
                    round_color = valid_card['color']
                    weight = valid_card['weight']
                else:
                    # if the player hand has cards of the round color
                    if round_color in [_crd['color'] for _crd in player['hand']]:
                        # check if the chosen card is of the round color
                        if valid_card['color'] == round_color:
                            weight = valid_card['weight']
                            pass
                        else:
                            print(f"You have cards of {round_color}, choose one from them.")
                            continue
                    else:
                        if valid_card['color']==hukum:
                            weight = valid_card['weight'] + HUKUM_WEIGHT
                        else:
                            weight = 0

                # if no errors we break the input loop
                player['hand'].remove(valid_card)
                heavy_weight.update({
                    weight : index
                })
                break
            except IndexError:
                print("Input Length should be 2 or 3 characters long!!")
                continue
            except Exception as exc:
                print("Error occured, choose again.", str(exc))
                continue
        
        table_cards.append(valid_card)
    
    # logic to store mindi/s to the winning team
    mindis_in_hand = []
    for _card in table_cards:
        if _card['value'] == "10":
            mindis_in_hand.append(_card)

    # Logic for determining who won the hand!!
    index_winner = heavy_weight[max(heavy_weight.keys())]
    winner = player_order[index_winner]
    print(f"\nWinner: {winner['name']}!!")
    # logic to find out the which team's player won and adding the scores to that team
    if winner in team_a['players']:
        team_a['hands'] += 1
        team_a['mindi'].extend(mindis_in_hand)
    elif winner in team_b['players']:
        team_b['hands'] += 1
        team_b['mindi'].extend(mindis_in_hand)
    else:
        print("winner team not found!!")
    

    print_table(
        card_list=table_cards,
        teams = [team_a, team_b],
        round_color=round_color,
        hukum=hukum
        )
    time.sleep(3)
    # if the winner was last player, we need to set start position to 0 else we set the start posistion to the next player
    start_position = index_winner


player_order = re_org_turn(
    start=start_position,
    player_list=player_order
    )

