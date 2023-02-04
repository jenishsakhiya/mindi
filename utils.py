from constants import *
from colorama import Fore, Style, Back
import random
from typing import List
import os

def print_card(card: dict, return_string=False):
    color = card.get('color')
    value = card.get('value')
    if len(value) < 2:
        value = f"{value} "
    template_placeholder = "zz "
    if card['color']== '♦':
        daimand_card = (f"""
{Fore.RED}{Back.WHITE}+----------------+{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|v       D       |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|c      DDD      |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|      DDDDD     |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|     DDDDDDD    |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|    DDDDDDDDD   |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|   DDDDDDDDDDD  |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|    DDDDDDDDD   |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|     DDDDDDD    |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|      DDDDD     |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|       DDD     c|{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|zz      D      v|{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}+----------------+{Style.RESET_ALL}""")
        card = daimand_card.replace("v ",value).replace("c",color).replace(' v', value[::-1]).replace('01', '10').replace('D','♦')
        card = card.replace(template_placeholder, f"D{value}")   
    elif card['color']== '♠':
        black_card = (f"""
{Back.WHITE}{Fore.BLACK}+----------------+{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|v               |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|c      B        |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|     /BBB\      |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|    /BBBBB\     |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|   /BBBBBBB\    |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|  /BBBBBBBBB\   |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}| (BBBBB BBBBB)  |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|  \BB/^|^\BB/   |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|   **  B  **    |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|       B       c|{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|zz  BBBBBBB    v|{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}+----------------+{Style.RESET_ALL}""")
        card = black_card.replace("v ",value).replace("c",color).replace(' v', value[::-1]).replace('01', '10').replace('B','♠')    
        card = card.replace(template_placeholder, f"B{value}")
    elif card['color'] == '♥':
        heart_card = (f"""
{Fore.RED}{Back.WHITE}+----------------+{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|v               |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|c  HH     HH    |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|  HHHH   HHHH   |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}| HHHHHH HHHHHH  |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|  HHHHHHHHHHH   |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|   HHHHHHHHH    |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|    HHHHHHH     |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|     HHHHH      |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|      HHH       |{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|       H       c|{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}|zz             v|{Style.RESET_ALL}
{Fore.RED}{Back.WHITE}+----------------+{Style.RESET_ALL}""")
        card = heart_card.replace("v ",value).replace("c",color).replace(' v', value[::-1]).replace('01', '10').replace('H','♥')
        card = card.replace(template_placeholder, f"H{value}")
    elif card['color'] == '♣':
        club_card = (f"""
{Back.WHITE}{Fore.BLACK}+----------------+{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|v               |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|c               |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|      /C\       |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|     CCCCC      |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|     \(C)/      |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|  (C\_.C._/C)   |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}| (CCCCCCCCCCC)  |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|   CC/^C^\CC    |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|       |        |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|      C^C      c|{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|zz             v|{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}+----------------+{Style.RESET_ALL}""")
        card = club_card.replace("v ",value).replace("c",color).replace(' v', value[::-1]).replace('01', '10').replace('C','♣')
        card = card.replace(template_placeholder, f"C{value}")
    if return_string:
        return card
    else:
        print(card)

def take_card(cards):
    for card in cards:
        yield card

def print_hand(hand: List[dict]):
    hand_pixel = []
    
    # for card in hand:
    #     
    #     for line in card.split('\n'):
    #         hand_pixel.append(line)
    card_pixels = print_card(hand[0], return_string=True).split('\n')
    for line_num, _ in enumerate(card_pixels):
        hand_line = ""
        for card in hand:
            lines = print_card(card=card, return_string=True).split('\n')
            if line_num:
                line_str = lines[line_num].rstrip(f"{Style.RESET_ALL}")
                hand_line = f"{hand_line[:-14]}{Style.RESET_ALL}" + line_str
            else:
                hand_line = lines[line_num]
        # hand_line = "".join(hand_line)
        hand_pixel.append(f"{hand_line}{Style.RESET_ALL}")
    hand_string = "\n".join(hand_pixel)
    # hand_string = f"{hand_string}{Style.RESET_ALL}"
    print(hand_string)

