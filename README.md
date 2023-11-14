# Detection and recognition of basketball audio events
This repository contains a Python script(nn_thesis_final_draft) for Audio Event Detection (AED) using Artificial Neural Networks (ANN) and Convolutional Neural Networks (CNN). The pipeline includes data loading, preprocessing, model preparation, training, and testing.

## Model Preparation
This section prepares the data for model training. It includes data augmentation, feature extraction, frame labeling, window creation, window labeling, and feature selection.

### Data Augmentation
The script uses audiomentations library for dynamic range compression to augment the audio signals.

### Audio Representation(Feature and Mel Spectrograms Extraction)
Features are extracted from the audio signals, including MFCCs, spectral centroid, zero-crossing rate, chroma, spectral flatness, spectral rolloff, RMS, spectral contrast, spectral bandwidth, linear predictive coding (LPC), and linear prediction cepstral coefficients (LPCC). Also, mel spectrograms are extracted for comparison with features.

### Frame Labelling
Frames are labeled based on the provided CSV files.

### Feature Time Integration(FTI)
Windows of consecutive frames are created using feature stacking and feature statistics(mean, variance, median).

### Windows Labelling
Windows are labeled using majority voting or weighted voting based on frame labels.

### Feature Selection
Features are selected based on Pearson correlation and mutual information.

## Artificial NN
This section defines an Artificial Neural Network (ANN) model using TensorFlow/Keras.

## CNN
This section defines a Convolutional Neural Network (CNN) model using TensorFlow/Keras.

## Load Data and Model
This section includes functions to get final data for training and testing and load the final model.

## Get Final Data for Training and Testing
This function loads, preprocesses, and augments audio signals, extracts features, and creates windows for training and testing.

## Load Final Model
This function loads the final model based on the chosen audio representation and neural network architecture.

## Main
The main function orchestrates the entire training and testing process. It prints training metrics, plots loss and accuracy curves, and displays a confusion matrix for testing results.
