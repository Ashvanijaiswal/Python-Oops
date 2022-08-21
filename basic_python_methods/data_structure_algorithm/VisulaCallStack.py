class Tree:
  def __init__(self):
    self.call: str = ''
    self.returned: Any = None
    self.children: List[Tree] = []

def waysToClimb(n,possibleSteps,tree):
    tree.call='waysToClimb('+str(n)+')'
    if(n==0):
        tree.returned=1
        return 1
    else:
        nbWays=0
        for steps in possibleSteps:
            if(n-steps)>=0:
                child:Tree=Tree()
                tree.children.append(child)
                nbWays+=waysToClimb(n-steps,possibleSteps,child)
        tree.returned=nbWays
        return nbWays
def printTree(tree, indent=''):
  if tree is None or len(tree.children) == 0:
    print(tree.call + ' returned ' + str(tree.returned))
  else:
    print(tree.call + ' returned ' + str(tree.returned))
    for child in tree.children[:-1]:
      print(indent + '|' + '-' * 4, end='')
      printTree(child, indent + '|' + ' ' * 4)
    child = tree.children[-1]
    print(indent + '└' + '-' * 4, end='')
    printTree(child, indent + '  ' * 4)

n=10
possibleSteps=[2,4,5,8]
recursionTree=Tree()
waysToClimb(n,possibleSteps,recursionTree)
printTree(recursionTree)
