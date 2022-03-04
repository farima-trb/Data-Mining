import pandas as pd
import numpy as np
from scipy import stats

df=pd.read_csv('star.csv')  
print('dataset:\n',df.head())

target = df.iloc[:,0]
print("target:\n",target)


#میانگین
target_mean=np.mean(target)
print("target_mean:",target_mean)

#واریانس
target_variance=np.var(target)
print("target_variance:",target_variance)

#انحراف استاندارد
target_stdeviation=np.std(target)
print("target_stdeviation:",target_stdeviation)

#چارک ها
first_quartile = np.quantile(target,0.25)
print("first_quartile:",first_quartile)

second_quartile = np.quantile(target,0.5)
print("second_quartile:",second_quartile)

third_quartile = np.quantile(target,0.75)
print("third_quartile:",third_quartile)

#دامنه میان چارکی
IQR = third_quartile - first_quartile
print("interquartile range:",IQR)
Upper = third_quartile + 1.5 * IQR
print("Upper bound:",Upper)
Lower = first_quartile - 1.5 * IQR
print("Lower bound:",Lower)

#ماکزیمم و مینیمم
target_min=np.min(target)
print("target_min:",target_min)
target_max=np.max(target)
print("target_max:",target_max)

#چندک های 10،65،80 درصد
per10_quartile = np.quantile(target,0.10)
print("per10_quartile:",per10_quartile)
per65_quartile = np.quantile(target,0.65)
print("per65_quartile:",per65_quartile)
per80_quartile = np.quantile(target,0.80)
print("per80_quartile:",per80_quartile)

print("target length:",len(target))

#---------------------------------------------------------------------------------------

#حذف داده ها با روش
#IQR
new_target=df.loc[(target>Lower) & (target<Upper)].iloc[:,0]

print("new target length:",len(new_target))      

print("new target:\n",new_target)

#میانگین
target_mean=np.mean(new_target)
print("target_mean:",target_mean)

#واریانس
target_variance=np.var(new_target)
print("target_variance:",target_variance)

#انحراف استاندارد
target_stdeviation=np.std(new_target)
print("target_stdeviation:",target_stdeviation)

#چارک ها
first_quartile = np.quantile(new_target,0.25)
print("first_quartile:",first_quartile)
second_quartile = np.quantile(new_target,0.5)
print("second_quartile:",second_quartile)
third_quartile = np.quantile(new_target,0.75)
print("third_quartile:",third_quartile)

#دامنه میان چارکی
IQR = third_quartile - first_quartile
print("interquartile range:",IQR)
Upper = third_quartile + 1.5 * IQR
print("Upper bound:",Upper)
Lower = first_quartile - 1.5 * IQR
print("Lower bound:",Lower)

#ماکزیمم و مینیمم
target_min=np.min(new_target)
print("target_min:",target_min)
target_max=np.max(new_target)
print("target_max:",target_max)

#چندک های 10،65،80 درصد
per10_quartile = np.quantile(new_target,0.10)
print("per10_quartile:",per10_quartile)
per65_quartile = np.quantile(new_target,0.65)
print("per65_quartile:",per65_quartile)
per80_quartile = np.quantile(new_target,0.80)
print("per80_quartile:",per80_quartile)

#-----------------------------------------------------------

#حذف داده ها با روش
#trimmed mean
p=0.05
tails=int(p*len(target))
target_list=target.tolist()
target_list.sort()
target_list=target_list[tails:len(target_list)-tails]

print("target list length:",len(target_list))
print("target list:\n",target_list)

print("trimmed mean:",np.mean(target_list))
#print("trimmed mean with scipy  module:",stats.trim_mean(target_list,0.05))
  
#میانگین
target_mean=np.mean(target_list)
print("target_mean:",target_mean)

#واریانس
target_variance=np.var(target_list)
print("target_variance:",target_variance)

#انحراف استاندارد
target_stdeviation=np.std(target_list)
print("target_stdeviation:",target_stdeviation)

#چارک ها
first_quartile = np.quantile(target_list,0.25)
print("first_quartile:",first_quartile)
second_quartile = np.quantile(target_list,0.5)
print("second_quartile:",second_quartile)
third_quartile = np.quantile(target_list,0.75)
print("third_quartile:",third_quartile)

#دامنه میان چارکی
IQR = third_quartile - first_quartile
print("interquartile range:",IQR)
Upper = third_quartile + 1.5 * IQR
print("Upper bound:",Upper)
Lower = first_quartile - 1.5 * IQR
print("Lower bound:",Lower)

#ماکزیمم و مینیمم
target_min=np.min(target_list)
print("target_min:",target_min)
target_max=np.max(target_list)
print("target_max:",target_max)

#چندک های 10،65،80 درصد
per10_quartile = np.quantile(target_list,0.10)
print("per10_quartile:",per10_quartile)
per65_quartile = np.quantile(target_list,0.65)
print("per65_quartile:",per65_quartile)
per80_quartile = np.quantile(target_list,0.80)
print("per80_quartile:",per80_quartile)
