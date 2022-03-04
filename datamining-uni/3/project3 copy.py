import pandas as pd


url="http://data.insideairbnb.com/singapore/sg/singapore/2021-10-28/visualisations/listings.csv"
data =pd.read_csv(url)

print("head of data before any changes:\n",data.head())
# dataset:
#         id                                              name  host_id host_name  ... calculated_host_listings_count availability_365  number_of_reviews_ltm  license
# 0   50646                   Pleasant Room along Bukit Timah   227796   Sujatha  ...                              1              365                      0      NaN
# 1   71609               Ensuite Room (Room 1 & 2) near EXPO   367042   Belinda  ...                              4              365                      0      NaN
# 2   71896                   B&B  Room 1 near Airport & EXPO   367042   Belinda  ...                              4              365                      0      NaN
# 3   71903                        Room 2-near Airport & EXPO   367042   Belinda  ...                              4              365                      0      NaN
# 4  275343  Conveniently located City Room!(1,2,3,4,5,6,7,8)  1439258     Joyce  ...                             50              343                      0      NaN

new_data1=data.copy()

mean_rpm="{:.2f}".format((data.iloc[:,-5]).mean(skipna=True))

print("mean of column -5:",mean_rpm)
# 0.65

print("column -5 before filling NaN:\n",new_data1.iloc[:,-5])
# 0       0.21
# 1       0.27
# 2       0.32
# 3       0.64
# 4       0.19
#         ... 
# 4118     NaN
# 4119     NaN
# 4120     NaN
# 4121     NaN
# 4122     NaN

(new_data1.iloc[:,-5]).fillna(value=mean_rpm,inplace=True)

print("column -5 after filling NaN:\n",new_data1.iloc[:,-5])
# 0       0.21
# 1       0.27
# 2       0.32
# 3       0.64
# 4       0.19
#         ... 
# 4118    0.65
# 4119    0.65
# 4120    0.65
# 4121    0.65
# 4122    0.65
# Name: reviews_per_month, Length: 4123, dtype: object


print("new data after filling NaN:\n",new_data1)
#            id                                               name    host_id   host_name  ... calculated_host_listings_count availability_365  number_of_reviews_ltm  license
# 0        50646                    Pleasant Room along Bukit Timah     227796     Sujatha  ...                              1              365                      0      NaN
# 1        71609                Ensuite Room (Room 1 & 2) near EXPO     367042     Belinda  ...                              4              365                      0      NaN
# 2        71896                    B&B  Room 1 near Airport & EXPO     367042     Belinda  ...                              4              365                      0      NaN
# 3        71903                         Room 2-near Airport & EXPO     367042     Belinda  ...                              4              365                      0      NaN
# 4       275343   Conveniently located City Room!(1,2,3,4,5,6,7,8)    1439258       Joyce  ...                             50              343                      0      NaN
# ...        ...                                                ...        ...         ...  ...                            ...              ...                    ...      ...
# 4118  53005959                         Modern condo at West Coast  246450542  Blackthorn  ...                              1              362                      0      NaN
# 4119  53016155          Walk up apartment one bed room at geylang  417393455     Desmond  ...                             13              365                      0      NaN
# 4120  53016255                  Ensuite master room @ Farrer Park  417393455     Desmond  ...                             13              358                      0      NaN
# 4121  53019055  Pleasant 1 BR in Clarke Quay, 3 mins stroll to...  156409670         Tia  ...                            172              364                      0      NaN
# 4122  53020768     STAY AT THE 2BR LUXURY AT BUSTLING- ORCHARD RD  156409670         Tia  ...                            172              358                      0      NaN
# [4123 rows x 18 columns]

with open ("/Users/faritorab/Desktop/newlisting1.csv" , 'w') as f:
    new_data1.to_csv(f)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

new_data12=data.copy()
new_data12.insert(18,"merged",data.iloc[:,1]+"("+data.iloc[:,-5].astype(str)+")")


print("new data2 after merging:\n",new_data12)
# new data2 after merging:
#              id                                               name    host_id  ... number_of_reviews_ltm license                                             merged
# 0        50646                    Pleasant Room along Bukit Timah     227796  ...                     0     NaN              Pleasant Room along Bukit Timah(0.21)
# 1        71609                Ensuite Room (Room 1 & 2) near EXPO     367042  ...                     0     NaN          Ensuite Room (Room 1 & 2) near EXPO(0.27)
# 2        71896                    B&B  Room 1 near Airport & EXPO     367042  ...                     0     NaN              B&B  Room 1 near Airport & EXPO(0.32)
# 3        71903                         Room 2-near Airport & EXPO     367042  ...                     0     NaN                   Room 2-near Airport & EXPO(0.64)
# 4       275343   Conveniently located City Room!(1,2,3,4,5,6,7,8)    1439258  ...                     0     NaN  Conveniently located City Room!(1,2,3,4,5,6,7,...
# ...        ...                                                ...        ...  ...                   ...     ...                                                ...
# 4118  53005959                         Modern condo at West Coast  246450542  ...                     0     NaN                    Modern condo at West Coast(nan)
# 4119  53016155          Walk up apartment one bed room at geylang  417393455  ...                     0     NaN     Walk up apartment one bed room at geylang(nan)
# 4120  53016255                  Ensuite master room @ Farrer Park  417393455  ...                     0     NaN             Ensuite master room @ Farrer Park(nan)
# 4121  53019055  Pleasant 1 BR in Clarke Quay, 3 mins stroll to...  156409670  ...                     0     NaN  Pleasant 1 BR in Clarke Quay, 3 mins stroll to...
# 4122  53020768     STAY AT THE 2BR LUXURY AT BUSTLING- ORCHARD RD  156409670  ...                     0     NaN  STAY AT THE 2BR LUXURY AT BUSTLING- ORCHARD RD...

# [4123 rows x 19 columns]

with open ("/Users/faritorab/Desktop/newlisting2.csv" , 'w') as f:
    new_data12.to_csv(f)