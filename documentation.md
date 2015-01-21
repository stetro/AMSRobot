AMS Robot Documentation
=======================

Introduction
------------
This documentation is covering our research and implementation for our own autonomous robot. The idea was to walk through all the necessary steps to build an autonomous robot which is solving a predefined problem. The following section will cover our problem definition and the goals, we would like to achive at the end of our build.

### Problem Definition and Goals

The robot should solve the following problem: A colored ball should be found and moved to a colored square.

We need to define some constraints for this problem definition, so that it gets simplified to an actual solvable task in the given time period. Both objects, the ball and the square goal, need to stay in places without any obstacles between the robot and itself. The surrounding area need to be a laboratory environment without any optical confusion or moving objects. There should also be a predefined and decent amount of light without any colored impact. The environment is assumed to be more or less a circle (No corners the ball could be captivated in).

Our goal for the constrained task is to build a robot, which is solving this problem without time limits. But it should solve this problem autonomously.


Theoretical Introduction
-------------------------
### Used Hardware

#### Raspberry Pi

The project is based on a raspberry pi b+ as a electronic base unit. The raspberry pi is a single-board-computer. It is based on a system on chip from broadcom. It provides:
- 700Mhz CPU
- 512MB Ram
- 40 GPIO Pins
- SPI interface
- I2C interface
- 4 USB Host Interfaces
- 1 HDMI Interface
- 1 LAN Interface
- 1 CSI Camera connector

![Raspberry Pi](presentation/final/raspberry.png "Raspberry Pi")

We use Rasbian as an operating system. The rasbian OS is based on Debian an optimized for raspberry pi.

#### Pi Camera

For image caputuring we use the "[Kameramodul für Raspberry Pi](http://www.amazon.de/Kamera-Modul-f%C3%BCr-Raspberry-Pi/dp/B00E1GGE40)"
It has a 5 Mega-Pixel image sensor and offers a maximal resolution of 2592 x 1944 Pixel for image processing.
It can be attached to the Raspberry Pi via the CSI Camera connector. It can be accessed via python. Further details about the programming can be found in the Used Software Chapter.

<img src="presentation/final/picamera.jpg" alt="Drawing" style="width: 200px;"/>
[src](http://www.amazon.de/28BYJ-48-28BYJ48-4-Phase-Arduino-Stepper/dp/B00ATA5MFE)

#### Stepper Motors

To Move the Robot we decided to use stepper motors. Stepper motors are synchronous motors driven by a controlled stepwise rotating electromagnetic field.
We decided to use stepper motors to avoid the necessarity of a seperate controlling unit that takes care for both wheels turing in the same speed.
The 4-phases-synchron-motor is delivered with an motor driver module. the purpose of the driver module is to support the motor with an external power supply.
the 4 phases of the driver module are attached to GPIO Pins of the Raspberry Pi.




The choosen stepper motor 28BYJ48 is an unipolar stepper motor. According to the schematic below it has 5 wires. one wire is connected to +5V the others dependent on the Step to +5V or 0V According to the following table. This is the so called full-Step mode.



| Step | A | B | C | D |
|------|---|---|---|---|
| 1    | + | + | 0 | 0 |
| 2    | 0 | + | + | 0 |
| 3    | 0 | 0 | + | + |
| 4    | + | 0 | 0 | + |

<img src="presentation/final/unipolar-stepper.jpg" alt="Drawing" style="width: 200px;"/>
[src](http://de.wikipedia.org/wiki/Schrittmotor#mediaviewer/File:Stepmotscheme.jpg)


* Hardware Basis(jojo)
* Pi
* Camera
* Schrittmotoren(Vollschritt/Halbschritt) Technische Details
* Energy+Communication

### Used Software

The mentioned raspberry pi is running different linux distributions such as Raspbian (based on debian), Pidora (based on Fedora) or Arch Linux and more. (http://www.raspberrypi.org/downloads/) The most spreaded and used distribution is Raspbian. It offers all the, in our case, used libraries in a prebuild format.

Depending on the Linux-based board, there are no limits to a used programming language. Many documentations about the controlling and usage of the raspberry pi are based on the Python programming language. In addition because of personal experiences we decided to use Python for this implementation.

##### Image processing with OpenCV

We will implement the ball detection with OpenCV. This library is designed for computational efficient and with a focus on real-time image processing because it can take advantage of the hardware acceleration.(http://opencv.org/) It is splitted in subprojects like the image feature recognition, image stitching or visualisation. We will mainly focus on the subprojects for image processing and video analysis to detect the two problem objects. OpenCV also offers programming interfaces for

##### Modelling with OpenSCAD



Umsetzung
---------
*Konstruktion(Jojo)
*Iterationen(Zahnräder)
*SCAD-STL-GCODE Workflow
*Slic3r

*Software(Steffen)
*Bildverarbeitung (Objekterkennung mit HSV ...)
*Klassendiagramm
*Schrittmotoren
*Zusammenspiel

Evaluation(Jojo)
----------
*Ziele erreicht?
*Bilderreihe
*Kritik (RPI? ok?) ...
*RPI Schrittmotor Kritik

Ausblick (STeffen)
--------
*Threading
*ROS
