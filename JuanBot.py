#!  python3
import pyautogui
import time
import os
import logging
import sys
import random
import copy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) # uncomment to block debug log messages

# Constants
PEARL = 'pearl'

# Global variables
LEVEL = 1 # current level being played

# various coordinates of objects in the game
GAME_REGION = () # (left, top, width, height) values coordinates of the entire game window
PEARL_REGION = ()
GO_COORDS = None
NEW_GAME_COORDS = None

def main():
    """Runs the entire program. Pearls Before Swine 3 game must be visible on the screen and the New Game button visible."""
    logging.debug('JuanBot - Yuval Gal - Omer Asher')
    logging.debug('To interrupt mouse movement, move mouse to upper left corner.\n')
    pyautogui.alert("Start bot?","JuanBot")
    getGameRegion()
    setupCoordinates()
    navigateStartGameMenu()
    startPlaying()

def imPath(filename):
    """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filename with 'images/' prepended."""
    return os.path.join('images', filename)


def getGameRegion():
    """Obtains the region that the Sushi Go Round game is on the screen and assigns it to GAME_REGION. The game must be at the start screen (where the New Game button is visible)."""
    global GAME_REGION

    # identify the top-left corner
    logging.debug('Finding game region...')
    region = pyautogui.locateOnScreen(imPath('top_right_corner.png'))
    print()
    if region is None:
        raise Exception('Could not find game on screen. Is the game visible?')

    # calculate the region of the entire game
    topRightX = region[0] + region[2] # left + width
    topRightY = region[1] # top
    GAME_REGION = (topRightX - 1792, topRightY, 1792, 891) # the game screen is 95% of website's screen
    logging.debug('Game region found: %s' % (GAME_REGION,))

def setupCoordinates():
    """Sets several of the coordinate-related global variables, after acquiring the value for GAME_REGION."""
    global NEW_GAME_COORDS, GO_COORDS, LEVEL, PEARL_REGION

    logging.debug('Initialising button coordinates...')
    NEW_GAME_COORDS = (GAME_REGION[0] + 1280, GAME_REGION[1] + 480)
    GO_COORDS = (GAME_REGION[0] + 560, GAME_REGION[1] + 280)
    #PEARL_REGION = (GAME_REGION[0] + 450, GAME_REGION[1] + 600, 648, 224)
    # Extended pearl region for high levels
    PEARL_REGION = (GAME_REGION[0] + 320, GAME_REGION[1] + 600, 1239, 222)
    LEVEL = 1

def navigateStartGameMenu():
    """Performs the clicks to navigate form the start screen (where the New Game button is visible) to the beginning of the first level."""
    # Click on everything needed to get past the menus at the start of the
    # game.

    # click on New Game
    # pyautogui.click(NEW_GAME_COORDS[0],NEW_GAME_COORDS[1],duration=0.25)
    logging.debug('Clicked on New Game button.')

def startPlaying():
    # Starting to play the game
    screenshot = pyautogui.screenshot(region=PEARL_REGION)

    logging.debug('Starting to play...')
    logging.debug('Searching for pearls in first row...')
    for pos in pyautogui.locateAll(imPath("pearl.png"),screenshot):
        print(pos)

    print()
    logging.debug('Searching for pearls in second row...')
    for pos in pyautogui.locateAll(imPath("pearl2.png"),screenshot):
        print(pos)

    print()
    logging.debug('Searching for pearls in third row...')
    for pos in pyautogui.locateAll(imPath("pearl3.png"),screenshot):
        print(pos)

main()