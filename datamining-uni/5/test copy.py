from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import Birch

url="/Users/faritorab/Desktop/datasets/imdb_top_1000.csv"
data = pd.read_csv(url)

cor=data.corr()
print(cor)
#                Released_Year  IMDB_Rating  Meta_score  No_of_Votes
# Released_Year       1.000000    -0.131152   -0.339279     0.241779
# IMDB_Rating        -0.131152     1.000000    0.268531     0.494979
# Meta_score         -0.339279     0.268531    1.000000    -0.018507
# No_of_Votes         0.241779     0.494979   -0.018507     1.000000
sns.heatmap(cor, square = True)
plt.show()

data["Certificate"].fillna(value="Unkown",inplace=True)


mean_score=int(float("{:.2f}".format(data["Meta_score"].mean(skipna=True))))
data["Meta_score"].fillna(value=mean_score,inplace=True)


le = preprocessing.LabelEncoder()
data["Certificate"] = le.fit_transform(data["Certificate"].values)
data["Director"] = le.fit_transform(data["Director"].values)

with open ("/Users/faritorab/Desktop/newlist.csv" , 'w') as f:
    data.to_csv(f)

# print(max(data["Certificate"]))
# 16

# print(max(data["Director"]))
# 547


def quantitive(data):
    #string variable = "Director"  
    #quantitive variable = "Meta_score"    
    new_data = data[["Director", "Meta_score"]]

    print("agg.quantitive new data:\n",new_data)
    #     agg.quantitive new data:
    #     Director  Meta_score
    # 0         141        80.0
    # 1         137       100.0
    # 2          83        84.0
    # 3         137        90.0
    # 4         456        96.0
    # ..        ...         ...
    # 995        50        76.0
    # 996       164        84.0
    # 997       145        85.0
    # 998        22        78.0
    # 999        22        93.0

    # [1000 rows x 2 columns]

    scaler = StandardScaler()
    X_std = scaler.fit_transform(new_data)

    print("agg.quantitive X_std:\n",X_std)
    #     agg.quantitive X_std:
    # [[-0.76219163  0.19195773]
    # [-0.78690621  1.95223033]
    # [-1.12055311  0.54401225]
    # ...
    # [-0.73747704  0.63202588]
    # [-1.49745054  0.01593047]
    # [-1.49745054  1.33613492]]
    
    #-----with 4 clusters----
    new_data4=new_data.copy()

    clt = AgglomerativeClustering(linkage="complete", affinity="euclidean", n_clusters=4)
    model = clt.fit(X_std)

    clusters = pd.DataFrame(model.fit_predict(X_std))
    new_data4["Cluster"] = clusters

    print("agg.quantitive new data with 4 clusters:\n",new_data4)
    #     agg.quantitive new data with 4 clusters:
    #     Director  Meta_score  Cluster
    # 0         141        80.0        1
    # 1         137       100.0        1
    # 2          83        84.0        1
    # 3         137        90.0        1
    # 4         456        96.0        3
    # ..        ...         ...      ...
    # 995        50        76.0        1
    # 996       164        84.0        1
    # 997       145        85.0        1
    # 998        22        78.0        1
    # 999        22        93.0        1

    # [1000 rows x 3 columns]

    fig = plt.figure(); ax = fig.add_subplot(111)
    scatter = ax.scatter(new_data4["Director"],new_data4["Meta_score"], c=new_data4["Cluster"],s=50)
    ax.set_title("quantitive Clustering with 4 clusters")
    plt.xlabel('Director')
    plt.ylabel('Meta_score')
    plt.colorbar(scatter)

    #-----with 5 clusters-----
    new_data5=new_data.copy()

    clt = AgglomerativeClustering(linkage="complete", affinity="euclidean", n_clusters=5)
    model = clt.fit(X_std)

    clusters = pd.DataFrame(model.fit_predict(X_std))
    new_data5["Cluster"] = clusters

    print("agg.quantitive new data with 5 clusters:\n",new_data5)
    #     agg.quantitive new data with 5 clusters:
    #     Director  Meta_score  Cluster
    # 0         141        80.0        0
    # 1         137       100.0        0
    # 2          83        84.0        0
    # 3         137        90.0        0
    # 4         456        96.0        1
    # ..        ...         ...      ...
    # 995        50        76.0        0
    # 996       164        84.0        0
    # 997       145        85.0        0
    # 998        22        78.0        0
    # 999        22        93.0        0

    # [1000 rows x 3 columns]

    fig = plt.figure(); ax = fig.add_subplot(111)
    scatter = ax.scatter(new_data5["Director"],new_data5["Meta_score"], c=new_data5["Cluster"],s=50)
    ax.set_title("quantitive Clustering with 5 clusters")
    plt.xlabel('Director')
    plt.ylabel('Meta_score')
    plt.colorbar(scatter)

    #-----with 6 clusters-----
    new_data6=new_data.copy()

    clt = AgglomerativeClustering(linkage="complete", affinity="euclidean", n_clusters=6)
    model = clt.fit(X_std)

    clusters = pd.DataFrame(model.fit_predict(X_std))
    new_data6["Cluster"] = clusters

    print("agg.quantitive new data with 6 clusters:\n",new_data6)
    #     agg.quantitive new data with 6 clusters:
    #     Director  Meta_score  Cluster
    # 0         141        80.0        5
    # 1         137       100.0        2
    # 2          83        84.0        2
    # 3         137        90.0        2
    # 4         456        96.0        1
    # ..        ...         ...      ...
    # 995        50        76.0        5
    # 996       164        84.0        2
    # 997       145        85.0        2
    # 998        22        78.0        5
    # 999        22        93.0        2

    # [1000 rows x 3 columns]

    fig = plt.figure(); ax = fig.add_subplot(111)
    scatter = ax.scatter(new_data6["Director"],new_data6["Meta_score"], c=new_data6["Cluster"],s=50)
    ax.set_title("quantitive Clustering with 6 clusters")
    plt.xlabel('Director')
    plt.ylabel('Meta_score')
    plt.colorbar(scatter); plt.show()
    
