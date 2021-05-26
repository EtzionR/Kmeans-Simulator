# Kmeans-Simulator
Allows 2D view of the calculation process of kmeans clustering.

## Overview
Kmeans simulator
Allows 2D view of the calculation process of kmeans clustering.

The kmeans algorithm is one of the best known clustering methods in the field of machine learning. At the same time, the use of the algorithm is usually a "black box" that it is not known what steps were taken during it. Therefore, most users do not know what happened in the calculation processes of the cluster.

This problem grows when it comes to an algorithm that is based on a random start of its computational process - like Kmeans. This situation means that different results can be obtained for the exact same inputs - which requires the ability to investigate the different stages of the clustering calculation.

To do this, the simulator code is developed. It is based on code that implements the kmeans algorithm, and which produces at each stage a plot that displays the current state of the record classification. The code works similar to the Kmeans algorithm as follows:

1. Starting of K primary centers at random.
 
2. Find the center closest to each point and classify it to that center.

3. Calculate the new centers, based on the points classified as attractive to them.

4. A production of a plot that presents the points in two-dimensional space according to their classification, and the motion of their center from the previous stage to the present stage.

5. Repeat processes 2 + 3, until the change of the centers becomes minor.

The algorithm works by displaying the points in two-dimensional space based on the first two fields in the given dataframe, but the calculation is performed on all the fields. Also, a simple version of the algorithm built for this project, without generating plots, is available at this link. It should be noted that this code of calculating the cluster using Kmeans does not require special library installations and is built from scratch only using basic Python commands and using a random directory (installed by default).

It should be noted that the algorithm reaches a stop when the distance between the old and new centers reaches a minor size determined by a defined epsilon. This size is calculated automatically as follows:

It is also possible to define under the parameter "eps" another epsilon, which the user wants to use. At the same time, the decision to select epsilon automatically brings the code at the end of its run to fairly accurate results relative to the run when eps = 0:

It can also be clearly seen that the amount of iterations decreases significantly when making an informed choice of epsilon:

example
Everything Else
