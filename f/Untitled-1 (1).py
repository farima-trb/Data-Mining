import random
import matplotlib.pyplot as plt
# from sklearn.preprocessing import MinMaxScaler
import csv
import numpy as np
import statistics
import os

def st_info(student_mean,student_median,student_mode,student_std):
	st_dict={}
	st_list=[['stmean',student_mean],['stmedain',student_median],['stmode',student_mode],['standard deviation',student_std]]
	st_dict=dict(st_list)
	return st_dict

os.makedirs('D:\\FARIMA st_results',exist_ok = True)
os.makedirs('D:\\FARIMA st_results\plots',exist_ok = True)
marks_list=[]
numbers=[]

#initialize the marks of students in a list
for i in range(0,1000):
	m="{:.2f}".format(random.uniform(0,20.00))
	marks_list.append(float(m))

#initalize the student's number in a list
for i in range(0,1000):
	numbers.append(i+1)

#put values in a dictionary
st_dict={numbers[i]: marks_list[i] for i in range(len(numbers))}

xpoints=numbers
ypoints=marks_list

#enter data in a dictionary
# st_dict=dict(zip(numbers,marks_list))

#---mean,mode,median,standard deviation
st_mean=statistics.mean(marks_list)
st_median=statistics.median(marks_list)
st_mode=statistics.mode(marks_list)
st_stdev=statistics.stdev(marks_list)

first_quartile = np.quantile(marks_list,0.25)
second_quartile = np.quantile(marks_list,0.5)
third_quartile = np.quantile(marks_list,0.75)
interquartile=third_quartile-first_quartile
High = third_quartile + 1.5 * interquartile
Low = first_quartile - 1.5 * interquartile


# print('marks list:\n',marks_list)
print('----------------------------------------------')
print('FIRST LIST\'S DATA:\n','mean:',st_mean,'\t','mode:',st_mode,'\t','median:',st_median,'\n',
	  'max:',max(marks_list),'\t','min:',min(marks_list),'\n','standard deviation:',st_stdev)
print('----------------------------------------------')


#---q2:draw chart--------------------------------
#linear
plt.plot(xpoints,ypoints)
plt.title("marks")
plt.xlabel("student's number")
plt.ylabel("student's marks")
stmax=plt.plot(max(marks_list), marker = 'o',color='Magenta')
stmin=plt.plot(min(marks_list), marker = 'o',color='Cyan')
stmean=plt.axhline(y=st_mean, color='y')
stmedian=plt.axhline(y=st_median, color='g')

quartile1=plt.plot(first_quartile, marker = 'o',color='r')
quartile2=plt.plot(second_quartile, marker = 'o',color='r')
quartile3=plt.plot(third_quartile, marker = 'o',color='r')

plt.legend((stmean,stmedian),['Mean','Median'],loc='upper right')

# for key,value in st_dict.items():
#     if value == max(numbers):
#     	plt.annotate("MAX", (key,max(marks_list)))

chart_path='D:\\FARIMA st_results\plots\ 1-marks without any changes.png'
plt.savefig(chart_path)
plt.show()

#histogram
# plt.hist(marks_list,bins=100)
# plt.ylabel("frequency")
# plt.show()

#---q3:normalization+chart------------------------

#MinMax Formula
normalized_list=[]
for i in range(0,len(marks_list)):
	normalized_list.append((marks_list[i] - min(marks_list)) / (max(marks_list) - min(marks_list)))

ypoints2=normalized_list
plt.plot(xpoints,ypoints2,color = 'orange')
plt.title("normalized marks")
plt.xlabel("student's number")
plt.ylabel("student's normalized mark")

chart_path='D:\\FARIMA st_results\plots\ 2-marks after normalization.png'
plt.savefig(chart_path)
plt.show()

#showing non-normalized and normalized data in a one plot
plt.plot(xpoints,ypoints)
plt.plot(xpoints,ypoints2)
plt.title("non-normalized and normalized marks")
chart_path='D:\\FARIMA st_results\plots\ 3-before after noramalizing.png'
plt.savefig(chart_path)
plt.show()

#---------------------------------------------------------------------------------------------------------
#Q 5&6 : change 100 marks randomly

#100 unrepetetive index values with range(0,1000) to change
indexes=random.sample(range(1000),100)              
new_choices=[]
new_marks100=marks_list.copy()

