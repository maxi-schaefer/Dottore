# @author: gokimax
# Created: 4/28/2024
#######################################################################################
# All the imports needed
import os
import shutil

#######################################################################################
# MakeENV Class
class MakeEnv:
    """
    The MakeEnv class creates the build directory and clones the source code
    """
    
    def __init__(self) -> None:
        self.buildDir = os.path.join(os.getcwd(), 'build')

    def makeEnv(self) -> None:
        """
        Creates the build directory
        """
        if os.path.exists(self.buildDir):
            shutil.rmtree(self.buildDir)

        os.mkdir(self.buildDir)

    def getSrc(self) -> None:
        srcDir = os.path.join(os.getcwd(), 'src')
        shutil.copytree(srcDir, os.path.join(self.buildDir, 'src'))