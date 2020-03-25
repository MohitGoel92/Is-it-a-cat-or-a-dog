# Is it a cat or a dog?

We will be using a "Convolution Neural Network" to classify images of dogs and cats

## Convolution Neural Networks

Convolution Neural Networks (CNN) are most commonly applied to analysing visual imagery or "Computer Vision". An image is used as an input, it is processed through the CNN and the output label gives us a probability of which class the image belongs to. In short there are 4 steps to this, they are:
- Convolution
- Max Pooling
- Flattening
- Full Connection

### Step 1: Convolution

In this step, we find features in our image using the "Feature Detector" and put them into a "Feature Map". This relationship is given below.

<img src = 'Screen1.png' width='300'>

**Convolution summary**

- The Feature Detector is used to detect certain features and the Feature Map captures key features. 
- The Feature Map preserves key features and discards unnecessary information.
- This process makes the image smaller, resulting in faster processing.
- When applying the feature detector we lose some information as we have less values in the resulting matrix. However, the purpose of the Feature Detector is to detect certain features or integral parts of the image.
- The higest number in our Feature Map is when the pattern matches up.
- We have a perfect match when: 
  - The sum of the Feature Detector = Number in the square (cell) of the Feature Map
- The Feature Map captures/preserves key features we look out for and discard unnecessary information that does not help us determing the image.
