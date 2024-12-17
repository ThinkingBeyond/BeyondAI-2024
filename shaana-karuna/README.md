![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# An Elementary Proof of the Universal Approximation Theorem for Multilayer Perceptrons

## Research question 
Our research question was to expand on Nielsen's proof for the **Universal Approximation Theorem for Multilayer Perceptrons** which he provided in his online textbook, Neural Networks and Deep Learning. We showed that any **continuous function** on the real numbers can be approximated by a **Multilayer Perceptron** (MLP) with several hidden layers and a finite number of neurons, using the **sigmoid** activation function. We also proved that **piecewise functions**, constructed using MLPs with **ReLU** activation, can also approximate any continuous function. Our aim was that our proof would be intuitive and easy to understand, and would use visualisations to help the reader grasp the concepts being used.

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

## Results and future plans

We created a **paper** detailing our proofs, and distilled the key concepts into our **research poster**. We also created **visualisations** for our poster using **Manim** and **Matplotlib**, and a video about the **epsilon-delta definition of continuity** using Manim. In the future, we would like to improve our poster by including a proof for the fact that MLPs with ReLU activation can be used to construct piecewise functions made up of simplices. We would also like to research further into the validity of our method, since we took limits at various stages which could cause issues with the error between the function and its approximation, and improve our proof based on our findings.

> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
