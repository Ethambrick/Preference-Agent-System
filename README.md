PrefAgent – Preference Agent System
CAP4630 Project 3 – Spring 2026
Author: Ethan Hambrick

This program implements a preference agent that models and solves preference problems using penalty logic and qualitative choice logic. It reads attributes, constraints, and preference rules from text files and allows the user to perform reasoning tasks through a menu interface.

Requirements
Python 3.11

How to Run
Run the program from the project root directory with:
python main.py

Project Structure
src/ contains all source code files
ExampleTestCase/ contains the provided example input files
TestCase/ contains the custom test case
README contains instructions
report.pdf contains the project report

Supported Tasks
The program supports encoding all objects, checking feasibility, displaying tables of feasible objects, comparing two objects, and finding all optimal objects.

File Formats
Attributes file uses the format: attribute: value1, value2
Constraints file contains CNF clauses using NOT and OR
Penalty logic file contains formulas with penalties
Qualitative logic file contains rules using BT and IF

No additional libraries are required.
