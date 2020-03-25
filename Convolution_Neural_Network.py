# Convolution Neural Network: Notes
# CNN are for computer vision; they classify images, photographs and videos.

# Building the CNN
# Sequential - Initialise the ANN as it is a sequence of layers
# Convolution 2D - The Convolution step: Adding convolution layers
# Maxpooling 2D - Pooling the layers
# Flatten - The Flattening step, where we convert the pooled feature map to input into the ANN
# Dense - Add layers to the ANN

import keras
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN

classifier = Sequential()

# Step 1 - Convolution
# We have 32 feature detectors (feature maps) of dimension 3X3
# input_shape: We want 64X64 pixels (128X128 and 256X256 will take too long), 3 is the number of channels as we want a colour map (1 channel B&W Image)
# Activation function is relu (ReLU: Rectified Linear Units) to avoid negative pixels for non-linearity

classifier.add(Convolution2D(32, (3, 3), input_shape = (64,64,3), activation = 'relu'))

# Step 2 - Max Pooling
# Reducing the size of the feature map by dividing it by 2

classifier.add(MaxPooling2D(pool_size = (2,2)))

# Adding a second convolutional layer
# Making a deeper neural network, increasing the accuracy of our model substantially. If desired, we can add a third layer with 64 detectors.
classifier.add(Convolution2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening

classifier.add(Flatten())

# Step 4 - Full Connection
# Units = 128 is from trial and error, it is seen to be a good number for neural networks. It is usually a power of 2

classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN
# If we had multiple outputs, our loss = 'categorical_crossentropy'

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the CNN to the images (Image Augmentation)
# We apply Image Augmentation when our image sample size is low. We get the code from keras.io

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                   target_size=(64, 64),
                                                   batch_size=32,
                                                   class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                             target_size=(64, 64),
                                             batch_size=32,
                                             class_mode='binary')

classifier.fit_generator(training_set,
                         steps_per_epoch = 8000,
                         epochs = 25,
                         validation_data = test_set,
                         validation_steps = 2000)