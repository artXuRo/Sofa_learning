from stlib.scene import MainHeader, ContactHeader
from stlib.visuals import ShowGrid
from stlib.solver import DefaultSolver
from stlib.physics.rigid import Cube
from stlib.physics.rigid import Floor

def createScene(rootNode):
    """This is the first scene"""
    MainHeader(rootNode2, gravity=[0.0,-981.0,0.0])
    ContactHeader(rootNode, alarmDistance=15, contactDistance=10) 

    Floor(rootNode,
          translation=[0.0,-160.0,0.0],
          isAStaticObject=True,
		  uniformScale=2.0)

    Cube(rootNode,
         translation=[0.0,0.0,0.0],
         uniformScale=20.0)


    return rootNode




