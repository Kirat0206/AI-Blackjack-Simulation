class BasicStrategy:

    # def __init__(self):
        # Representing tables using nested dictionaries
    hard_totals_strategy = {
        2: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        3: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        4: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        5: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        6: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        7: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        8: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        9: [' ', ' ', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        10: [' ', ' ', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'],
        11: [' ', ' ', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
        12: [' ', ' ', 'H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
        13: [' ', ' ', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
        14: [' ', ' ', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
        15: [' ', ' ', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
        16: [' ', ' ', 'S', 'S', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H']
        # 17: [' ', ' ', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
    }

    soft_totals_strategy = {
        5: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        6: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        7: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        8: [' ', ' ', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'],
        9: [' ', ' ', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        10: [' ', ' ', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'H', 'H'],
        11: [' ', ' ', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
        12: [' ', ' ', 'H', 'H', 'S', 'S', 'S', 'H', 'H', 'H', 'H', 'H'],
        13: [' ', ' ', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        14: [' ', ' ', 'H', 'H', 'H', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        15: [' ', ' ', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        16: [' ', ' ', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        17: [' ', ' ', 'H', 'D', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        18: [' ', ' ', 'D', 'D', 'D', 'D', 'D', 'S', 'S', 'H', 'H', 'H'],
        19: [' ', ' ', 'S', 'S', 'S', 'S', 'D', 'S', 'S', 'S', 'S', 'S'],
        20: [' ', ' ', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
        21: [' ', ' ', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']
        
    }

    split_strategy = {
        1: [' ', ' ', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
        2: [' ', ' ', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
        3: [' ', ' ', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
        4: [' ', ' ', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
        5: [' ', ' ', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
        6: [' ', ' ', 'H', 'H', 'D', 'D', 'D', 'H', 'H', 'H', 'H', 'H'],
        7: [' ', ' ', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'N', 'N', 'N'],
        8: [' ', ' ', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y'],
        9: [' ', ' ', 'Y', 'Y', 'Y', 'Y', 'Y', 'N', 'Y', 'Y', 'N', 'N'],
        10: [' ', ' ', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
        
    }

    # Function that checks if a players hand is eligible to be split (Exactly two cards in the hand that are equal)
    @staticmethod
    def split_hand(hand):
        return (len(hand) == 2) and (hand[0] == hand[1])