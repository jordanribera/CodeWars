class MapSolver:
    map = []
    miner = {'x':0,'y':0}
    exit = {'x':0,'y':0}
    paths = []
    
    def __init__(self, map, miner, exit):
        self.map = map
        self.miner = miner
        self.exit = exit
        self.paths = []
        
    def solve(self):
        self.doMove([], self.miner, None)
        
        if len(self.paths) > 0:
            shortestPath = self.paths[0]
            for thisPath in self.paths:
                if len(thisPath) < len(shortestPath):
                    shortestPath = thisPath
                
            return shortestPath
        
        
    def doMove(self, previousMoves, currentPosition, nextMove):
        if nextMove is not None:
            previousMoves.append(nextMove)
            if nextMove == "up":
                currentPosition["y"] -= 1
            if nextMove == "down":
                currentPosition["y"] += 1
            if nextMove == "left":
                currentPosition["x"] -= 1
            if nextMove == "right":
                currentPosition["x"] += 1
                
        if currentPosition["x"] == self.exit["x"] and currentPosition["y"] == self.exit["y"]:
            self.paths.append(previousMoves)
            return True
    
        possibleMoves = []
        if currentPosition["y"] > 0:
            if self.map[currentPosition["x"]][currentPosition["y"] - 1]:
                possibleMoves.append("up")
        if currentPosition["y"] < len(self.map[0]) - 1:
            if self.map[currentPosition["x"]][currentPosition["y"] + 1]:
                possibleMoves.append("down")
        if currentPosition["x"] > 0:
            if self.map[currentPosition["x"] - 1][currentPosition["y"]]:
                possibleMoves.append("left")
        if currentPosition["x"] < len(self.map) - 1:
            if self.map[currentPosition["x"] + 1][currentPosition["y"]]:
                possibleMoves.append("right")
                
        if nextMove == "up" and "down" in possibleMoves:
            possibleMoves.remove("down")
        if nextMove == "down" and "up" in possibleMoves:
            possibleMoves.remove("up")
        if nextMove == "left" and "right" in possibleMoves:
            possibleMoves.remove("right")
        if nextMove == "right" and "left" in possibleMoves:
            possibleMoves.remove("left")
            
        print previousMoves
        print currentPosition
        print possibleMoves
            
        if len(possibleMoves) < 1:
            print "DEAD END"
            return False
        else:   
            for thisMove in possibleMoves:
                self.doMove(previousMoves[:], {"x": currentPosition["x"], "y": currentPosition["y"]}, thisMove)
            return True
                
        return False

def solve(map, miner, exit):
    mapSolver = MapSolver(map, miner, exit)
    return mapSolver.solve()
