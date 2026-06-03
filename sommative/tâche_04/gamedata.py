# gamedata.py

OPPONENTS = {
    "Alberta": [
        {"name": "Karie Kreutz", "avg": 255, "skill": 0.85},
        {"name": "Katie Rayner", "avg": 248, "skill": 0.82},
        {"name": "Tim Wiseman", "avg": 262, "skill": 0.88},
        {"name": "Dexter Wiseman", "avg": 250, "skill": 0.83},
        {"name": "Tyler Tytgat", "avg": 258, "skill": 0.86}
    ],
    "Newfoundland": [
        {"name": "Jeff Young", "avg": 265, "skill": 0.90},
        {"name": "Jen Young", "avg": 252, "skill": 0.84},
        {"name": "Shane Chafe", "avg": 260, "skill": 0.87},
        {"name": "Brad Glynn", "avg": 245, "skill": 0.80},
        {"name": "Melissa Manor", "avg": 240, "skill": 0.78}
    ],
    "Ontario": [
        {"name": "Martin Talbot", "avg": 258, "skill": 0.86},
        {"name": "Mitch Davies", "avg": 261, "skill": 0.88},
        {"name": "Matt Houston", "avg": 250, "skill": 0.83},
        {"name": "Cody Laycox", "avg": 254, "skill": 0.85},
        {"name": "Kayla Anderson", "avg": 246, "skill": 0.81}
    ]
}

TOURNAMENTS = [
    {
        "tour_name": "Western Canadian Bowling Tour (WCBT)",
        "stops": [
            {"stop": 1, "name": "The Beef Bowl", "center": "Panorama Lanes", "city": "Medicine Hat, AB"},
            {"stop": 2, "name": "The Autumn Open", "center": "Paradise Lanes", "city": "Calgary, AB"},
            {"stop": 3, "name": "TPC at Sherwood", "center": "Sherwood Bowl", "city": "Sherwood Park, AB"},
            {"stop": 4, "name": "The Regina Classic", "center": "Golden Mile Bowl", "city": "Regina, SK"},
            {"stop": 5, "name": "The Manitoba Open", "center": "St. James Lanes", "city": "Winnipeg, MB"},
            {"stop": 6, "name": "The Heritage Traditional", "center": "Heritage Lanes", "city": "Red Deer, AB"}
        ]
    },
    {
        "tour_name": "The Club Tour",
        "stops": [
            {"stop": 1, "name": "The Club Tour Event (Michelob Ultra)", "center": "NEB's Fun World", "city": "Oshawa, ON"},
            {"stop": 2, "name": "The Homeguard Club Tour", "center": "Echo Bowl", "city": "Brantford, ON"},
            {"stop": 3, "name": "The Timmins Invitational", "center": "Midtown Bowl", "city": "Timmins, ON"}
        ]
    },
    {
        "tour_name": "Newfoundland Bowling Tour (NBT)",
        "stops": [
            {"stop": 1, "name": "Paradise Bowl", "center": "Paradise Bowl", "city": "Mount Pearl, NL"},
            {"stop": 2, "name": "Plaza Bowl", "center": "Plaza Bowl", "city": "St. John's, NL"},
            {"stop": 3, "name": "Holiday Lanes", "center": "Holiday Lanes", "city": "St. John's, NL"}
        ]
    }
]