# Kmeans-Simulator
Allows a 2D view of the calculation process for kmeans clustering.

## Overview
The kmeans algorithm is one of the best known clustering methods in the field of **machine learning**. At the same time, the use of the algorithm is usually as a **"black box"** that the users dont know what steps were taken during it. Therefore, most users do not know what happened in the calculation processes of the cluster.

This problem grows when it comes to an algorithm that is based on a **random start point** of its computational process - as Kmeans. This aspect means that different results can be obtained for the exact same inputs - which requires the ability to investigate the different stages of the clustering calculation.

The [**Kmeans simulator code**](https://github.com/EtzionR/Kmeans-Simulator/blob/main/kmeans.py) developed to do so. It is based on code that apply kmeans algorithm, and which produces at each stage a **plot that displays the current state** of the row classification. The code works similar to the Kmeans algorithm as follows:

1. Starting **randomaly** K primary centers from the original dataframe .
 
2. Find the center closest to each row and **classify** this row to that center.

3. Calculate the **new centers**, based on the rows classified as closest to the old centers.

4. produce a **plot** that presents the rows in 2D space according to their classification, and the motion of their centers from the previous stage to the present stage.

5. **Repeat** stages 2 + 3, until the change of the centers becomes minor.

You can see example output of the simulation code here (based on [data_1.csv](https://github.com/EtzionR/Kmeans-Simulator/blob/main/example/data_1.csv) dataset):

![exm](https://github.com/EtzionR/Kmeans-Simulator/blob/main/picture/output_3.gif)

As yo can see, the code works by displaying the points in 2D space based on the **first two fields** in the given dataframe, but the calculation is performed on all the fields. Also, a simple version of the algorithm built for this project, without plots generating, is available here: [**kmeans algorithm**](https://github.com/EtzionR/Kmeans-Simulator/blob/main/km.py). It should be noted that this code of calculating the cluster using Kmeans **does not require special library installations** and it built from scratch only using basic Python commands and using only random library (installed by default).

It should be noted that the algorithm iterations stop when the distance between the old and new centers reaches a **minor size** determined by a defined epsilon. This size is calculated automatically as follows:

<img src="https://render.githubusercontent.com/render/math?math=Epsilon =  \epsilon  = \frac{min(len(column_{1}) \cdots len(column_{p}))}{\sqrt{n}}">

when P represent the number of columns in the dataframe, and len:

<img src="https://render.githubusercontent.com/render/math?math=len(x) = \mid max(x)-min(x) \mid">

It is also possible to define under the parameter **"eps"** another epsilon, which the user wants to use. At the same time, the decision to select epsilon automatically brings the code at the end of its run to fairly **accurate** results relative to the run when eps = 0:

![acc](https://github.com/EtzionR/Kmeans-Simulator/blob/main/picture/eps_adapt.png)

This calculation made by using this examples files:

1. [data_1.csv](https://github.com/EtzionR/Kmeans-Simulator/blob/main/example/data_1.csv)

2. [data_2.csv](https://github.com/EtzionR/Kmeans-Simulator/blob/main/example/data_2.csv)

3. [data_3.csv](https://github.com/EtzionR/Kmeans-Simulator/blob/main/example/data_3.csv)

We check the accuracy by comparing two labels sets:
- The labels of the rows when the distance between the centers is smaller than the adapt epsilon.
- The labels when the distance is equal to 0. 
As you can see, we get **pretty accurate** results even when we choose the adapt epsilon.

It can also be clearly seen that the **amount of iterations decreases significantly** when making an informed choice of epsilon:

![itr](https://github.com/EtzionR/Kmeans-Simulator/blob/main/picture/eps_distr_.png)


## Libraries
The code uses the following libraries in Python:

 - **random** (Default installed)


## Application
An application of the code is attached to this page under the name: 

[**implementation.py**](https://github.com/EtzionR/Kmeans-Simulator/blob/main/implementation.py)

the examples outputs are also attached here.


## Example for using the code
To use this code, you just need to import it as follows:
``` sh
# import
from kmeans import Simulator
import pandas as pd

# define variables
data= pd.read_csv(r'path\data.csv')  
k = 5
eps = 0.001

# application
Simulator(data,k,eps=eps).fit().create_gif('output')
```

When the variables displayed are:

**data:** pandas dataframe that you want to perform clustering on all its columns

**k:** the number of clusters that should split the data

**eps:** epsilon for centers calculation you want to define (default: as follow: [LINK](https://render.githubusercontent.com/render/math?math=Epsilon%20=%20%20\epsilon%20%20=%20\frac{min(len(column_{1})%20\cdots%20len(column_{p}))}{\sqrt{n}}))


## License
MIT © [Etzion Harari](https://github.com/EtzionData)
