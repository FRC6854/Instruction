# VIKING Instruction Sytntax
NOTICE: Still being drafted, final idea will be different.  

Universal Syntax for deploying future robot code.
```
0 goto 0
1000 goto ~ 500
5000 goto 20 60
8000 stop
```
## Clock Cycle
The clock cycle is what executes commands. All commands are asynchronous and are loaded in via Viking. Commands will be executed by the badge, the badge is a number coralating to when the command should be executed. Badges are in mileseconds (1000:second).

## Universal Functions
### Goto Function
Flags
```
{badge} goto {x} {y}
```
### Rotate Function
Flags
```
{badge} rotate {degrees (clockwise)}
```
Swerve can use built in movement but other deployments can rotate to next movement.

# Variables
## ~ Constant
Use current variable, a example is ~ in a x function meaning no movement.
