import random

cards = {
    1: 26000051,  # Ram Rider
    2: 26000052,  # Zappies
    3: 26000053,  # Rascals
    4: 26000054,  # Cannon Cart
    5: 26000056,  # Skeleton Barrel
    6: 26000058,  # Wall Breakers
    7: 26000060,  # Goblin Giant
    8: 26000061,  # Fisherman
    9: 26000062,  # Magic Archer
    10: 26000063,  # E-Dragon
    11: 26000064,  # Firecracker
    12: 26000067,  # E-Golem
    13: 26000068,  # Battle Healer
    14: 28000013,  # Clone
    15: 28000012,  # Tornado
    16: 28000011,  # Log
    17: 28000010,  # Graveyard
    18: 28000009,  # Poison
    19: 28000008,  # Zap
    20: 28000007,  # Lightning
    21: 28000006,  # Mirror
    22: 28000005,  # Freeze
    23: 28000004,  # Gobblin Barrel
    24: 28000003,  # Rocket
    25: 28000002,  # Rage
    26: 28000000,  # Fireball
    27: 28000001,  # Arrows
    28: 26000007,  # Witch
    29: 26000008,  # Barbarians
    30: 26000006,  # Balloon
    31: 26000005,  # Minions
    32: 26000004,  # Pekka
    33: 26000003,  # Giant
    34: 26000002,  # Goblins
    35: 26000001,  # Archers
    36: 26000000,  # Knight
    37: 26000046,  # Bandit
    38: 26000045,  # Executioner
    39: 26000044,  # Hunter
    40: 26000043,  # Elite Barbarians
    41: 26000042,  # Electro Wizard
    42: 26000041,  # Goblin Gang
    43: 26000040,  # Dart Goblin
    44: 26000039,  # Mega Minion
    45: 26000038,  # Ice Golem
    46: 26000037,  # Inferno Dragon
    47: 26000036,  # Battle Ram
    48: 26000035,  # Lumberjack
    49: 26000034,  # Bowler
    50: 26000033,  # Sparky
    51: 26000032,  # Miner
    52: 26000031,  # Fire Spirits
    53: 26000030,  # Ice Spirit
    54: 26000029,  # Lava Hound
    55: 26000028,  # 3 Musketeers
    56: 26000027,  # Dark Prince
    57: 26000026,  # Princess
    58: 26000025,  # Guards
    59: 26000024,  # Royal Giant
    60: 26000023,  # Ice Wizard
    61: 26000022,  # Minion Horde
    62: 26000021,  # Hog Rider
    63: 26000020,  # Giant Skeleton
    64: 26000019,  # Spear Goblins
    65: 26000018,  # Mini Pekka
    66: 26000017,  # Wizard
    67: 26000016,  # Prince
    68: 26000015,  # Baby Dragon
    69: 26000014,  # Mega Knight
    70: 26000013,  # Bomber
    71: 26000012,  # Skeleton Army
    72: 26000011,  # Valkyrie
    73: 26000010,  # Skeletons
    74: 26000009,  # Golem
    75: 27000005,  # Barbarian Hut
    76: 27000004,  # Bomb Tower
    77: 27000003,  # Inferno Tower
    78: 27000002,  # Mortar
    79: 27000000,  # Cannon
    80: 26000049,  # Bats
    81: 26000048,  # Night Witch
    82: 26000047,  # Royal Recruits
    83: 26000050,  # Royal Ghost
    84: 26000083,  # Mother Witch
    85: 26000085,  # Electro Giant
    86: 28000016,  # Heal Spirit
    87: 28000017,  # Snowball
    88: 28000018,  # Royal Delivery
    89: 26000080,  # Skeleton Dragons
    90: 27000012,  # Goblin Cage
    91: 26000059,  # Royal Hogs
    92: 27000008,  # X-Bow
    93: 27000007,  # Elexir Pump
    94: 27000001,  # Spear Goblin Hut
    95: 27000010,  # Furnace
    96: 27000009,  # Tombstone
    97: 26000057,  # Flying Machine
    98: 27000006,  # Tesla
    99: 26000014,  # Musketeer
    100: 26000084,  # E-Spirit
    101: 28000014,  # Earthquake
    102: 28000015,  # Barbarian Barrel
}
link = 'https://link.clashroyale.com/deck/en?deck='


def get_link():
    global link
    list = []
    for _ in range(1, 9):
        num = random.randint(1, 102)
        if cards[num] not in list:
            list.append(cards[num])
            link = link.__add__(str(cards[num]) + ';')
    link = link.rstrip(link[-1])
    print(link)


get_link()
