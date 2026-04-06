# truss_calculator
## About this project
Just a simple truss calculator :)
This is my first attempt at seriously writing OOP code, so things may be quite messy and definitly not perfect. However, it works and that is all that matters. 

## Use
Edit the "defineObjects()" function in th define file. You can then run the program through the main file; when running the file, there will be a visualiser that you can close by clicking on and the exact values will be displayed on the console.
There are a few objects that can be difined. The primary ones are: Node, MemberForce, SupportForce and LoadForce.
### Node
Nodes are where the truss members will connect. Define them with a name and their x-y coordinate.
### MemberForce
MemberForces are the forces placed onto the truss. Define them with a name and their parent nodes.
### SupportForce
SupportForces are the forces at the support. Currently, there can only be forces in the x-y directions (there are no moment reactions). Define them with a name, their parent node and the axis that they are on.
### LoadForce
LoadForces are loads placed onto a node. Define them with a name, parent node, magnitude and angle direction from the x-axis.
