# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util


from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]
    def evaluationFunction(self, currentGameState, action):
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        newScore = 0
        newCapsules = successorGameState.getCapsules()
        # Variables generated for later use
        # Variables are data pulled from currentGame State
        oldPos = currentGameState.getPacmanPosition()
        oldFood = currentGameState.getFood()
        oldCapsules = currentGameState.getCapsules()
        explore = []
        positionP = list(successorGameState.getPacmanPosition())
        if action == Directions.STOP:
          return -float("inf")
        for food in currentGameState.getFood().asList():
            xAxis = 0
            yAxis = 1
            x = food[xAxis] - positionPacman[xAxis]
            y = food[yAxis] - positionPacman[xAxis]
            x = -1 * abs(x)
            y = -1 * abs(y)
            xAndy = x + y
            explore.append(xAndy)
        return max(explore)
            

        # def closestGhost():
        #     tmp = []
        #     tmp.append(newGhostStates[0])
        #     for x in newGhostStates:
        #         if manhattanDistance(newPos, x.getPosition())\
        #         < manhattanDistance(newPos, tmp[-1].getPosition()):
        #             tmp.append(x)
        #     return tmp[-1]
        # def closestFood():
        #     tmp = []
        #     tmp.append(newFood.asList()[0])
        #     for x in newFood.asList():
        #          if manhattanDistance(newPos, x)\
        #          < manhattanDistance(newPos, tmp[-1]):
        #              tmp.append(x)
        #     return tmp[-1]

      




        # print "Closest food", closestFood()
        # if manhattanDistance(newPos, closestGhost().getPosition()) < 3:
        #     return 10 * manhattanDistance(newPos, closestGhost().getPosition())\
        #     + newScore
        # elif manhattanDistance(newPos, closestGhost().getPosition()) > 3\
        # and closestGhost().scaredTimer > 1\
        # and manhattanDistance(newPos, closestGhost().getPosition())\
        # < manhattanDistance(oldPos, closestGhost().getPosition()):
        #     return 10 * manhattanDistance(newPos, closestGhost().getPosition())\
        #     + newScore
        # else:
        #     return 1 / (manhattanDistance(newPos, closestFood()) + 1)\
        #      * 2 + 1 /(manhattanDistance(newPos, newCapsulses[0]) * 2
        #print "closest Ghost", closestGhost()     
        #Main of the function
        #computes for each Ghost on the bored
        #for x in newGhostStates:
          #if new position is moving towards a ghost lower the value of newScore
        #  if manhattanDistance(newPos, x.getPosition()) < manhattanDistance(oldPos, x.getPosition()):
        #    newScore = newScore - 1
            #print "Move is towards ghost points dropped", newScore
          #if new position is in a more dangerous area
          #needs to not move in this area if it can avoid it
          #lowers the value of moving to this area more heavily
          #only matters if the ghost is not scared or about to be not scared
        #  if manhattanDistance(newPos, x.getPosition()) < 2 and x.scaredTimer < 2:
            #Most dangerous area, need to heavily discourage moving this close
            #most points are removed
        #    if manhattanDistance(newPos, x.getPosition()) < 1.5:
		#print "Move is close ghost points dropped", newScore              
		#return newScore
            #points are removed to discourage this behavior
            #points are removed now  
          #  print "Move is close ghost points dropped", newScore
     #       return newScore
          #if findFood has elements in its list it hunts for food
          #due to [], an empty list returning as false
     #     if len(newFood.asList()) != 0:
              #for each food increases the value
              #only  if the new position is closer than the old position
   #           for y in newFood.asList():
      #          if manhattanDistance(newPos, y) < manhattanDistance(oldPos, y):
                  #currently only increases by a small amount
                  #the inverse of the distance
                  #the closer the more it increases
                  #capture for if it is at the location
        #          if manhattanDistance(newPos, y) == 0:
                   # print "Found food points increased", newScore +700
        #            return newScore + 1000
       #           newScore = newScore + 1 / manhattanDistance(newPos, y)
                 # print "moving towards food points increased", newScore
          #hunts for capsules
       #   for y in newCapsules:
            #if moving towards capsule increase value
      #      if manhattanDistance(newPos, y) < manhattanDistance(oldPos, y):
      #        newScore = newScore + 1/(manhattanDistance(newPos, y) + 1)
             # print "moving towards capsule points increased", newScore
          #if pacman is not near a ghost hunt for food
     #     if manhattanDistance(newPos, x.getPosition()) > 2:
            #if there is food on the board hunt
     #       if len(newFood.asList()) != 0:
              #for each food on the board increase value
      #        for y in newFood.asList():
                #if the food is 20 units away it is less
                #important than food that is closer
                #therefore more points are assigned for food that is closer
                #from very small at the other end of the board
                #if manhattanDistance(newPos, y) < 20\
		#and manhattanDistance(newPos, y) < manhattanDistance(oldPos, y):
                #  newScore = newScore + .5 / (manhattanDistance(newPos, y) + 1)
                #  print "moving towards furthest away capsule points increased", newScore
                #to fairly small in the far side of the board
                #if manhattanDistance(newPos, y) < 15\
		#and manhattanDistance(newPos, y) < manhattanDistance(oldPos, y):
                #  newScore = newScore + 1.0 / (manhattanDistance(newPos,y) + 1)                
                #  print "moving towards faraway capsule points increased", newScore
                #to half way across the board
    #            if manhattanDistance(newPos, y) < 10\
		#and manhattanDistance(newPos, y) < manhattanDistance(oldPos, y):
    #              newScore = newScore + 2.0/ (manhattanDistance(newPos, y)+ 1)
                #  print "moving towards capsule points increased", newScore
                #to close to the pacman
    #            if manhattanDistance(newPos, y) < 5\
		#and manhattanDistance(newPos, y) < manhattanDistance(oldPos, y):
    #              newScore = newScore + 5
              #    print "moving towards close capsule points increased", newScore
                #to help hunt down final food pellets
    #            if len(newFood.asList()) < 5\
		#and manhattanDistance(newPos, y) < manhattanDistance(oldPos, y):
     #             newScore = newScore + 20
                #  print "hunting final capsules", newScore
      #  return newScore