#100 mark values with range(0,20)
for i in range(0,100):
	m="{:.2f}".format(random.uniform(0,20.00))    
	new_choices.append(float(m))

# values2=[list(x) for x in zip(indexes,new_choices)]

#put new marks in list
for i in range(0,100):
	new_marks100[indexes[i]]=new_choices[i]        #P

st_mean2=statistics.mean(new_marks100)
st_median2=statistics.median(new_marks100)
st_mode2=statistics.mode(new_marks100)
st_stdev2=statistics.stdev(new_marks100)


print('LIST WITH 100 CHOOSEN MARK TO REPLACE:\n',
	'mean:',st_mean2,'\t','mode:',st_mode2,'\t','median:',st_median2,'\n',
	'max:',max(new_marks100),'\t','min:',min(new_marks100),'\n','standard deviation:',st_stdev2)
print('----------------------------------------------')	  

#plot
plt.plot(marks_list)
plt.plot(new_marks100)
plt.xlabel("student's number")
plt.ylabel("student's mark")
plt.title("changing 100 marks")
chart_path='D:\\FARIMA st_results\plots\ 4-changing 100 marks.png'
plt.savefig(chart_path)
plt.show()

#---------------------------------------------------------------------------------------------------------
#Q 7&8 : choose 15 marks with >18 value

#15 index values with range(0,1000) to change
indexes3=random.sample(range(1000),15)
new_choices=[]
new_marks15=marks_list.copy()

#15 mark values with >18 value
for i in range(0,15):
	m="{:.2f}".format(random.uniform(18.01,20.00))    
	new_choices.append(float(m))

# values3=[list(x) for x in zip(indexes3,new_choices)]

#put new marks in list
for i in range(0,15):
	new_marks15[indexes3[i]]=new_choices[i]

st_mean3=statistics.mean(new_marks15)
st_median3=statistics.median(new_marks15)
st_mode3=statistics.mode(new_marks15)
st_stdev3=statistics.stdev(new_marks15)



print('LIST WITH 15 CHOOSEN MARKS WITH 18> VALUE REPLACED DATA:\n',
	'mean:',st_mean3,'\t','mode:',st_mode3,'\t','median:',st_median3,'\n',
	'max:',max(new_marks15),'\t','min:',min(new_marks15),'\n','standard deviation:',st_stdev3)
print('----------------------------------------------')

#plot
plt.plot(marks_list)
plt.plot(new_marks15)
plt.xlabel("student's number")
plt.ylabel("student's mark")
plt.title("changing 15 mark values with >18 value")
chart_path='D:\\FARIMA st_results\plots\ 5-15marks more than 18.png'
plt.savefig(chart_path)
plt.show()
#---------------------------------------------------------------------------------------------------------
#Q 9&10 : choose 15 marks among down 50 with >18 value

new_marks1550=[list(x) for x in zip(numbers,marks_list)]

#sort based on second value
new_marks1550.sort(key = lambda x: x[1]) 	

#15 index values with range(0,50) to change
indexes4=random.sample(range(0,50),15)
new_choices=[]

#15 mark values with >18 value
for i in range(0,15):
	m="{:.2f}".format(random.uniform(18.01,20.00))    
	new_choices.append(float(m))	

#put new marks in list
for i in range(0,15):
	new_marks1550[indexes4[i]][1]=new_choices[i]

#sort based on first value
new_marks1550.sort(key = lambda x: x[0])

secondv1550=[]
for i in range(0,1000):
	secondv1550.append(new_marks1550[i][1])

st_mean4=statistics.mean(secondv1550)
st_median4=statistics.median(secondv1550)
st_mode4=statistics.mode(secondv1550)
st_stdev4=statistics.stdev(secondv1550)



print('LIST WITH 15 CHOOSEN MARKS AMONG DOWN 50 WITH 18> VALUE REPLACED DATA:\n',
	'mean:',st_mean4,'\t','mode:',st_mode4,'\t','median:',st_median4,'\n',
	'max:',max(secondv1550),'\t','min:',min(secondv1550),'\n','standard deviation:',st_stdev4)
print('----------------------------------------------')	  

#plot
plt.plot(marks_list)
plt.plot(secondv1550)
plt.xlabel("student's number")
plt.ylabel("student's mark")
plt.title("changing 15 marks among down 50 with >18 value")
chart_path='D:\\FARIMA st_results\plots\ 6-15marks among down 50 more than 18.png'
plt.savefig(chart_path)
plt.show()

