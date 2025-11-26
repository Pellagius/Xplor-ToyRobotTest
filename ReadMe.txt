____________________________________________________________________________________

Robot Test ReadMe

Hello, RobotTest is a python script implemtation and as such Python will be required to the run the main program and also the test target. Please install python3 using the following method based on your OS:

Python Installation

1. Ubuntu 
       	i) sudo apt update (to update your package list)
       	ii) sudo apt install python3

2. MacOS -  Please use Homebrew to install python, to install Homebrew please enter into Terminal:
 	i) /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	ii) Once the Homebreew installation is finished, in Terminal, type:
             
             brew install python

3. Windows 
	i) please go to https://www.python.org/downloads/windows/, and download the appropriate .exe for your machine/OS

____________________________________________________________________________________

Running RobotTestMain

In the folder called RobotTest you will find all necessary files. Please drag the folder RobotTest to wherever you would like, then navigate to this location in the Terminal/Command line. 

Enter the following command:

python3 RobotTestMain.py

____________________________________________________________________________________

Running RobotTestTests

From the same directory you have copied the RobotTest folder to in the above step, int the Terminal/Command Line please type:

python3 -m unittest -v test*.py

The project contains a total of 18 tests, covering a total of 3 files - MovementHandler, PlacementHandler and Helpers. 

These files are where the strong majority of business logic sits and no other part of the code is tested.
