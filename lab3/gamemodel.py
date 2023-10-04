from math import sin,cos,radians
import random

# Unnecessary clutter
fsdiisdf = 89
fsdiisdf += 1



#TODO: Deal with all TODOs in this file and also remove the TODO and HINT comments.

""" This is the model of the game"""
class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """
    def __init__(self, cannonSize: float, ballSize: float  ): #xBounds: tuple, standardYPos: float
        self.P1 = Player(self, "blue", -90, False)
        self.P2 = Player(self, "red", 90, True)
        self.CurrentPlayerIndex = 0
        self.currentWind = 0
        self.CannonSize = cannonSize
        self.BallSize = ballSize
        self.xBounds = (10,10)
        self.standardYPos = 10.0
        # HINT: This constructor needs to create two players according to the rules specified in the assignment text
        

    """ A list containing both players """
    def getPlayers(self):
        return [self.P1, self.P2]

    """ The height/width of the cannon """
    def getCannonSize(self):
        return self.CannonSize #Gets Cannon Size

    """ The radius of cannon balls """
    def getBallSize(self):
        return self.BallSize #Gets Ball SizeB
    """ The current player, i.e. the player whose turn it is """
    def getCurrentPlayer(self):
        return self.getPlayers()[self.getCurrentPlayerNumber()]

    """ The opponent of the current player """
    def getOtherPlayer(self):
        if self.getCurrentPlayerNumber() == 0:
            return self.getPlayers()[1]
        elif self.getCurrentPlayerNumber() == 1:
            return self.getPlayers()[0]
        
    
    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        return self.CurrentPlayerIndex
    
    """ Switch active player """
    def nextPlayer(self):
        self.CurrentPlayerIndex = not self.CurrentPlayerIndex

    """ Set the current wind speed, only used for testing """
    def setCurrentWind(self, wind):
        self.currentWind = wind
    
    def getCurrentWind(self):
        return self.currentWind

    """ Start a new round with a random wind value (-10 to +10) """
    def newRound(self):
        WIND_RANGE = 10
        new_wind = 2 * WIND_RANGE * random.random() - WIND_RANGE # set wind range to -WIND_RANGE to +WIND_RANGE
        self.setCurrentWind(new_wind)

""" Models a player """
class Player:
   #HINT: It should probably take the Game that creates it as parameter and some additional properties that differ between players (like firing-direction, position and color)
    def __init__(self, game: Game, color: str, xPos: float, is_left: bool, yPos: float = None):
        self.game = game
        self.color = color
        self.xPos = xPos
        self.score = 0
        self.is_left = is_left
        self.last_fired_angle_and_velocity = (45, 40)

       # if yPos is None:
      #      yPos = self.game.standardYPos
            

    """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """
    def fire(self, angle: float, velocity: float):
        wind = self.game.getCurrentWind
        xLower, xUpper = self.game.xBounds
        Projectile(angle, velocity, wind, self.xPos, self.yPos, xLower, xUpper)
        # The projectile should start in the middle of the cannon of the firing player
        # HINT: Your job here is to call the constructor of Projectile with all the right values
        # Some are hard-coded, like the boundaries for x-position, others can be found in Game or Player
        return None #TODO: this is just a dummy value

    """ Gives the x-distance from this players cannon to a projectile. If the cannon and the projectile touch (assuming the projectile is on the ground and factoring in both cannon and projectile size) this method should return 0"""
    def projectileDistance(self, proj):
        dist = abs(Projectile.getX() - Game.getOtherPlayer().getX()) - (Game.getBallSize()/2 + Game.getCannonSize()/2)
        if(dist <= 0): return 0
        return dist

        
            
        
        
        # HINT: both self (a Player) and proj (a Projectile) have getX()-methods.
        # HINT: This method should give a negative value if the projectile missed to the left and positive if it missed to the right.
        # The distance should be how far the projectile and cannon are from touching, not the distance between their centers.
        # You probably need to use getCannonSize and getBallSize from Game to compensate for the size of cannons/cannonballs
 
        return 0 #TODO: this is a dummy value.

    """ The current score of this player """
    def getScore(self):
        return self.score

    """ Increase the score of this player by 1."""
    def increaseScore(self, score_to_add: int = 1):
        self.score += score_to_add

    """ Returns the color of this player (a string)"""
    def getColor(self):
        return self.color 

    """ The x-position of the centre of this players cannon """
    def getX(self):
        return self.xPos

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
    def getAim(self):
        return self.last_fired_angle_and_velocity 

    """ This should do nothing """
    def doNothing(self):
        pass



""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    """
        Constructor parameters:
        angle and velocity: the initial angle and velocity of the projectile 
            angle 0 means straight east (positive x-direction) and 90 straight up
        wind: The wind speed value affecting this projectile
        xPos and yPos: The initial position of this projectile
        xLower and xUpper: The lowest and highest x-positions allowed
    """
    def __init__(self, angle: float, velocity: float, wind: float, xPos: float, yPos: float, xLower: float, xUpper: float):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xVelocity = velocity*cos(theta)
        self.yVelocity = velocity*sin(theta)
        self.wind = wind


    """ 
        Advance time by a given number of seconds
        (typically, time is less than a second, 
         for large values the projectile may move erratically)
    """
    def update(self, time):
        # Compute new velocity based on acceleration from gravity/wind
        newYVelocity = self.yVelocity - 9.8*time
        newXVelocity = self.xVelocity + self.wind*time
        
        # Move based on the average velocity in the time period 
        self.xPos = self.xPos + time * (self.xVelocity + newXVelocity) / 2.0
        self.yPos = self.yPos + time * (self.yVelocity + newYVelocity) / 2.0

        # make sure yPos >= 0
        self.yPos = max(self.yPos, 0)
        
        # Make sure xLower <= xPos <= mUpper   
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        
        # Update velocities
        self.yVelocity = newYVelocity
        self.xVelocity = newXVelocity
        
    """ A projectile is moving as long as it has not hit the ground or moved outside the xLower and xUpper limits """
    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    """ The current y-position (height) of the projectile". Should never be below 0. """
    def getY(self):
        return self.yPos