#---------------------------------------------------------------------------------------------------------
#Q 11&12 : choose 15 marks with <10 value

#15 index values with range(0,1000) to change
indexes5=random.sample(range(1000),15)
new_choices=[]
new_marks151=marks_list.copy()

#15 mark values with <10 value
for i in range(0,15):
	m="{:.2f}".format(random.uniform(0,10.00))    
	new_choices.append(float(m))

# values5=[list(x) for x in zip(indexes5,new_choices)]

#put new marks in list
for i in range(0,15):
	new_marks151[indexes5[i]]=new_choices[i]  #P

st_mean5=statistics.mean(new_marks151)
st_median5=statistics.median(new_marks151)
st_mode5=statistics.mode(new_marks151)
st_stdev5=statistics.stdev(new_marks151)

print('LIST WITH 15 CHOOSEN MARKS WITH <10 VALUE REPLACED DATA:\n',
	'mean:',st_mean5,'\t','mode:',st_mode5,'\t','median:',st_median5,'\n',
	'max:',max(new_marks151),'\t','min:',min(new_marks151),'\n','standard deviation:',st_stdev5)
print('----------------------------------------------')	  

#plot
plt.plot(marks_list)
plt.plot(new_marks151)
plt.xlabel("student's number")
plt.ylabel("student's mark")
plt.title("changing 15 marks with <10 value")
chart_path='D:\\FARIMA st_results\plots\ 7-15marks less than 10.png'
plt.savefig(chart_path)
plt.show()


#---------------------------------------------------------------------------------------------------------
#Q 13&14 : choose 15 marks among top 50 with <10 value

new_marks15501=[list(x) for x in zip(numbers,marks_list)]

#sort based on second value
new_marks15501.sort(key = lambda x: x[1]) 	

#15 index values with range(0,50) to change
indexes6=random.sample(range(950,1000),15)
new_choices=[]

#15 mark values with <10 value
for i in range(0,15):
	m="{:.2f}".format(random.uniform(0,10.00))    
	new_choices.append(float(m))


#put new marks in list
for i in range(0,15):
	new_marks15501[indexes6[i]][1]=new_choices[i]

#sort based on first value
new_marks15501.sort(key = lambda x: x[0])

secondv15501=[]
for i in range(0,1000):
	secondv15501.append(new_marks15501[i][1])

st_mean6=statistics.mean(secondv15501)
st_median6=statistics.median(secondv15501)
st_mode6=statistics.mode(secondv15501)
st_stdev6=statistics.stdev(secondv15501)


print('LIST WITH 15 CHOOSEN MARKS AMONG TOP 50 WITH <10 VALUE REPLACED DATA:\n',
	'mean:',st_mean6,'\t','mode:',st_mode6,'\t','median:',st_median6,'\n',
	'max:',max(secondv15501),'\t','min:',min(secondv15501),'\n','standard deviation:',st_stdev6)
print('----------------------------------------------')	 

#plot
plt.plot(marks_list)
plt.plot(secondv15501)
plt.xlabel("student's number")
plt.ylabel("student's mark")
plt.title("changing 15 marks among top 50 with <10 value")
chart_path='D:\\FARIMA st_results\plots\ 8-15marks among top 50 less than 10.png'
plt.savefig(chart_path)
plt.show()

#---------------------------------------------------------------------------------------------------------
#Q15&16 : add -2 or +2 to all of them
marks_list15=marks_list.copy()

#number of indexes to remove
choose=random.randint(1,1000)
#indexes to remove from first list
removal_indexes=random.sample(range(1000),choose)
new15=[]
values15=[]

#put values of removal indexes into a seperate list
for i in removal_indexes:
	values15.append(marks_list[i])

for i in range(0,len(values15)):
	values15[i]=values15[i]+2

#>0 and >20	

marks_list15=[i for j, i in enumerate(marks_list15) if j not in removal_indexes]

for i in range(0,len(marks_list15)):
	marks_list15[i]=marks_list15[i]-2

new15=marks_list15+values15

st_mean7=statistics.mean(new15)
st_median7=statistics.median(new15)
st_mode7=statistics.mode(new15)
st_stdev7=statistics.stdev(new15)


print('LIST WITH 15 MARKS CHOOSEN TO *2 OR *(-2):\n',
	'mean:',st_mean7,'\t','mode:',st_mode7,'\t','median:',st_median7,'\n',
	'max:',max(new15),'\t','min:',min(new15),'\n','standard deviation:',st_stdev7)
