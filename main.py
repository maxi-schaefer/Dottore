# @author: gokimax
# Created: 4/28/2024
#######################################################################################
# All the imports needed
import sys
import click
import logging
import pyfiglet
import requests
import fileinput
from utils.build import Build
from rich.console import Console
from utils.makeenv import MakeEnv
from rich.logging import RichHandler
from utils.obfuscate import DoObfuscate

#######################################################################################
# Replace all occurences in an file
def replaceAll(file: str, searchExp: str, replaceExp):
    """
    Replace all occurences in an file
    """
    for line in fileinput.input(file, inplace=1, encoding="utf-8"):
        if(searchExp in line):
            line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)

#######################################################################################
# Github Stats Methodes
def getStars(repoURL: str) -> str:
    stars = requests.get(repoURL).json()["stargazers_count"]
    return stars

def getForks(repoURL: str) -> str:
    forks = requests.get(repoURL).json()["forks_count"]
    return forks

#######################################################################################
# Main Methode
def main():
    # Get GitHub Stats
    stars = getStars("https://api.github.com/repos/maxi-schaefer/Dottore")
    forks = getForks("https://api.github.com/repos/maxi-schaefer/Dottore")

    # Setup logger
    logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])])
    logging.getLogger("Rich")

    # Setup Console and print informations
    console = Console()
    console.print("\n")
    console.print(pyfiglet.figlet_format("Dottore", font="graffiti"), justify="center", highlight=False, style="cyan", overflow="ignore")
    console.print(f"Easy to use and open-source python builder. \nStars: {stars} | Forks: {forks}", justify="center", highlight=False, style="bold cyan", overflow="ignore")

    # Continue
    input("Press any key to start building...")

    # MakeENV setup
    makeEnv = MakeEnv()
    makeEnv.makeEnv()
    makeEnv.getSrc()

    # Obfuscate
    doObfuscate = DoObfuscate()
    doObfuscate.run()

    # Build
    build = Build()
    build.get_pyinstaller()
    build.get_upx()
    build.build("main.py")

if __name__ == "__main__":
    main()