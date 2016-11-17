# Histogram Equalization
## Variables
* count -> the total number of every grey scale in the input image
* accuRatio -> the accumulation ratio of every grey scale
* rows -> the height of the input image
* cols -> the width of the input image
* total -> the total number of pixels in the input image

## Algorithm Explanation
Histogram equalization is a technique for adjusting image intensities to enhance contrast.
Consider a discrete grayscale image {x} and let ni be the number of occurrences of gray level i. The probability of an occurrence of a pixel of level i in the image is ![](1.svg).
Count up every grey scale's ratio in the input image, sum up to get the **CDF**(Cumulative Distribution Function), then multiply 255 to find the corresponding grey scale value.
Eventually, write the dealt image to the disk.
