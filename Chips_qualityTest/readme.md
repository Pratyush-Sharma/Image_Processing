#Chips quality test

This project aimed on determining the quality of test 25 sample chips in an image i.e. determining whether they are fit for packing and selling based on spices(hazy red) colour intensity on plane(yellowish) potato chip.

## Code

- **colordetect.py** - Converted assign.jpg(sample) rgb image to hsv image and then using trackbar window for each parameter determined the color(hsv) range for creating a bitwise_and mask to identify and create contours.

- **contour_seperation.py** - Using trackar and mask limits, created and seperated contours using erosion, blurring, dilation and canny edge detector on test image.

- **finaltest.py** - Using the results from above two codes, seperated the contours on test image and then determined the area with higher red color intensity on each contour. Finally, the ratio of red and yellowish color intensity area was compared with the threshold of 0.68 to determine the quality of chips.