def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        #print "Pacman legal Actions", gameState.getLegalActions(0)
        #print "Get ghost1 Legal actions", gameState.getLegalActions(1)
        #print "Get ghost2 legal actions", gameState.getLegalActions(2)
        #print "self.", self.evaluationFunction
        #print "self.depth", self.depth

	      # bestAction = None
	      # maxMinValue = None
       #  for y in gameState.getLegalActions(0):
	      #     temp = self.minValue(gameState.generateSuccessor(0,y), 0, 1)
   	   #      if bestAction is None or  maxMinValue < temp :
		     #        bestAction = y
		     #        maxMinValue = temp
	      # return bestAction

       #  def minValue(self, state, depth, agentIndex):
	      #   if state.isWin() or state.isLose() or depth == self.depth:
       #        return self.evaluationFunction(state)
	      #   value = float("inf")
	      #   for y in state.getLegalActions(agentIndex):
	      #     if agentIndex ==  state.getNumAgents()- 1:
		     #        value = min(value, self.maxValue(state.generateSuccessor(agentIndex,y), depth+1))
	      #   else:
		     #      value = min( value, self.minValue(state.generateSuccessor(agentIndex,y),depth,agentIndex+1))
       #    return value


       #  def maxValue(self, state, depth):
	      #       if state.isWin() or state.isLose() or depth == self.depth:
	      #           return self.evaluationFunction(state)
	      #       value = -float("inf")
	      #       for y in state.getLegalActions(0):
	      #           value = max( value, self.minValue(state.generateSuccessor(0,y),depth, 1))
       #        return value

       #  util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

