# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #python pacman.py -l testMaze -p SearchAgent -a fn=dfs  use such sample command can help print and test result
    #python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs would be the sample testing command
    #it is the position search problem in the beginning

    #read gamestate in pacman.py, problem calls the searchagent, calls the gamestate in pacman.py
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    #problems r defined in the searchagents
    open_list =  util.Stack()    #[problem.getStartState()]   #(8, 1) as the start state
    open_list.push((problem.getStartState(),[]))
    #open_list.push(problem.getStartState())    #might have problems
    close_list = []
    #path = []        #a list to store all the path notations
    while open_list.isEmpty() is False:
        #cur_node = open_list.pop()
        (cur_node,path) = open_list.pop()
        if problem.isGoalState(cur_node):
            return path                 #if reaching the goal, then return the path
        close_list.append(cur_node)     #adding the node into the close state
        successors = problem.getSuccessors( cur_node)     #get a list of (states,action,cost)
        for (success_node, success_path, path_cost) in successors:
            if success_node not in close_list and success_node not in open_list.list:
                open_list.push((success_node,path+[success_path]))
                #path.append(success_path)
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #somehow have expanded state twice
    open_list = util.Queue()  # [problem.getStartState()]   #(8, 1) as the start state
    open_list.push((problem.getStartState(),[]))
    close_list = []
    while open_list.isEmpty() is False:
        #cur_node = open_list.pop()
        (cur_node,path) = open_list.pop()
        #print('curnode is ',cur_node)
        if problem.isGoalState(cur_node):
            return path  # if reaching the goal, then return the path
        if not cur_node in close_list:
            close_list.append(cur_node)
            successors = problem.getSuccessors(cur_node)  # get a list of (states,action,cost)
            for (success_node, success_path, path_cost) in successors:
                open_list.push((success_node, path + [success_path]))

    return []
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #in theory should use priority queue with function, just explore the priority function and the rest should be similar to bfs
    open_list = util.PriorityQueue()  # adding the cost function, testing
    #open_list.push( (problem.getStartState(),[]),0)#because the starting node cost 0   #((problem.getStartState(), []))
    counts = util.Counter()
    open_list.push((problem.getStartState(), []), 0)
    close_list = []
    while open_list.isEmpty() is False:
        (cur_node,path) = open_list.pop()
        if problem.isGoalState(cur_node):
            return path  # if reaching the goal, then return the path
        if not cur_node in close_list:
            close_list.append(cur_node)
            successors = problem.getSuccessors(cur_node)  # get a list of (states,action,cost)
            for (success_node, success_path, path_cost) in successors:
                counts[success_node] = counts[cur_node]   #use counts as a dictionary to add step numbers
                counts[success_node] += path_cost         #add new path_cost to the old ones
                open_list.push((success_node, path + [success_path]), counts[success_node])
    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #shouldn't it just be another priorityque with heuristic+the cost?
    open_list = util.PriorityQueue()  # adding the cost function, testing
    counts = util.Counter()
    cur_state = (problem.getStartState(), [])      #because not stringfied, need to stringfy cur_state first
    counts[str(cur_state[0])] += heuristic(cur_state[0],problem)  #dictionaries to add the step cost according to heuristic
    open_list.push(cur_state, counts[str(cur_state[0])])
    close_list = []

    while open_list.isEmpty() is False:
        (cur_node, path) = open_list.pop()
        if problem.isGoalState(cur_node):
            return path  # if reaching the goal, then return the path
        if not cur_node in close_list:
            close_list.append(cur_node)  # adding the node into the close state
            successors = problem.getSuccessors(cur_node)  # get a list of (states,action,cost)
            for (success_node, success_path, path_cost) in successors:
                updated_path = path + [success_path]
                counts[str(success_node)] = problem.getCostOfActions(updated_path)   #update with the current path to starting path cost
                counts[str(success_node)] += heuristic(success_node, problem)        #add estimate lowest cost to that node
                open_list.push((success_node, updated_path), counts[str(success_node)])
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