def print_table(card_list: List[dict], teams: List[dict], round_color=None, hukum=None):
    print("\n")
    print("* # * # * # " * 8)
    print("\n")

    for team in teams:
        print("Team Name:", team['name'])
        print("Team Players:", ", ".join(
            [_player['name'] for _player in team['players']]
            )
        )
        print("Hands Won:", team['hands'])
        print("10s Won:", " ".join(
            [_mindi['color'] for _mindi in team['mindi']]
        ))
        print("---------------------")
    
    print("\n")
    print("* # * # * # " * 8)
    print("\n")
    if hukum:
        print("HUKUM:", hukum)
    
    
    if not card_list:
        print("The table is currently empty!!")
        return
    hand_pixel = []
    card_pixels = print_card(card_list[0], return_string=True).split('\n')
    for line_num, _ in enumerate(card_pixels):
        hand_line = ""
        for card in card_list:
            lines = print_card(card=card, return_string=True).split('\n')
            if line_num:
                line_str = lines[line_num]
                table_background = "+" if line_num%2==0 else " "
                hand_line = f"{hand_line}  {table_background}  {line_str}"
            else:
                hand_line = lines[line_num]
        hand_pixel.append(f"{hand_line}{Style.RESET_ALL}")
    hand_string = "\n".join(hand_pixel)
    if round_color:
        print("Round color is:", round_color)
    print(hand_string)

def create_deck(shuffle=True, num_of_deck=1):
    deck = []
    values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    colors = ['♦','♠','♥','♣']
    for _ in range(0,num_of_deck):
        for color in colors:
            for value in values:
                try:
                    weight = int(value)
                except Exception:
                    if value=="A":
                        weight = 14
                    elif value=="K":
                        weight = 13
                    elif value=="Q":
                        weight = 12
                    elif value=="J":
                        weight = 11

                deck.append({
                    "color": color,
                    "value": value,
                    "weight": weight
                })
    if shuffle:
        random.shuffle(deck)
    return deck

def choose_hukum():
    colors = ['♦','♠','♥','♣']
    random.shuffle(colors)
    return random.choice(colors)

def re_org_turn(start, player_list):
    for _ in range(0, start):
        player_list.append(player_list.pop(0))
    return player_list

def clear_screen():
    os.system("clear")

def create_teams_distribute_cards():
    """
    The function creates teams based on inputs from User and 
    also distribute cards based on number of decks selected by User
    Retuns: Team objects with players attached to it, player order, total mindis 
    """
    num_of_deck = int(input("enter number of decks :"))
    
    # each deck has 4 mindis
    total_mindis = num_of_deck * 4
    
    deck = create_deck(
        shuffle=True,
        num_of_deck=num_of_deck
        )
    num_of_players = int(input("enter number of players :"))
    if len(deck)%num_of_players==0:
        hand_size = int(len(deck) / num_of_players)
        players = [ {"name":"", "hand":[]} for _ in range(num_of_players)]
        card_picker = take_card(deck)

        for i in range(hand_size):
            for player in players:
                player['hand'].append(
                    next(card_picker)
                    )
        player_list = []
        for player in players:
            name_of_p = str(input('enter player name -->'))
            player['name'] = name_of_p
            player['hand'] = sorted(player['hand'], key=lambda card: COLOR_MAPPER[card["color"]])
            # print(player)
            player_list.append(player)
            # print_hand(player['hand'])
        
        random.shuffle(player_list)
        team_a_players = player_list[0::2]
        team_b_players = player_list[1::2]

        print("Player Order:", " : ".join(
            [_player['name'] for _player in player_list]
        ))

        team_a = {
            "name" : "Team A",
            "hands" : 0, # number of hands won by the team!!
            "mindi" : [],
            "players" : team_a_players
        }

        team_b = {
            "name" : "Team B",
            "hands" : 0,
            "mindi" : [],
            "players" : team_b_players
        }

        return team_a, team_b, player_list, total_mindis

def determine_card(card_code):
    color_code = card_code[0]
    value = card_code[1:].strip().upper()
    color = COLOR_SYMBOL_MAPPER[color_code.upper()]
    card = {
        "color" : color,
        "value" : value
    }
    return card


def check_win(team_a, team_b, mindis_to_win):
    if len(team_a['mindi']) >= mindis_to_win:
        return team_a['name']
    elif len(team_b['mindi']) >= mindis_to_win:
        return team_b['name']
    elif len(team_b['mindi']) == mindis_to_win - 1 and len(team_a['mindi']) == mindis_to_win:
        if team_a['hands'] > team_b['hands']:
            return team_a['name']
        elif team_a['hands'] < team_b['hands']:
            return team_b['name']
        else:
            return "Draw"
    else:
        return None


def check_mindicort_possiblity(team_a, team_b):
    for team in [team_a, team_b]:
        if not team['mindi']:
            return True
    return False