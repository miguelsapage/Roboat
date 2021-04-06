# Roboat
This was my first project at school. This project got me into code!!
The program uses **graphics.py** and **button.py** from John M. Zelle. 

## Description
The Roboat is a cleaning bot that operates with the previews knowledge of the locations that need to be cleaned. This program has three implementations.

### GUI
Each implementation operates in a environment that has islands and a harbor, the roboat needs to circumvent the islands in order to clean the area. The three implementations can be accessed through a menu.

### 1st Implementation
On the first implementation, the user choose the location of the dirt that needs to be cleaned one at a time by clicking with the mouse than waits for place dirt on another point again.

### 2nd Implementation
On the second implementation, the user places as many dirt points as they want and then gives the command to clean the area by clicking on a button.

### 3rd Implementation
On the third implementation, the user can choose how the obstacles will be placed (by reading a file or random) and can choose where the dirt points will be (by reading a file or by mouse clicks), then the user gives the command to clean the area.

## Limitations
Sometimes the roboat jams on a island, and will ignore rectangular objects if placed by file on the third implementation. The speed of the roboat isn't linear since it's calculated each time it hit a island and the speed is based on the distance between the roboat and the dirt point.