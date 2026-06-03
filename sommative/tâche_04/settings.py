# Screen Configuration
WIDTH = 900
HEIGHT = 700
FPS = 60

# Colors (RGB)
LANE_COLOR = (242, 199, 119)     # Light maple wood color
GUTTER_COLOR = (40, 30, 20)       # Dark wooden gutters
WHITE = (255, 255, 255)
RED = (220, 40, 40)
BLACK = (20, 20, 20)
BLUE = (0, 102, 204)
GOLD = (218, 165, 32)
GREY = (180, 180, 180)

# Game Physics & Sizing
BALL_RADIUS = 14  
PIN_RADIUS = 12
FRICTION = 0.992   

# 5-Pin Specific Point Values (Left to Right: 2, 3, 5, 3, 2)
PIN_VALUES = [2, 3, 5, 3, 2]

# Bowling Ball Catalog Data
BALL_CATALOG = {
    "Softrolls": [
        {"name": "Missiles", "color": (140, 20, 20), "style": "stripe"},
        {"name": "Ballistics", "color": (20, 140, 80), "style": "speckle"},
        {"name": "Sidewinders", "color": (90, 20, 140), "style": "swirl"},
        {"name": "Tornado Alleys", "color": (30, 30, 30), "style": "spiral"}
    ],
    "Aramiths": [
        {"name": "Classic Cream", "color": (245, 235, 200), "style": "solid"},
        {"name": "Belgian Blue", "color": (20, 70, 160), "style": "solid"}
    ],
    "EPCO": [
        {"name": "Sparkle", "color": (220, 40, 180), "style": "glitter"},
        {"name": "Starline", "color": (240, 180, 20), "style": "star"}
    ],
    "Paramounts": [
        {"name": "Marble Pro", "color": (100, 50, 20), "style": "marble"},
        {"name": "Royal Satin", "color": (110, 20, 60), "style": "solid"}
    ]
}