quantitive(data)    


def qualitive(data):
    #string variable = "Director"  
    #qualitive variable = "Certificate"        
    new_data = data[["Director","Certificate"]]

    print("agg.qualitive new data:\n",new_data)
    #     agg.qualitive new data:
    #     Director  Certificate
    # 0         141            1
    # 1         137            1
    # 2          83           14
    # 3         137            1
    # 4         456           12
    # ..        ...          ...
    # 995        50            1
    # 996       164            3
    # 997       145            7
    # 998        22           15
    # 999        22           15

    # [1000 rows x 2 columns]

    scaler = StandardScaler()
    X_std = scaler.fit_transform(new_data)

    print("agg.qualitive X_std:\n",X_std)
    #     agg.qualitive X_std:
    # [[-0.76219163 -1.58797324]
    # [-0.78690621 -1.58797324]
    # [-1.12055311  1.00349703]
    # ...
    # [-0.73747704 -0.39191004]
    # [-1.49745054  1.20284089]
    # [-1.49745054  1.20284089]]
    
    #-----with 4 clusters----
    new_data4=new_data.copy()

    clt = AgglomerativeClustering(linkage="complete", affinity="euclidean", n_clusters=4)
    model = clt.fit(X_std)

    clusters = pd.DataFrame(model.fit_predict(X_std))
    new_data4["Cluster"] = clusters

    print("agg.qualitive new data with 4 clusters:\n",new_data4)
    #     agg.qualitive new data with 4 clusters:
    #     Director  Certificate  Cluster
    # 0         141            1        0
    # 1         137            1        0
    # 2          83           14        3
    # 3         137            1        0
    # 4         456           12        1
    # ..        ...          ...      ...
    # 995        50            1        0
    # 996       164            3        0
    # 997       145            7        0
    # 998        22           15        3
    # 999        22           15        3

    # [1000 rows x 3 columns]

    fig = plt.figure(); ax = fig.add_subplot(111)
    scatter = ax.scatter(new_data4["Director"],new_data4["Certificate"], c=new_data4["Cluster"],s=50)
    ax.set_title("agg.qualitive Clustering with 4 clusters")
    plt.xlabel('Director')
    plt.ylabel('Certificate')
    plt.colorbar(scatter)

    #-----with 5 clusters-----
    new_data5=new_data.copy()

    clt = AgglomerativeClustering(linkage="complete", affinity="euclidean", n_clusters=5)
    model = clt.fit(X_std)

    clusters = pd.DataFrame(model.fit_predict(X_std))
    new_data5["Cluster"] = clusters

    print("agg.qualitive new data with 5 clusters:\n",new_data5)
    #     agg.qualitive new data with 5 clusters:
    #     Director  Certificate  Cluster
    # 0         141            1        1
    # 1         137            1        1
    # 2          83           14        3
    # 3         137            1        1
    # 4         456           12        0
    # ..        ...          ...      ...
    # 995        50            1        1
    # 996       164            3        4
    # 997       145            7        1
    # 998        22           15        3
    # 999        22           15        3

    # [1000 rows x 3 columns]

    fig = plt.figure(); ax = fig.add_subplot(111)
    scatter = ax.scatter(new_data5["Director"],new_data5["Certificate"], c=new_data5["Cluster"],s=50)
    ax.set_title("agg.qualitive Clustering with 5 clusters")
    plt.xlabel('Director')
    plt.ylabel('Certificate')
    plt.colorbar(scatter)

    #-----with 6 clusters-----
    new_data6=new_data.copy()

    clt = AgglomerativeClustering(linkage="complete", affinity="euclidean", n_clusters=6)
    model = clt.fit(X_std)

    clusters = pd.DataFrame(model.fit_predict(X_std))
    new_data6["Cluster"] = clusters

    print("agg.qualitive new data with 6 clusters:\n",new_data6)
    #     agg.qualitive new data with 6 clusters:
    #     Director  Certificate  Cluster
    # 0         141            1        1
    # 1         137            1        1
    # 2          83           14        3
    # 3         137            1        1
    # 4         456           12        5
    # ..        ...          ...      ...
    # 995        50            1        1
    # 996       164            3        4
    # 997       145            7        1
    # 998        22           15        3
    # 999        22           15        3

    # [1000 rows x 3 columns]

    fig = plt.figure(); ax = fig.add_subplot(111)
    scatter = ax.scatter(new_data6["Director"],new_data6["Certificate"], c=new_data6["Cluster"],s=50)
    ax.set_title("agg.qualitive Clustering with 6 clusters")
    plt.xlabel('Director')
    plt.ylabel('Certificate')
    plt.colorbar(scatter); plt.show()

