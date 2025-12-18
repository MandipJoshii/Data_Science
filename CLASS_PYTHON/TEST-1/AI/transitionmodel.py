

def transitionModel(state,action):
    if action == "left":
        return state + 1
    elif action == "right":
        return state - 1


print(transitionModel(5,"left"))