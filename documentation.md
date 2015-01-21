AMS Robot Documentation
=======================

Introduction
------------
This documentation is covering our research and implementation for our own autonomous robot. The idea was to walk through all the necessary steps to build an autonomous robot which is solving a predefined problem. The following section will cover our problem definition and the goals, we would like to achive at the end of our build.

### Problem Definition and Goals

The robot should solve the following problem: A colored ball should be found and moved to a colored square. 

We need to define some constraints for this problem definition, so that it gets simplified to an actual solvable task in the given time period. Both objects, the ball and the square goal, need to stay in places without any obstacles between the robot and itself. The surrounding area need to be a laboratory environment without any optical confusion or moving objects. There should also be a predefined and decent amount of light without any colored impact.

Our goal for the constrained task is to build a robot, which is solving this problem without time limits. But it should solve this problem autonomously.


Theoretische Vorbemerkung
-------------------------
*Hardware Basis(jojo)
*Pi
*Camera
*Schrittmotoren(Vollschritt/Halbschritt) Technische Details
*Energy+Communication

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

