from stlib.scene import  MainHeader
from stlib.visuals import ShowGrid
from stlib.solver import DefaultSolver
from stlib.physics.rigid import Floor

def createScene(rootNode):
    ShowGrid(rootNode)

    #
    MainHeader(rootNode,gravity=[0.0,-981.0,0.0])

    cube=rootNode.createChild("Cube")


    totalMass = 1.0
    volume =1.0
    inertiaMatrix = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]

    cube.createObject('MechanicalObject', name="DOF", template="Rigid3", translation=[0.0,0.0,0.0],rotation=[0.0,0.0,0.0])
    cube.createObject('UniformMass', name="vertexMass", vertexMass=[totalMass, volume, inertiaMatrix[:]])
    #cube.createObject('UniformMass', name="vertexMass", vertexMass=[totalMass, volume, inertiaMatrix[:]])

    cube.createObject('EulerImplicit', name='odesolver')
    cube.createObject('CGLinearSolver', name='Solver')


    visual = cube.createChild("CubeVisula")
    """gramma has been changed!!!!!!!!!!!!!!!"""
    visual.createObject("MeshObjLoader", name="loader", filename="mesh/smCube27.obj")
    visual.createObject('OglModel', name="Visual", src="@loader", color=[0.1, 0.0, 1.0], scale=20.0)
    visual.createObject('RigidMapping')



    Floor(rootNode,
          translation=[0.0,-300.0,0.0],
          uniformScale=5.0,
          isAStaticObject=True)

    return rootNode