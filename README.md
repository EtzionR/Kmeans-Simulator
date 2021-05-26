# Kmeans-Simulator
Allows 2D view of the calculation process of kmeans clustering.

## Overview
The kmeans algorithm is one of the best known clustering methods in the field of **machine learning**. At the same time, the use of the algorithm is usually as a **"black box"** that the users dont know what steps were taken during it. Therefore, most users do not know what happened in the calculation processes of the cluster.

This problem grows when it comes to an algorithm that is based on a **random start point** of its computational process - as Kmeans. This aspect means that different results can be obtained for the exact same inputs - which requires the ability to investigate the different stages of the clustering calculation.

The simulator code developed to do so. It is based on code that apply kmeans algorithm, and which produces at each stage a **plot that displays the current state** of the row classification. The code works similar to the Kmeans algorithm as follows:

1. Starting **randomaly** K primary centers from the original dataframe .
 
2. Find the center closest to each row and **classify** this row to that center.

3. Calculate the **new centers**, based on the rows classified as closest to the old centers.

4. produce a **plot** that presents the rows in 2D space according to their classification, and the motion of their centers from the previous stage to the present stage.

5. **Repeat** stages 2 + 3, until the change of the centers becomes minor.

The code works by displaying the points in 2D space based on the **first two fields** in the given dataframe, but the calculation is performed on all the fields. Also, a simple version of the algorithm built for this project, without plots generating, is available here: [**kmeans algorithm**](). It should be noted that this code of calculating the cluster using Kmeans **does not require special library installations** and it built from scratch only using basic Python commands and using only random library (installed by default).

It should be noted that the algorithm iterations stop when the distance between the old and new centers reaches a **minor size** determined by a defined epsilon. This size is calculated automatically as follows:

<img src="https://render.githubusercontent.com/render/math?math=Epsilon =  \epsilon  = \frac{min(len(column_{1}) \cdots len(column_{p}))}{\sqrt{n}}">

It is also possible to define under the parameter **"eps"** another epsilon, which the user wants to use. At the same time, the decision to select epsilon automatically brings the code at the end of its run to fairly **accurate** results relative to the run when eps = 0:

It can also be clearly seen that the **amount of iterations decreases significantly** when making an informed choice of epsilon:

example
Everything Else
