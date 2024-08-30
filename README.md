# Pressure drop in pipe calculator
Video Demo:  https://youtu.be/uO5HB2q2REw
## Description:
Process engineers often need to design a flow of the fluid process. During this process in the real non-ideal world there is an energy loss in the fluid due to the friction with a pipe. This loss in energy is shown by the decrease in a pressure of the fluid. Sometimes it is very important for an engineer to contain a specific pressure inside the reactor, so they need to know how much of a pressure is lost while the fluid flows in a pipe. This pressure decrease is called a pressure drop.

This program calculates the pressure drop in the fluid flowing in a horizontal pipe due to friction.
### A file project.py is the main program
The function get_info() asks user for the length, diameter, and surface roughness of the pipe. It also asks for the flow rate, density and viscosity of the fluid. If the values are non-positive the code raises an exception.

The function q_to_v(Q, D) gets the flow rate and a pipe diameter and then converts flow rate of the fluid to its velocity.

The function Re(Rho, Mu, V, D) gets density, viscosity, and velocity of the fluid with the diameter of the pipe. Then it returns Reynold's number. If Reynold's number is not suitable for the model approximation, the program raises an exception.


The function fric_coef(Re, K, D) gets Reynold's number, surface rougness and diameter of the pipe, then calculates and returns the friction coefficient. If the ratio of the surface roughness to the diameter of the pipe is not suitable for the model approximation, the program raises an exception.

The function h_f(F, V, L, G, D) gets the friction coefficient, velocity of the fluid, length of the pipe, standard gravity, and the diameter of the pipe. Then it returns the pressure drop due to friction in a pipe.

The main function calls these functions one by one, and then prints the pressure drop in two different units (Pa and atm), and the friction coefficient.
## A file test_project.py is a test for the main program
The file consists of 4 functions: test_q_to_v(), test_Re(), test_fric_coef(), test_h_f(). Each function checks the values provided by a fitting function in project.py.
## Possible improvments to the code (TODO list):
- Adding the difference in the height between the start and the end points of the flow, so the program can work not only for the horizontal pipes.
- Adding the possibility to add different additional parts of the pipes as turns, elbows, etc. which also cause pressure drop in the flow.
- Creating a user-friendly design.
- Creating a unit conversion calculator and implementing inside the program, so an engineer can enter the variables in the preferable units and the result in desired units.
- Adding possibility to find the end point pressure by entering the start point pressure in addition to pressure drop.
## Example of the usage:
### Input:
What is the density of the fluid? [kg/m^3] 998

What is the dynamic viscosity of the fluid? [Pa*sec] 0.001

What is the flow rate of the fluid? [m^3/sec] 1

What is the length of the pipe? [m] 10

What is the diameter of the pipe? [m] 0.1

What is the surface roughness of the pipe? [m] 0.0009

### Output:
The pressure drop is estimated to be 3023.81 [Pa] or 0.0298 [atm].

While the friction factor is estimated to be 0.03656.
