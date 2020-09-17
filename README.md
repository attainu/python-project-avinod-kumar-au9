# Parking Lot Problem

## About Problem

#### To design a parking lot system with ability to find:
* Registration numbers of all cars of a particular colour.

* Slot number in which a car with a given registration number is parked.

* Slot numbers of all slots where a car of a particular colour is parked.

## Pre requisites
The source code for this project is written using python 3.8 .Make sure you have python 3.8 installed on your computer before running this application.

## How to run?
This is a console application written in python 3.8. This can be run in two modes:

Interactive Mode: An interactive terminal based shell where commands can be typed in to perform different actions.

File Mode: It accepts a filename as a parameter at the terminal and read the commands from that file.

## Quick Start
Proceed to the steps below only if you've python 3.8 installed. If not, please refer pre requisites section.

Run the code and choose your choice in terminal- interactive or file

#### For Interactive Mode

Type interactive

#### For File Mode
Type file  
And type your path of the file

## List of User Commands
Users can interact with the Parking Lot system via a following simple set of commands which produce a specific output:

* create_parking_lot < NUMBER OF SLOTS REQUIRED > : create_parking_lot 6 will create a parking lot with 6 slots

* park < REGISTRATION NUMBER > < COLOR > : park KA-01-HH-1234 White will allocate the nearest slot from entry gate.

* leave < SLOT NUMBER> : leave 4 will make slot number 4 free.

* status : status will display cars and their slot details
Slot No.  Registration No Color     
1         KA-01-HH-1234  White  
2         KA-01-HH-9999  Red    
3         KA-01-BB-0001  White   
5         KA-01-HH-2701  Black   
6         KA-01-HH-3141  Black

* registration_numbers_for_cars_with_colour < COLOR >: registration_numbers_for_cars_with_colour White will display the registration number of the cars of white color e.g. KA-01-HH-1234, KA-01-BB-0001

* slot_numbers_for_cars_with_colour < COLOR > : slot_numbers_for_cars_with_colour White will display slot numbers of the cars of white color e.g. 1, 3

* slot_number_for_registration_number < REGISTRATION NUMBER > : slot_number_for_registration_number MH-04-AY-1111 will display the slot number for the car with registration number MH-04-AY-1111

* exit : exit will quit the terminal and end the code execution

### NOTE: Any commands which are not mentioned above will throw an error: PLease enter a valid command



