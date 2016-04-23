import math
class Astar(object):
	def __init__(self, SearchSpace, Start, Goal):
		self.OPEN = []
		self.CLOSED = []
		self.PATH = []
		self._graph = SearchSpace		
		self._start = Start
		self._goal = Goal
		self._current = self._start
		
		self.Reset()

	
	@property
	def current(self):		
		return self._current
	@current.setter
	def current(self, value):
		#set the current node				
		self._current = value
	def Reset(self):
		for n in self._graph:
			node = self._graph[n]			
			node.parent = None
			node.g = 0
			node.f = 0
			node. h = 0
		for n in self._graph:
			node = self._graph[n]
			self.SetNeighbors(node)
			xdist = int(math.fabs(self._goal.index[0] - node.index[0]))			
			xdist *= 10
			ydist = int(math.fabs(self._goal.index[1] - node.index[1]))
			ydist *= 10
			node.h = xdist + ydist
	
	def Run(self):
		self.Reset()
		open = self.OPEN
		closed = self.CLOSED
		start = self._start
		goal = self._goal
		open.append(start)
		print(open)
		while open:						
			open.sort(key = lambda x : x.f)
			current = open[0]
			open.remove(current)			
			closed.append(current)
			i = 0
			for adj in current.adjacents:
				if adj.walkable and adj not in closed:
					if adj not in open:
						open.append(adj)
						adj.parent = current						
						adj.g = 10 if i < 4 else 14
					else:
						move = 10 if i < 4 else 14
						movecost = move + current.g
						if movecost < adj.g: 
							adj.parent = current						
							adj.g = movecost
							
				i+=1
			if goal in open:
				self.PATH = self.GetPath(goal)
				break;
				
	def TestStart(self):
		self.current = self._start

	def GetPath(self, node):
		path = []
		current = node
		while(current != self._start):
			path.append(current.parent)
			current = current.parent
		return path
			
		
		
	def SetNeighbors(self, node):
	#always use rows b/c we go nxn
		rows = 15
		bot = node.id + 1
		top = node.id - 1
		right = node.id + rows
		left = node.id - rows
		t_right = right - 1
		t_left = left - 1
		b_right = right + 1
		b_left = left + 1
		adjs = [bot, top, right, left, b_right, b_left, t_right, t_left ]
		for i in adjs:
			if i in self._graph:			
				if self._graph[i].walkable:
					node.adjacents.append(self._graph[i])
					
				
		
'''
	TODO.Add(start)


	while (!TODO.IsEmpty())	// While there are squares to check
	{
		current = TODO.LowestF() // Get the lowest F
		TODO.Remove(current) 
		DONE.Add(current)

		foreach (adjacent square)
		{
			if (square.walkable && !DONE.Contains(square))
			{
				if (!TODO.Contains(square))
				{

					if (square.IsDestination())
					{
						RetracePath();
						return true; // Success
					}

					else
					{
						TODO.Add(square);
					
						square.Parent = current;
						// calcuate G and H
					}
				}

				else
				{
					int costToMoveToSquare = current.G + costToMove;

					if (costToMoveToSquare < square.G)
					{
						square.Parent = current;
						square.G = costToMoveToSquare;
						TODO.Sort();
					}
				}
			}
		}
	}

	return false; // Failure
	'''




