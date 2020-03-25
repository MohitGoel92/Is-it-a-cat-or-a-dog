# Is it a cat or a dog?

We will be using a "Convolution Neural Network" to classify images of dogs and cats

## Convolution Neural Networks

Convolution Neural Networks (CNN) are most commonly applied to analysing visual imagery or "Computer Vision". An image is used as an input, it is processed through the CNN and the output label gives us a probability of which class the image belongs to. In short there are 4 steps to this, they are:

- Convolution + ReLu layer
- Max Pooling
- Flattening
- Full Connection

### Step 1: Convolution

In this step, we find features in our image using the "Feature Detector" and put them into a "Feature Map". This relationship is given below.

<img src = 'Screen1.png' width='600'>

**Convolution summary**

- The Feature Detector is used to detect certain features and the Feature Map captures key features. 
- The Feature Map preserves key features and discards unnecessary information.
- This process makes the image smaller, resulting in faster processing.
- When applying the feature detector we lose some information as we have less values in the resulting matrix. However, the purpose of the Feature Detector is to detect certain features or integral parts of the image.
- The higest number in our Feature Map is when the pattern matches up.
- We have a perfect match when: 
  - The sum of the Feature Detector = Number in the square (cell) of the Feature Map.
- The Feature Map captures/preserves key features we look out for and discards unnecessary information that does not help us determine the image.

### ReLu Layer

ReLu stands for "Rectified Linear Units", which is the Rectifier Activation function. This is an additional step to the convolution step. We apply the Rectifier as we want to increase non-linearity in our image/CNN. This is due to images being highly non-linear as there may be different objects next to each other or in the background. The diagram below shows the ReLu function: f(x) = max(x,0), in comparison to the softplus function.

<img src = 'Screen2.png' width='700'>

### Step 2: Max Pooling

<img src = 'Screen3.png' width='600'>

In this step, we eliminate further unnecessary data by "Max Pooling". 

**Max Pooling summary**

- We place a 2x2 box on top of the Feature Map and select the largest number in the 2x2 box, and enter it into the "Pooled Feature Map".
- This gets rid of 75% of the information that is not feature data, therefore no longer requiring this data.
- We now introduce spatial invariance: As we're taking the maximum of the values, we're taking into consideration any distortions. For example, in the Feature Map if the distinctive feature we're looking out for is a position different to the expected Feature Map, the maximum number will be in the same position in the Pooled Feature Map. Note: Any vaguely similar features will not score high enough.
- We have reduced the number the number of parameters that will go into the final layers of the Neural Network. This prevents overfitting of current information as we should only be feature based.


### References

Online latex editor: https://www.codecogs.com/latex/eqneditor.php

ReLu Graph: https://en.wikipedia.org/wiki/Rectifier_(neural_networks)#/media/File:Rectifier_and_softplus_functions.svg
