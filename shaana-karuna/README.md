![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# An Elementary Proof of the Universal Approximation Theorem for Multilayer Perceptrons

## Research question 
Our research question was to expand on Nielsen's proof for the **Universal Approximation Theorem for Multilayer Perceptrons** which he provided in his online textbook, Neural Networks and Deep Learning[^1]. We showed that any **continuous function** on the real numbers can be approximated by a **Multilayer Perceptron** (MLP) with several hidden layers and a finite number of neurons, using the **sigmoid** activation function. We also proved that **piecewise functions**, constructed using MLPs with **ReLU** activation, can also approximate any continuous function. Our aim was that our proof would be intuitive and easy to understand, and would use visualisations to help the reader grasp the concepts being used.

## Motivation 
The universal approximation theorem states that a **Multilayer Perceptron** with a finite number of neurons and a single hidden layer can approximate any **continuous function**. The original proofs of the universal approximation theorem involve **advanced mathematics** such as the Hahn-Banach theorem, the Riesz Representation theorem, Fourier analysis and the Stone-Weierstrass theorem, which the majority of people would not be able to understand fully. Therefore, our motivation for this research project was to construct an **elementary** proof of a similar result.

## Breakdown of proof
To begin our project, we carefully worked through Nielsen's proof and broke it down into smaller proofs. Although these sections relied on each other, we were able to deal with them individually by assuming that the earlier proofs were true. These subdivisions were as follows:

1. The **output** of a neuron in the **first hidden layer** of a MLP can approximate a **step function** in the direction of the ith input as the weight of the connection between the ith input neuron and the neuron in the hidden layer tends to infinity.
2. We can add **step** functions together to create **bump** and **tower** functions, which can be used to construct **piecewise constant** functions.
3. **Piecewise constant** functions can approximate any **continuous function**.

Meanwhile, we researched core concepts for our proof, such as the **epsilon-delta** definition of **limits** and **continuity** and **distance metrics**, which we would implement later in our proofs. 

## The case of ReLU functions

We observed that MLPs with **ReLU** activation could also be used to create **piecewise functions** which consisted of **simplices** instead of parallel hyperplanes for the sigmoid case. Although we did not complete a proof showing that piecewise functions can be created using MLPs with ReLU activation for this research project, we assumed this was true and also proved that these piecewise functions could also **approximate any continuous function**. 

## Visualisations

We created four Google Colabs for our project to create our visualisations.
### 1. Approximation_Using_a_Piecewise_Constant_Function_in_2D_Final.ipynb
Creates a interactive plot of a piecewise constant function(which would be constructed by MLPs with sigmoid activation) and a continuous function which the piecewise function is approximating. The user can change the number of sections the piecewise function has. The user can choose one of three continuous functions to approximate and all the plots are in 2D. This helps aid understanding of how increasing the number of sections in the piecewise function improves the approximation.
### 2. Visualisations_for_Poster_Final.ipynb
Creates various visualisations for our research poster. It uses the Manim library to create visualisations. It creates a visualisation of a discrete piecewise function, then four visualisations to illustrate the general structure of the proof: a visualisation of a step function, a visualisation of a bump function, a visualisation of a tower function and a visualisation of another discrete piecewise function.
### 3. Simplex_Construction.ipynb
Creates a plot of a ReLU function, a simplex and a piecwise function constructed from simplices in 3D. This illustrates what these functions would look like, showing how the piecewise function would constructed (by a MLP with ReLU activation), and are used as a visual aid in our poster to aid understanding of our proof.
### 4. Continuity_Video_Final.ipynb
Creates a video explaining the epsilon-delta definition of continuity. It is linked to in our poster using a QR code but can also be downloaded in 2 parts by running the code is also uploaded below:
https://github.com/user-attachments/assets/0fb58fc9-8bfb-4275-adac-ebc01350c839

## Results and future plans

We created a **paper** detailing our proofs, and distilled the key concepts into our **research poster**. We also created **visualisations** for our poster using **Manim** and **Matplotlib**, and a video about the **epsilon-delta definition of continuity** using Manim. In the future, we would like to improve our poster by including a proof for the fact that MLPs with ReLU activation can be used to construct piecewise functions made up of simplices. We would also like to research further into the validity of our method, since we took limits at various stages which could cause issues with the error between the function and its approximation, and improve our proof based on our findings.

> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).

## References

[^1]: Michael Nielsen, *Neural Networks and Deep Learning* (2019). [Chapter 4: Backpropagation](http://neuralnetworksanddeeplearning.com/chap4.html).
