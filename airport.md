# Piyush Khushlani
# 15ME30057
## 1st Projection Matrix

### Requirements

This program uses a number of open source libraries to work properly:

* [OpenCV](https://opencv.org/) - Open Source Computer Vision Library
* [Tkinter](https://wiki.python.org/moin/TkInter) - Graphical User Interface
* Standard Python Libraries.

### Instructions

  - To run program, open terminal to run "airport.py"
  - Open image in the folder you want to perform calculations
  - Please follow the commands on terminal to get respective values and thus, get the Projection Matrix


A test case is solved and output is given below.
> Note:  The selected modules in requirement section may not work properly for some PCs. Please get back to me in that case
### Calculations
> The main part of calculation is to solve for Linear Equations to find the co-efficient of the Projection Vectors.
> Calculation of co-efficients will occur after you will select the final middle point of Airplane.
### Test Output

```sh
$ python airport.py 
Please select 2 sets of two points in X, Y and Z axes of World Co-ordinate
Clicked Pixel : (985, 369)
Clicked Pixel : (1078, 366)
length in pixels between two image points = 93.04837451562494
Clicked Pixel : (984, 340)
Clicked Pixel : (1089, 338)
length in pixels between two image points = 105.01904589168576
Line1 = [-2, -105, 37668]
Line2 = [-3, -93, 37272]
Line1xLine2 = [-410436, -38460, -129]
Vanishing point = [3181.6744186046512, 298.13953488372096]
Clicked Pixel : (719, 272)
Clicked Pixel : (716, 196)
length in pixels between two image points = 76.05918747922567
Clicked Pixel : (1150, 723)
Clicked Pixel : (1153, 600)
length in pixels between two image points = 123.03657992645927
Line1 = [-123, -3, 143619]
Line2 = [-76, 3, 53828]
Line1xLine2 = [-592341, -4294200, -597]
Vanishing point = [992.1959798994975, 7192.964824120603]
Clicked Pixel : (480, 591)
Clicked Pixel : (525, 499)
length in pixels between two image points = 102.41581909060729
Clicked Pixel : (736, 615)
Clicked Pixel : (707, 521)
length in pixels between two image points = 98.37174391053561
Line1 = [-94, 29, 51349]
Line2 = [-92, -45, 70755]
Line1xLine2 = [4362600, 1926862, 6898]
Vanishing point = [632.4441867207886, 279.3363293708321]
Select two pairs of wheels to calculate px/meter
Clicked Pixel : (626, 340)
Clicked Pixel : (709, 339)
length in pixels between two image points = 83.00602387778854
Assuming World Origin and Center at (0,0,0) which last column of Projection Matrix

Select middle point on the nearest Airplane.
Clicked Pixel : (685, 315)


##Projection Matrix##

[0.26764516962491608, 0.046564543375749994, -4.110885698469934, 0]
[0.025079752321371107, 0.33757153761793562, -1.8156854716740416, 0]
[8.4120854120043492e-05, 4.6930792221579705e-05, -0.0064999976041914464, 0]
```
For more, see my [Github](https://github.com/SinghamSonia).
### Thank You
