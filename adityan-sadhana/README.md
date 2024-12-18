![BeyondAI Banner for Research Projects](../BeyondAI_Banner_Research_Projects_2024.png)

# Dynamic Graph Neural Networks For Anomaly Detection


We implement a Spatio-Temporal Graph Neural Network (SpatioTemporalGNN) to understand spatio-temporal relationships between nodes in a dynamic graph. To realise DGNNs, we utilise satellite trajectories and the prediction of potential collisions as edge features. By utilising Two-Line Element (TLE) data, we model satellites as nodes in a dynamic graph and encode their relative spatial interactions as edge features. Our approach demonstrates the capability of graph-based learning to capture spatiotemporal dependencies, enabling the prediction of anomalies or in our application, impending satellite collisions.

Graph Neural Networks (GNNs) are a powerful tool for learning from graph-structured data, where nodes represent entities and edges capture relationships. Dynamic Graph Neural Networks (DGNNs) extend GNNs by incorporating temporal dynamics, enabling them to model evolving graphs over time. DGNNs represent entities as nodes with feature embeddings and encode evolving relationships through dynamically updated edges. These dynamic edges can reflect changes in connections or interactions over time. We use GCNConv layers, which aggregate information from neighboring nodes and edges, to effectively learn and propagate both spatial and temporal patterns across the graph. This enables DGNNs to adapt to changing graph structures and extract meaningful insights from time-evolving data.

We utilised the NORAD dataset’s TLE data of active satellites. Working with SGP4, we converted TLE data into Cartesian coordinates to represent satellite positions. Using this ground truth, we generated a temporal sequence of graphs where edges represent relative distances. Each snap shot of the dyngraph is taken per day. We normalized features for stable training and split our testing and training data. In this manner, we obtain a ground truth as well as a prediction allowing us to accurately gauge the functionality of the model.

We approach this problem by working with a spatio-temporal graph neural network model that utilises Graph Convolution via the GCNConv function in the PyTorch-Geometric library. 
- The first GCN layer transforms the input node features  into an intermediate representation by aggregating information from neighboring nodes.
- The second GCN layer refines this representation, further capturing spatial dependencies.


By normalising the feature distribution we maintain the training stability and improve convergence. We calculate our loss using Mean Squared Error and use the Adam optimiser to ensure accurate and efficient training. Our testing metrics include RMSE, F1-score, Recall, and Precision. We observe that our model is able to predict the spatio-temporal dependencies between the satellites overhead, and effectively predict collisions between satellites, which we have defined as our anomaly. This novel application of DGNNs allows us to perceive the problem of satellite trajectories in a new light, enhancing our understanding of them and providing us with the opportunity to develop our representation further with additional features.

->
| Metric              | Value  |
|---------------------|--------|
| Mean Squared Error  | 0.9987 |
| Mean Absolute Error | 0.0975 | 
| Accuracy            | 99%    |
| F1 Score            | 1      |
<-

> The research poster for this project can be found in the [BeyondAI Proceedings 2024](https://thinkingbeyond.education/beyondai_proceedings_2024/).