print('----------------------------------------------')	

#plot
plt.plot(marks_list)
plt.plot(new15)
plt.xlabel("student's number")
plt.ylabel("student's mark")
plt.title("add -2 or +2 to all of them")
chart_path='D:\\FARIMA st_results\plots\ 9-add +-2 to all.png'
plt.savefig(chart_path)
plt.show()

#---------------------------------------------------------------------------------------------------------

#enter data in a csv file
with open('D:\\FARIMA st_results\student_info.csv','a') as f:
	f.write("FIRST LIST\'S DATA:\n")
	for key, value in st_info(st_mean,st_median,st_mode,st_stdev).items(): 
		f.write('%s:%s\n' % (key, value))
	f.write("LIST WITH 100 CHOOSEN MARK TO REPLACE:\n")
	for key, value in st_info(st_mean2,st_median2,st_mode2,st_stdev2).items(): 
		f.write('%s:%s\n' % (key, value))
	f.write("LIST WITH 15 CHOOSEN MARKS WITH 18> VALUE REPLACED DATA:\n")
	for key, value in st_info(st_mean3,st_median3,st_mode3,st_stdev3).items(): 
		f.write('%s:%s\n' % (key, value))
	f.write("LIST WITH 15 CHOOSEN MARKS AMONG DOWN 50 WITH 18> VALUE REPLACED DATA:\n")
	for key, value in st_info(st_mean4,st_median4,st_mode4,st_stdev4).items(): 
		f.write('%s:%s\n' % (key, value))
	f.write("LIST WITH 15 CHOOSEN MARKS WITH <10 VALUE REPLACED DATA:\n")
	for key, value in st_info(st_mean5,st_median5,st_mode5,st_stdev5).items(): 
		f.write('%s:%s\n' % (key, value))
	f.write("LIST WITH 15 CHOOSEN MARKS AMONG TOP 50 WITH <10 VALUE REPLACED DATA:\n")
	for key, value in st_info(st_mean6,st_median6,st_mode6,st_stdev6).items(): 
		f.write('%s:%s\n' % (key, value))
	f.write("LIST WITH 15 MARKS CHOOSEN TO *2 OR *(-2):\n")
	for key, value in st_info(st_mean7,st_median7,st_mode7,st_stdev7).items(): 
		f.write('%s:%s\n' % (key, value))


#---------------------------------------------------------------------------------------------------------
#Q20

marks=marks_list.copy()

#each group with percentage of students

def grouping(st_marks):
	
	#A,B,C,D,E,F
	A,B,C,D,E,F=[],[],[],[],[],[]

	for i in st_marks:
		if i>=0.00 and i<10:
			F.append(i)
		elif i>=10.00 and i<12:
			E.append(i)
		elif i>=12.00 and i<14:
			D.append(i)
		elif i>=14.00 and i<16:
			C.append(i)	
		elif i>=16.00 and i<18:
			B.append(i)	
		elif i>=18.00 and i<=20.00:
			A.append(i)

	gp_dict={'A':"{:.2f}".format(len(A)*0.1),'B':"{:.2f}".format(len(B)*0.1),
			'C':"{:.2f}".format(len(C)*0.1),'D':"{:.2f}".format(len(D)*0.1),
			'E':"{:.2f}".format(len(E)*0.1),'F':"{:.2f}".format(len(F)*0.1)}

	

	with open('D:\\FARIMA st_results\groupingA.csv','a',newline="") as f:
		writer = csv.writer(f)
		# writer.writerow(['groups', 'percentage'])
		for key, value in gp_dict.items():
        	 writer.writerow([key, value])
		f.write("\n")
	return 	f	 

#seeing result after 10 times of excecution 



# for i in range(0,10):
	#respectively first list , changing 100 marks randomly
	#change 15marks to >18 , change 15marks from down 50 to >18
	#change 15marks to <10 , change 15marks from top 50 to <10
	#add -2 or +2 to all marks
	
grouping(marks_list)	
grouping(new_marks100)
grouping(new_marks15)
grouping(secondv1550)
grouping(new_marks151)
grouping(secondv15501)
grouping(new15)



#top 10%
marks.sort(reverse=True)
top_10per=[]
for i in range(0,100):
	top_10per.append(marks[i])

# print(top_10per)