qualitive(data)


def two_steps(data):
    new_data2 = data[["Director", "Meta_score"]]
    print(new_data2.head())
    #    Director  Meta_score
    # 0       141        80.0
    # 1       137       100.0
    # 2        83        84.0
    # 3       137        90.0
    # 4       456        96.0   
        
    #-----with 4 clusters----    
    model = Birch(branching_factor=30, n_clusters=4, threshold=2.5)
    model.fit(new_data2)
    pred = model.predict(new_data2)    
    plt.scatter(new_data2["Director"],new_data2["Meta_score"], c=pred,s=50)
    plt.title("2 step Clustering with 4 clusters")
    plt.xlabel('Director')
    plt.ylabel('Meta_score')
    plt.show()
    #-----with 5 clusters---- 
    model = Birch(branching_factor=30, n_clusters=5, threshold=2.5)
    model.fit(new_data2)
    pred = model.predict(new_data2)    
    plt.scatter(new_data2["Director"],new_data2["Meta_score"], c=pred,s=50)
    plt.title("2 step Clustering with 5 clusters")
    plt.xlabel('Director')
    plt.ylabel('Meta_score')
    plt.show()
    #-----with 6 clusters----
    model = Birch(branching_factor=30, n_clusters=6, threshold=2.5)
    model.fit(new_data2)
    pred = model.predict(new_data2)    
    plt.scatter(new_data2["Director"],new_data2["Meta_score"], c=pred,s=50)
    plt.title("2 step Clustering with 6 clusters")
    plt.xlabel('Director')
    plt.ylabel('Meta_score')
    plt.show()  
    
two_steps(data)    