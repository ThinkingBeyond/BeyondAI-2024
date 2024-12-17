![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Geometric Clifford Algebra Networks in Robotics

## Project Description

Conventional methods for modeling the dynamics of robots often depend on intricate kinematic and dynamic equations. Geometric Clifford Algebra Networks (GCANs) have the potential to provide a more intuitive and efficient approach due to their ability to capture geometric transformations and relationships (Ruhe, 2023). This project aims to outline the problem, focusing on the creation and assessment of GCAN models for predicting the motion and forces exerted by robotic arms across various scenarios. Within the timeframe of the research stage, we focused on: 
1. Implementing a basic Geometric Clifford Algebra - Multi Layer Perceptron (GCA-MLP) in Python using clifford, cliffordlayers, etc. as per the structure introduced by Ruhe(2023).
2. Testing the GCA-MLP's performance on simple datasets such as MNIST and Iris, as well for trajectory prediction and implementing it in robot dynamics
3. Comparing its performance to an MLP and a CNN, including accuracy, loss over epochs, and time for convergence.

The project was built with the intention of understanding how well the implemented GCA-MLP learns and interprets spatial relationships, to use it in robotics - more specifically aerial robotics, we needed a clear intuition of the behavior of our MLP in various tasks.

### Technologies, Libraries and Datasets
1. **Required Downloads and Imports** <br>
This .ipynb file contains requires all imports and downloads which are needed to run the program on Google colab, it is essential to run this code block on Colab for the rest of the code to work.

3. **GCA-MLP** <br>
CliffordLayers - a type of neural network layers inspired by geometric Clifford algebras was used in implementing the MLP. The intention behind using CliffordLayers was the ability to expand operations such as convolutions and Fourier transforms over multivector fields (Microsoft Research, 2023).

4. **Tetris Trajectory Prediction** <br>
Draft 1 and draft 2 are both attempts to reproduce Ruhe's (2023) tetris trajectory application.

5. **Testing MNIST and IRIS** <br>
As apparent in the name, the MNIST and IRIS datasets were used for testing the MLP in 2d applications like image recognition, the datasets can be imported in Google Colab from Sklearn.

6. **Dummy Robot Application** <br>
The ARKOMA dataset for NAO robot arms was used here. The dataset is referenced, and can be downloaded from https://data.mendeley.com/datasets/brg4dz8nbb/1/files/8912a634-6f54-48db-9a97-67a782e49ff8

---

 ## How to Install and Run the Project
 Run the provided .ipynb files on Google Colab in the following order:
 1. Required Downloads and Imports
 2. GCA-MLP
 3. Tetris Object Trajectory Draft 1
 4. Tetris Object Trajectory Draft 2
 5. Testing IRIS (Optional)
 6. Testing MNIST (Optional)
 7. Dummy Robot Application

---

## Known Issues 
We were not able to reproduce Ruhe's (2023) tetris object trajectory application, as the predicted trajectory deviates from the actual trajectory about halfway along the path

![Screenshot 2024-12-04 133125](https://github.com/user-attachments/assets/a36b0ca2-ab33-49a1-8fee-5871143063d8)

---

## Credits
**Student Researchers:** Loulia Jaafari, Warenya Ranmini
**Mentors:** Dr.Filip Bar

---

## Conclusion and Future Work
Generally, the GCA-MLP showed decent accuracy during testing (85%-90%), and low loss by the last epoch (0.5 by the 50th epoch in the robot dynamics experiment). However, the GCA-MLP consumes a considerable amount of time to converge. As addressed in the GCAN paper, the problem of higher computational density can be addressed by using hardware accelerators like GPUs. In scenarios which require a faster time for convergence such as robotic motion, we suspect that the model will require some form of modification. The Geometric Algebra Transformers (GATr) paper by Brehmer et al. appears to be a promising route for future research on geometric algebra in robotics.

---

## References
1. Bár, F. (2011) On the Foundations of Geometric Algebra. Diploma thesis, LMU Munich.
2. Brehmer, J., de Haan, P., Behrends, S., & Cohen, T. (2023). Geometric algebra transformer. NeurIPS 2023. https://arxiv.org/abs/2305.18415
3. Hitzer, E., Nitta, T., & Kuroe, Y. (2013). Applications of Clifford's geometric algebra in robotics. Advances in Applied Clifford Algebras, 23(3), 377-404.
4. Ruhe, D., Gupta, J. K., de Keninck, S., Welling, M., & Brandstetter, J. (2023). Geometric Clifford algebra networks. arXiv preprint arXiv:2302.06594.
   
> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
