![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Comparative Analysis of ODE Solvers: Accuracy and Performance Evaluation

# Project Description
Solving Ordinary Differential Equations (ODEs) is crucial for modeling dynamic systems in fields like physics, biology, and machine learning. This research evaluates and compares the accuracy of three NODE integrators: RK4, Euler’s method, and an adaptive step-size solver Dormand-Prince 5 utilizing PyTorch’s torchdiffeq. By testing these solvers, we analyze their strengths, limitations, and suitability for tasks requiring precision and efficiency, providing insights for applications like Neural ODEs.

# 1. Motivation
Ordinary Differential Equation (ODE) methods play a vital role in modeling dynamic systems across fields like physics, biology, and machine learning. However, determining which numerical solver offers the best balance of accuracy, efficiency, and computational cost remains a critical challenge. By evaluating and comparing fixed-step solvers like Euler's method and RK4 against the adaptive step-size Dormand-Prince 5 solver, this research provides a systematic analysis of their performance. The results aim to offer deeper insights into the strengths and limitations of each method, guiding researchers and practitioners toward choosing the most suitable solver for Neural ODEs!

# 2. Research question
How do various ODE solvers influence the accuracy and computational performance of Neural Ordinary Differential Equations?

# 3.  Method and implementation
-**Dataset:** Spiral dataset with 2000 points.
-**Methods:** Euler’s method, Runge-Kutta 4 (RK4), and Dormand-Prince 5 (Dopri5) adaptive solver from the torchdiffeq library.
-**Evaluation Metrics:** Training loss and computational time over 400 epochs.
-**Sensitivity Method:** Adjoint sensitivity for memory-efficient backpropagation.
-**Framework:** PyTorch.
**Key Focus:** Comparison of fixed-step solvers (Euler, RK4) and adaptive solver (ODEINT - Dopri5) to analyze trade-offs in accuracy, computational efficiency, and performance optimization in Neural ODEs.

# 4. Results
Two Neural ODE fixed time step numerical solvers: Euler’s method RK4 method were implemented, and compared against each other in terms of error. Because Euler’s integrator is the simplest way to solve NODEs, I decided to compare one of the famous fixed step size ODE solver - RK4 against proposed custom made ODE solver(Dopri5) from the original paper and torchdiffeq library created by author. I utilized spirial dataset of 2000 points and trained them using 4 hundred iterations.

# 5. Conclusions
The objective of this research was to identify the most accurate and efficient Neural ODE (NODE) integrator. By comparing the loss and processing time, it was observed that the adaptive step-size solver Dopri5 demonstrated superior accuracy, with a lower loss compared to the RK4 integrator. However, achieving comparable accuracy with RK4 required reducing the time steps, which significantly increased the computational time. Consequently, Dopri5 proved to be more effective, balancing both accuracy and computational efficiency, making it a preferable choice over RK4 in this context.

> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
