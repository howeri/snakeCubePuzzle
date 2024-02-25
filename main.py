import copy

def dfs(state, path=None):
    if path is None:
        path = []
    path.append(state)

    # Is puzzle solved? Check if all locations occupied.
    all_elements_are_one = True
    for sublist in state['OccupiedLocations']:
        for inner_list in sublist:
            for element in inner_list:
                if element != 1:
                    all_elements_are_one = False
                    break
            if not all_elements_are_one:
                break
        if not all_elements_are_one:
            break
    if all_elements_are_one:
        print('Puzzle Solved!')

        # Show Solution
        sol = []
        for step in range(len(segmentLen)-1):
            sol.append(path[step]['direction']) 
        print('Rotate with the following axis:')
        print(sol)
        return True
    else:
        print('Solving...')
    
    # Find possible roations
    all_possible_moves = ['x', '-x', 'y', '-y', 'z', '-z']
    if state['direction']=='x':
        all_possible_moves.remove('x')
        all_possible_moves.remove('-x')
    elif state['direction']=='y':
        all_possible_moves.remove('y')
        all_possible_moves.remove('-y')
    elif state['direction']=='z':
        all_possible_moves.remove('z')
        all_possible_moves.remove('-z')
    
    # Consider length of the extension and space limits 
    removeList = []
    for move in all_possible_moves:
        if  move=='x' and state['currentLocaion'][0]+segmentLen[state['segmentNum']]-1>2:
            removeList.append('x')
        if  move=='-x' and state['currentLocaion'][0]-segmentLen[state['segmentNum']]+1<0:
            removeList.append('-x')
        if  move=='y' and state['currentLocaion'][1]+segmentLen[state['segmentNum']]-1>2:
            removeList.append('y')
        if  move=='-y' and state['currentLocaion'][1]-segmentLen[state['segmentNum']]+1<0:
            removeList.append('-y')
        if  move=='z' and state['currentLocaion'][2]+segmentLen[state['segmentNum']]-1>2:
            removeList.append('z')
        if  move=='-z' and state['currentLocaion'][2]-segmentLen[state['segmentNum']]+1<0:
            removeList.append('-z')
    for removeMove in removeList:
        all_possible_moves.remove(removeMove) 

    # Check if location already occupied
    removeList = []
    for move in all_possible_moves:
        newOccupoedLocation_move = []
        for blockNum in range(segmentLen[state['segmentNum']]-1):
            if  move=='x':
                newBlock = [state['currentLocaion'][0]+blockNum+1, state['currentLocaion'][1], state['currentLocaion'][2]]
                newOccupoedLocation_move.append(newBlock)
            if  move=='-x':
                newBlock = [state['currentLocaion'][0]-blockNum-1, state['currentLocaion'][1], state['currentLocaion'][2]]
                newOccupoedLocation_move.append(newBlock)
            if  move=='y':
                newBlock = [state['currentLocaion'][0], state['currentLocaion'][1]+blockNum+1, state['currentLocaion'][2]]
                newOccupoedLocation_move.append(newBlock)
            if  move=='-y':
                newBlock = [state['currentLocaion'][0], state['currentLocaion'][1]-blockNum-1, state['currentLocaion'][2]]
                newOccupoedLocation_move.append(newBlock)
            if  move=='z':
                newBlock = [state['currentLocaion'][0], state['currentLocaion'][1], state['currentLocaion'][2]+blockNum+1]
                newOccupoedLocation_move.append(newBlock)
            if  move=='-z':
                newBlock = [state['currentLocaion'][0], state['currentLocaion'][1], state['currentLocaion'][2]-blockNum-1]
                newOccupoedLocation_move.append(newBlock)
        for newOccupoedLocation_i in newOccupoedLocation_move:
            if state['OccupiedLocations'][newOccupoedLocation_i[2]][newOccupoedLocation_i[1]][newOccupoedLocation_i[0]]==1 and not move in removeList:
                removeList.append(move)
    for removeMove in removeList:
        all_possible_moves.remove(removeMove) 

    # Loop through all possible moves
    for move in all_possible_moves:
        if  move=='x':
            state_new = {'currentLocaion': [state['currentLocaion'][0]+segmentLen[state['segmentNum']]-1, state['currentLocaion'][1], state['currentLocaion'][2]],\
                         'OccupiedLocations': copy.deepcopy(state['OccupiedLocations']), \
                         'direction': move, \
                         'segmentNum': state['segmentNum']+1}
            for blockNum in range(segmentLen[state['segmentNum']]-1):
                newBlock = [state['currentLocaion'][0]+blockNum+1, state['currentLocaion'][1], state['currentLocaion'][2]]
                state_new['OccupiedLocations'][newBlock[2]][newBlock[1]][newBlock[0]]=1
            if dfs(state_new, path):
                return True
            path.pop()
            # return False
            
        if  move=='-x':
            state_new = {'currentLocaion': [state['currentLocaion'][0]-segmentLen[state['segmentNum']]+1, state['currentLocaion'][1], state['currentLocaion'][2]],\
                         'OccupiedLocations': copy.deepcopy(state['OccupiedLocations']), \
                         'direction': move, \
                         'segmentNum': state['segmentNum']+1}
            for blockNum in range(segmentLen[state['segmentNum']]-1):
                newBlock = [state['currentLocaion'][0]-blockNum-1, state['currentLocaion'][1], state['currentLocaion'][2]]
                state_new['OccupiedLocations'][newBlock[2]][newBlock[1]][newBlock[0]]=1
            if dfs(state_new, path):
                return True
            path.pop()
            # return False
                    
        if  move=='y':
            state_new = {'currentLocaion': [state['currentLocaion'][0], state['currentLocaion'][1]+segmentLen[state['segmentNum']]-1, state['currentLocaion'][2]],\
                         'OccupiedLocations': copy.deepcopy(state['OccupiedLocations']), \
                         'direction': move, \
                         'segmentNum': state['segmentNum']+1}
            for blockNum in range(segmentLen[state['segmentNum']]-1):
                newBlock = [state['currentLocaion'][0], state['currentLocaion'][1]+blockNum+1, state['currentLocaion'][2]]
                state_new['OccupiedLocations'][newBlock[2]][newBlock[1]][newBlock[0]]=1
            if dfs(state_new, path):
                return True
            path.pop()
            # return False
                    
        if  move=='-y':
            state_new = {'currentLocaion': [state['currentLocaion'][0], state['currentLocaion'][1]-segmentLen[state['segmentNum']]+1, state['currentLocaion'][2]],\
                         'OccupiedLocations': copy.deepcopy(state['OccupiedLocations']), \
                         'direction': move, \
                         'segmentNum': state['segmentNum']+1}
            for blockNum in range(segmentLen[state['segmentNum']]-1):
                newBlock = [state['currentLocaion'][0], state['currentLocaion'][1]-blockNum-1, state['currentLocaion'][2]]
                state_new['OccupiedLocations'][newBlock[2]][newBlock[1]][newBlock[0]]=1
            if dfs(state_new, path):
                return True
            path.pop()
            # return False
            
        if  move=='z':
            state_new = {'currentLocaion': [state['currentLocaion'][0], state['currentLocaion'][1], state['currentLocaion'][2]+segmentLen[state['segmentNum']]-1],\
                         'OccupiedLocations': copy.deepcopy(state['OccupiedLocations']), \
                         'direction': move, \
                         'segmentNum': state['segmentNum']+1}
            for blockNum in range(segmentLen[state['segmentNum']]-1):
                newBlock = [state['currentLocaion'][0], state['currentLocaion'][1], state['currentLocaion'][2]+blockNum+1]
                state_new['OccupiedLocations'][newBlock[2]][newBlock[1]][newBlock[0]]=1
            if dfs(state_new, path):
                return True
            path.pop()
            # return False
        
        if  move=='-z':
            state_new = {'currentLocaion': [state['currentLocaion'][0], state['currentLocaion'][1], state['currentLocaion'][2]-segmentLen[state['segmentNum']]+1],\
                         'OccupiedLocations': copy.deepcopy(state['OccupiedLocations']), \
                         'direction': move, \
                         'segmentNum': state['segmentNum']+1}
            for blockNum in range(segmentLen[state['segmentNum']]-1):
                newBlock = [state['currentLocaion'][0], state['currentLocaion'][1], state['currentLocaion'][2]-blockNum-1]
                state_new['OccupiedLocations'][newBlock[2]][newBlock[1]][newBlock[0]]=1
            if dfs(state_new, path):
                return True
            path.pop()
            # return False
    return False


## APPLICATION
# Define state as a set {[currentLocaion], [OccupiedLocations], pointingDirection, segmentNum}
# Define puzzle to start with first 2 segment laying on xy plane. Consider where the 3rd segment goes.
segmentLen = [3,2,2,3,2,3,2,2,3,3,2,2,2,3,3,3,3]

OccupiedLocations = []
for i in range(3):
    temp2 = []
    for j in range(3):
        temp = []
        for k in range(3):
            temp.append(0)
        temp2.append(temp)
    OccupiedLocations.append(temp2)
OccupiedLocations[0][0][0]=1
OccupiedLocations[0][0][1]=1
OccupiedLocations[0][0][2]=1
OccupiedLocations[0][1][2]=1

state = {'currentLocaion': [2,1,0], 'OccupiedLocations': OccupiedLocations, 'direction': 'y', 'segmentNum': 2}
if not dfs(state):
    print("No path found.")
