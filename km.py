# Create by Etzion Harari
# https://github.com/EtzionR

# import libraries
from random import sample

# define helpful functions
dist    = lambda x,y: sum([(x[j]-y[j])**2 for j in range(len(x))])**.5
stop    = lambda old,new,eps: max([dist(old[i],new[i]) for i in range(len(new))])>eps
length  = lambda col: abs(max(col)-min(col))
colmean = lambda tbl:[sum([tbl[i][j] for i in range(len(tbl))])/len(tbl) for j in range(len(tbl[0]))]

# define kmeans simulator object
class Kmeans:
    """
    kmeans object
    """
    def __init__(self,df,k,eps=-1):
        """
        initialize object
        :param df: given dataframe
        :param k: k value for split the df for clusters
        """
        self.k = k
        self.n = df.shape[0]
        self.p = df.shape[1]
        self.x = df.iloc[:,0]
        self.y = df.iloc[:,1]
        self.times = 0
        self.table = df.values.tolist()
        self.labels= [0]*self.n
        self.centers = sample(self.table,k)
        self.columns = [[self.table[i][j] for i in range(self.n)] for j in range(self.p)]
        self.running = True
        self.eps = eps if eps>=0 else min([length(c) for c in self.columns])/(self.n**.5)

    def find_labels(self):
        """
        calculate the cluster labels in given loop step
        :return: labels for each row
        """
        labels = []
        for line in self.table:
            dists = {dist(self.centers[i], line):i for i in range(self.k)}
            labels.append(dists[min(dists.keys())])
        return labels

    def split_table(self):
        """
        split the given df to separate dataframes,
        one for each cluster
        :return: separate dataframes
        """
        sub_tables = {i: [] for i in range(self.k)}
        for idx in range(self.n):
            sub_tables[self.labels[idx]].append(self.table[idx])
        return sub_tables

    def fit(self):
        """
        the main function of the object
        calculate kmeans clustering for the given df
        :param self
        :return: self
        """
        while self.running:
            self.times += 1
            old_centers = self.centers[:]
            self.labels = self.find_labels()
            self.tables = self.split_table()
            self.centers= [colmean(self.tables[i]) for i in range(self.k)]
            self.running= stop(old_centers, self.centers, self.eps)
        return self

# MIT © Etzion Harari
