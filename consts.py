import tcod

# Screen Parameters
SCREEN_X = 40
SCREEN_Y = 40
CENTER_X = SCREEN_X // 2
CENTER_Y = SCREEN_Y // 2
GAME_TITLE = "Puzzler: The Roguelike"
FONT_PATH = "terminal.png"

# Colors
WHITE = tcod.Color(255, 255, 255)

# Tile Characters
T_SPACE = 0
T_PLAYER = 1

# Action Types
PLAYER_ACTION = {
    tcod.KEY_UP: "M_UP",
    tcod.KEY_DOWN: "M_DOWN",
    tcod.KEY_LEFT: "M_LEFT",
    tcod.KEY_RIGHT: "M_RIGHT"
}
GAME_ACTION = {
    tcod.KEY_ESCAPE : "QUIT"
}



