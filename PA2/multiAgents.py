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
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """

        "Turn food system into a call to grid.asList()"


        #def manhattanDistance( xy1, xy2 ):
        #    "Returns the Manhattan distance between points xy1 and xy2"
        #    return abs( xy1[0] - xy2[0] ) + abs( xy1[1] - xy2[1] )

        #Useful information you can extract from a GameState (pacman.py)
        #Generate variables for use later
        #Variables are data pulled from SuccessorGameState
        #except for successorGameState itself
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        newScore = 0
        newCapsules = successorGameState.getCapsules()
        #Variables generated for later use
        #Variables are data pulled from currentGame State
        oldPos = currentGameState.getPacmanPosition()
        oldFood = currentGameState.getFood()
        oldCapsules = currentGameState.getCapsules()

        def closestGhost():
            tmp = float("inf")
            for x in newGhostStates:
                tmp = min(manhattanDistance(newPos, x.getPosition()), tmp)
            return tmp

        def closestFood():
            tmp = float("inf")
            for x in newFood.asList():
                tmp = min(manhattanDistance(newPos, x), tmp)
            return tmp

        print "newPos", newPos
        print "Closest food", closestFood()
        print "Closest Ghost", closestGhost()
        if sum(newScaredTimes) > 0:
            return 10 * 1.0 /(closestGhost() + 1) + newScore + 10000
        elif closestGhost() < 3:
            return -100.0 /(0.1+closestGhost()) #+ ss100.0/(len(newFood.asList())+0.1) + newScore
        elif len(newCapsules) != 0:
            return 5.0/(manhattanDistance(newPos, newCapsules[0]) + .1) 
        else:
            return 100.0/(len(newFood.asList())+0.1) + 10*closestGhost() + newScore

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

        bestAction = None
        maxMinValue = None
        for y in gameState.getLegalActions(0):
            temp = self.minValue(gameState.generateSuccessor(0,y), 0, 1)
            if bestAction is None or  maxMinValue < temp :
                bestAction = y
                maxMinValue = temp
        return bestAction

    def minValue(self, state, depth, agentIndex):
        if state.isWin() or state.isLose() or depth == self.depth:
            return self.evaluationFunction(state)
        value = float("inf")
        for y in state.getLegalActions(agentIndex):
            if agentIndex ==  state.getNumAgents()- 1:
                value = min(value, self.maxValue(state.generateSuccessor(agentIndex,y), depth+1))
            else:
                value = min(value, self.minValue(state.generateSuccessor(agentIndex,y),depth,agentIndex+1))
        return value


    def maxValue(self, state, depth):
        if state.isWin() or state.isLose() or depth == self.depth:
            return self.evaluationFunction(state)
        value = -float("inf")
        for y in state.getLegalActions(0):
            value = max(value, self.minValue(state.generateSuccessor(0,y),depth, 1))
        return value

        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """   

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        bestAction = None
        maxMinValue = None
        a = -float("inf")
        b = float("inf")
        for y in gameState.getLegalActions(0):
            temp = self.minValue(gameState.generateSuccessor(0,y), a, b, 0, 1)
            if bestAction is None or  maxMinValue < temp :
                bestAction = y
                maxMinValue = temp
            if maxMinValue > b: return bestAction
            a = max(a,maxMinValue)
        return bestAction


    def maxValue(self, state, a, b, depth):
        if state.isWin() or state.isLose() or depth == self.depth:
            return self.evaluationFunction(state)
        v = -float("inf")
        for y in state.getLegalActions(0):
            v = max(v, self.minValue(state.generateSuccessor(0,y), a, b, depth, 1))
            if v > b: return v
            a = max(a,v)
        return v
    
    def minValue(self, state, a, b, depth, agentIndex):
        if state.isWin() or state.isLose() or depth == self.depth:
            return self.evaluationFunction(state)
        v = float("inf")
        for y in state.getLegalActions(agentIndex):
            if agentIndex == state.getNumAgents() -1:
                v = min(v, self.maxValue(state.generateSuccessor(agentIndex,y), a, b, depth+1))
            else:
                v = min(v, self.minValue(state.generateSuccessor(agentIndex,y), a, b,depth, agentIndex+1))
            if v < a: return v
            b = min(b,v)
        return v
        
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

