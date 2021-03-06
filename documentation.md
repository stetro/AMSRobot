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
| 1    | + | 0 | 0 | 0 |
| 2    | 0 | + | 0 | 0 |
| 3    | 0 | 0 | + | 0 |
| 4    | 0 | 0 | 0 | + |

But we also implemented the possibility to use Half-Step-Mode. In Half-Step-Mode the time consumed to make one rotation of the wheel is double the time than the one in Full-Step-mode. But on the other hand the torque in Full-Step-Mode is lower. So in Full-Step-Mode there is a higher risk to lose steps. Steps are lost if the tork is not sufficient to turn the motors axis sufficiently far. Because the torque on our wheels is sufficient in Full-Step-Mode and we wanted to let the robot move a bit faster, we choose Full-Step-Mode.

| Step | A | B | C | D |
|------|---|---|---|---|
| 1    | + | 0 | 0 | 0 |
| 2    | + | + | 0 | 0 |
| 3    | 0 | + | 0 | 0 |
| 4    | 0 | + | + | 0 |
| 5    | 0 | 0 | + | 0 |
| 6    | 0 | 0 | + | + |
| 7    | 0 | 0 | 0 | + |
| 8    | + | 0 | 0 | + |



<img src="presentation/final/unipolar-stepper.jpg" alt="Drawing" style="width: 200px;"/>
[src](http://de.wikipedia.org/wiki/Schrittmotor#mediaviewer/File:Stepmotscheme.jpg)

The Energy-Supply of the Raspberry Pi is provided by an external power source. It is attached to the Raspberry Pi and the also directly to the stepper motor driver. we chose this wiring because the pins of the raspberry pi can not provide sufficient amount of energy for the stepper motors.

#### WLAN


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



Implementation
--------------
We completely designed the robot from scratch.
This was only possible to do because we had access to a 3D-Printer. Even though 3D-Printers are already used since many years for rapid prototyping, they just became affordable to a broader public just within the last few years.

### Used 3D-Printer
We used a 3D-Printer using the Fused Deposition Modeling Method. This kind of 3D-Printer melds some kind of plastic-filament by simlpy heating it to 200-220*C. the heated filament is extruded and the object is created layer by layer


*Konstruktion(Jojo)
*Iterationen(Zahnräder)
*SCAD-STL-GCODE Workflow
*Slic3r



## Software

This subsection will present our python based implementation in detail. It shows the structure and the use of the mentioned framework in this project.

### Project Structure
Our project structure is quite simple and is shown in the following class diagram. There is one inheritence shown between the Detection and the two childs SquareDetection and CircleDetection. Detection is generalizin the whole access to the camera module and ech child is running the specific image processing, described in the following chapter. ![image](ClassDiagram.jpg)

### Imageprocessing with OpenCV

#### Circle Deteciton
#### Square Detection


### Addressing Steppermotors

Each steppermotor has 4 input wires (A to D) to control the step movement of the inner restricted rotor. There are different modes to use a stepper motor which will effect the movement speed and torque. The first four colums are showing fullstep mode which will run fast with less torque. The second part is showing halfstep mode which will run fast but with less torque.

|       | A | B | C | D |   | A | B | C | D |
|-------|---|---|---|---|---|---|---|---|---|
| **1** | 1 | 0 | 0 | 0 |   | 1 | 0 | 0 | 0 |
| **2** | 0 | 1 | 0 | 0 |   | 1 | 1 | 0 | 0 |
| **3** | 0 | 0 | 1 | 0 |   | 0 | 1 | 0 | 0 |
| **4** | 0 | 0 | 0 | 1 |   | 0 | 1 | 1 | 0 |
| **5** |   |   |   |   |   | 0 | 0 | 1 | 0 |
| **6** |   |   |   |   |   | 0 | 0 | 1 | 1 |
| **7** |   |   |   |   |   | 0 | 0 | 0 | 1 |
| **8** |   |   |   |   |   | 1 | 0 | 0 | 1 |

In this project we don't needed to have too much torque and therefor we decided to use fullstep to gain a little bit more speed. The detailed pin addressing is happening in the Stepper class and it can handle both modes, depending on the input values from our Driver class.

### Zusammenspiel

The following image is showing the state mashine our implementation. It shows the two main loops for the circle or squardetection and also the decision situation for the driver controller. Each image capturing process is coming from one of the both detection implementation and each movement-sequenz is going to the diver instance d.

![image](presentation/final/process.png)


Evaluation
----------
Our aim was to build an robot that can find a colored ball and move it to a colored square.

As a result of this course our final robot is able to fulfill that aim unter the given constraints (see Chapter: Problem Definition and Goals).

In the folowing sequence of images you see the robot searching and and finding the ball. Driving to the ball and then switching to square-detection mode. Searching and finding the colored square and then driving and finally reaching the goal.

![image]()

Even though the robot reached the defined goal, it doesn't solve it very quickly. One reason is that the choosen stepper motors. Even in full-step-mode they don't turn the wheel faster than about 3/5 cm per second.

Usage
-----

To install and use our implementation you need to install some necessary libraries for the raspbian operating system. All of them are prebuild and can be installed with the package control as following:

```
sudo apt-get install libopencv-dev python-opencv
sudo apt-get install python-setuptools
easy_install --user picamera
```

To run the project code you also need to have a working raspberrypi camera. To check if an attached camera is working properly, the following command is capturing a sample photo:

```raspistill -o cam.jpg```

This is the actual python command to start the robot. Root rights are needed to be able to control GPIO pins for the steppermotors.

```sudo python main.py```





Conclusion
----------

Our main problem for this hardware and software decision is performance as we reached a feedback loop time of round about 5 seconds. This is quite a long time and is caused by the calculation speed of the Raspberry Pi during the image processing. Of cause, speed wasn't the main goal for this project, thus we could actually tweak and change our implementation to gain some performance improvements. But still, there would be a big delay during the image processing.

To solve this issue we thought about outsourcing of the computationally intensive image processing. One way to do this is the ROS - Robot Operating System which will be shortly introduces in the following chapter.

## ROS
