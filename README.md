# Struct:
- Detection folder
- Drawing folder + arduino parser
- Other not interesting folders/files
- main.py
- BasicFunctions.py


### Detection folder
  There are all files which can detect anything
  
### Drawing folder
  Here is only one normal file, ParseArduino.py. Here you can set all arduino port names
  
### main.py
  It's main file for the project. Here you can set a model of an action. 
  In the variable with name "plan" you can configure the model. Just put there a list of commands in string format and separate it with "|"
  Here's a list of possible commands:
  - ```objects()``` **--> draw all detected objects**
  - ```marker()```  **--> draw ArUco markers**
  - ```qrcode()```  **--> draw qrcode markers**
  - ```bottles()``` **--> draw bottles only**
  - ```colors()```  **--> coming soon**

### BasicFunctions.py
  There are lots of custom function and nothing interesting.
