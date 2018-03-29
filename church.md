# Piyush Khushlani
# 15ME30057
## 2nd(Affine) Projection Matrix

### Requirements

This program uses a number of open source libraries to work properly:

* [OpenCV](https://opencv.org/) - Open Source Computer Vision Library
* [Tkinter](https://wiki.python.org/moin/TkInter) - Graphical User Interface
* Standard Python Libraries.

### Instructions

  - To run program, open terminal to run "church.py"
  - Open image in the folder you want to perform calculations
  - Please follow the commands on terminal to get respective values and thus, get the Projection Matrix


A test case is solved and output is given below.
> Note:  The selected modules in requirement section may not work properly for some PCs. Please get back to me in that case
### Calculations
> The main part of calculation is to solve for Linear Equations to find the co-efficient(lambda) of the Projection Vectors.
> Calculation of co-efficients will occur after you will select the two points across width of the Window Pane(9th Point) which solves for lambda(s) by simple linear equation.
### Test Output

```sh
$ python church.py 
Select 2 points in each direction x, y and z
Clicked Pixel : (795, 282)
Clicked Pixel : (833, 271)
length in pixels between two image points = 39.56008088970496
Line: [-11, -38, 19461]
Clicked Pixel : (957, 293)
Clicked Pixel : (977, 306)
length in pixels between two image points = 23.853720883753127
Line: [13, -20, -6581]
Clicked Pixel : (920, 299)
Clicked Pixel : (928, 385)
length in pixels between two image points = 86.37129152675674
Line: [86, -8, -76728]
Select corner point where two walls meet with the attic which will be image of World Origin
Clicked Pixel : (914, 196)
Select 2 points across width of windows on left wall from left to right to calculate px/meter
Clicked Pixel : (815, 428)
Clicked Pixel : (846, 421)


##Projection Matrix##

[-44.846505330677545, 47.74102765482496, 3.9987302291391384, 914]
[12.981883122038235, 31.031667975636225, 42.986349963245736, 196]
[0.0, -0.0, -0.0, 1]
```
For more, see my [Github](https://github.com/SinghamSonia).
### Thank You
