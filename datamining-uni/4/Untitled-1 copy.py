from http.client import responses
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy.stats import chi2_contingency
from sklearn.preprocessing import LabelEncoder

import matplotlib as plt
import seaborn as sns

url="http://data.insideairbnb.com/singapore/sg/singapore/2021-10-28/visualisations/listings.csv"
data =pd.read_csv(url)


new_data=data.copy()


# x1: reviews_per_month  --> mean_rpm: 0.65
mean_rpm="{:.2f}".format((data.iloc[:,-5]).mean(skipna=True))
(new_data.iloc[:,-5]).fillna(value=mean_rpm,inplace=True)

# x2: availability_365   --> mean_nor: 239.63  
mean_nor="{:.2f}".format((data.iloc[:,-3]).mean(skipna=True))
(new_data.iloc[:,-3]).fillna(value=mean_nor,inplace=True)

with open ("/Users/faritorab/Desktop/newlisting.csv" , 'w') as f:
    new_data.to_csv(f)
    
# print(new_data.head())
#        id                                              name  host_id host_name  ... calculated_host_listings_count availability_365  number_of_reviews_ltm  license
# 0   50646                   Pleasant Room along Bukit Timah   227796   Sujatha  ...                              1              365                      0      NaN
# 1   71609               Ensuite Room (Room 1 & 2) near EXPO   367042   Belinda  ...                              4              365                      0      NaN
# 2   71896                   B&B  Room 1 near Airport & EXPO   367042   Belinda  ...                              4              365                      0      NaN
# 3   71903                        Room 2-near Airport & EXPO   367042   Belinda  ...                              4              365                      0      NaN
# 4  275343  Conveniently located City Room!(1,2,3,4,5,6,7,8)  1439258     Joyce  ...                             50              343                      0      NaN

# [5 rows x 18 columns]

X=new_data[["reviews_per_month","availability_365"]]
y=new_data["price"]

print("X: \n",X)
# X: 
#       reviews_per_month  availability_365
# 0                 0.21               365
# 1                 0.27               365
# 2                 0.32               365
# 3                 0.64               365
# 4                 0.19               343
# ...                ...               ...
# 4118              0.65               362
# 4119              0.65               365
# 4120              0.65               358
# 4121              0.65               364
# 4122              0.65               358
print("y:\n",y)
# y:
#  0        80
# 1       177
# 2        81
# 3        81
# 4        52
#        ... 
# 4118    123
# 4119     88
# 4120     58
# 4121    276
# 4122    480

regr = LinearRegression()
regr.fit(X, y)

print('b0: \t', regr.intercept_)
# b0: 174.4405622545075

print('slope: \t', regr.coef_)
# slope: [-6.76081324  0.0507245 ]

print('R^2: \t', regr.score(X, y))
# R^2: 0.0006654739313914915

response = regr.predict(X)
print('predicted response:', response, sep='\n')
# predicted response:
# [191.5352338  191.129585   190.79154434 ... 188.20540448 188.50975147
#  188.20540448]




#------------------------------------------------------------------------------------------------------------------------------------

contingency_table = pd.crosstab(
    new_data['neighbourhood_group'],
    new_data['room_type'],
    margins = True
)

print(contingency_table)
# room_type            Entire home/apt  Hotel room  Private room  Shared room   All
# neighbourhood_group                                                              
# Central Region                  1547         179          1448          132  3306
# East Region                       54           3           201            6   264
# North Region                      13           0           100            6   119
# North-East Region                 33           0           106            4   143
# West Region                      122           0           158           11   291
# All                             1769         182          2013          159  4123

# print(stats.chi2_contingency(crosstab))

# neighbourhood_group = new_data["neighbourhood_group"]
# # l=LabelEncoder()
# # neighbourhood_group=l.fit_transform(neighbourhood_group)

# room_type=new_data["room_type"]
# # l=LabelEncoder()
# # room_type=l.fit_transform(room_type)


x_squared, p, dof, expected = chi2_contingency(contingency_table)

print(x_squared,"\n", p,"\n", dof,"\n",expected )

