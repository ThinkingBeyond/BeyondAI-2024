![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Geometric Clifford Algebra Networks in Robotics

## Project Description

Conventional methods for modeling the dynamics of robots often depend on intricate kinematic and dynamic equations. Geometric Clifford Algebra Networks (GCANs) have the potential to provide a more intuitive and efficient approach due to their ability to capture geometric transformations and relationships (Ruhe, 2023). This project aims to outline the problem, focusing on the creation and assessment of GCAN models for predicting the motion and forces exerted by robotic arms across various scenarios. Within the timeframe of the research stage, we focused on: 
1. Implementing a basic Geometric Clifford Algebra - Multi Layer Perceptron (GCA-MLP) in Python using clifford, cliffordlayers, etc. as per the structure introduced by Ruhe(2023).
2. Testing the GCA-MLP's performance on simple datasets such as MNIST and Iris, as well for trajectory prediction and implementing it in robot dynamics
3. Comparing its performance to an MLP and a CNN, including accuracy, loss over epochs, and time for convergence.

The project was built with the intention of understanding how well the implemented GCA-MLP learns and interprets spatial relationships, to use it in robotics - more specifically aerial robotics, we needed a clear intuition of the behavior of our MLP in various tasks.


### Technologies, Libraries and Datasets
1. **GCA-MLP** <br>
CliffordLayers - a type of neural network layers inspired by geometric Clifford algebras was used in implementing the MLP. The intention behind using CliffordLayers was the ability to expand operations such as convolutions and Fourier transforms over multivector fields (Microsoft Research, 2023).

2. **Tetris Trajectory Prediction** <br>
Draft 1 and draft 2 are both attempts to reproduce Ruhe's (2023) tetris trajectory application.

3. **Testing MNIST and IRIS** <br>
As apparent in the name, the MNIST and IRIS datasets were used for testing the MLP in 2d applications like image recognition, the datasets can be imported in Google Colab from Sklearn.

4. **Dummy Robot Application** <br>
The ARKOMA dataset for NAO robot arms was used here. The dataset is referenced, and can be downloaded from https://data.mendeley.com/datasets/brg4dz8nbb/1/files/8912a634-6f54-48db-9a97-67a782e49ff8

---

 # How to Install and Run the Project

 Run the provided .ipynb files in Google Colab!
 1. 

Generally, the GCA-MLP showed decent accuracy during testing (85%-90%), and low loss by the last epoch (0.5 by the 50th epoch in the robot dynamics experiment). However, the GCA-MLP consumes a considerable amount of time to converge. As addressed in the GCAN paper, the problem of higher computational density can be addressed by using hardware accelerators like GPUs. In scenarios which require a faster time for convergence such as robotic motion, we suspect that the model will require some form of modification. The Geometric Algebra Transformers (GATr) paper by Brehmer et al. appears to be a promising route for future research on geometric algebra in robotics.

> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
