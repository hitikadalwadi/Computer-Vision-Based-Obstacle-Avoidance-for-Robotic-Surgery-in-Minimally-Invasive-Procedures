# Computer Vision-Based Obstacle Avoidance for Robotic Surgery in Minimally Invasive Procedures

## Overview

This project implements a computer vision system designed to enhance surgical precision and safety in minimally invasive robotic procedures. The system utilizes advanced image segmentation techniques to provide real-time instrument tracking and collision avoidance capabilities for surgical robotics.

## Features

- **Real-time Instrument Detection**: Accurately identifies and tracks surgical instruments in live video feeds
- **Semantic Segmentation**: Utilizes U-Net architecture for precise medical equipment segmentation
- **Collision Avoidance**: Provides distance calculations and spatial awareness to prevent instrument collisions

## Technical Implementation

### Computer Vision Pipeline
- **Feature Extraction**: Leverages DeepLabCut for robust feature identification
- **Image Segmentation**: Implements U-Net neural networks for precise instrument boundary detection
- **Contour Analysis**: Processes segmented images to identify instrument contours and centroids
- **Spatial Mapping**: Generates bounding boxes and calculates distance metrics from camera perspective

### Dataset and Training
- **Training Data**: TF-Cholec80 dataset for comprehensive medical equipment recognition
- **Model Performance**: Achieves 90-95% accuracy in instrument segmentation
- **Model Output**: `Semantic_instrument_seg.h5` trained model for deployment

### Real-time Processing
- Continuous video frame analysis for dynamic surgical environments
- Low-latency processing for immediate feedback to surgical systems
- Robust performance in challenging lighting and viewing conditions typical of minimally invasive procedures

## Applications

- **Minimally Invasive Surgery**: Enhanced precision for laparoscopic and endoscopic procedures
- **Remote Surgery**: Enables telesurgery applications in remote or high-risk environments
- **Surgical Training**: Provides objective feedback for surgical skill development

## Technology Stack

- **Programming Language**: Python
- **Computer Vision**: OpenCV, DeepLabCut
- **Deep Learning**: TensorFlow/Keras, U-Net architecture
- **Image Processing**: Custom segmentation and contour detection algorithms
- **Machine Learning**: Semantic segmentation models

## Key Benefits

- **Improved Safety**: Real-time collision detection and avoidance
- **Enhanced Precision**: Accurate instrument localization and tracking

## Future Development

This system represents a significant advancement in surgical robotics, offering the potential to make minimally invasive surgery safer, more precise, and more accessible. The technology provides a competitive alternative to conventional surgical approaches while maintaining high standards of patient care and surgical outcomes.

# Project Supervision
**Dr. Kunal Korgaonkar**
Lead of Confluence Lab
Asst Prof, CSIS, BITS-Goa 

## Contributing

This project contributes to the advancement of medical robotics and computer vision applications in healthcare, with potential for significant impact on surgical safety and accessibility worldwide.
