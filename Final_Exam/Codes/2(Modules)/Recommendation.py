import json
import numpy as np
import os, sys
from numpy import vstack,array
from numpy.random import rand

source = os.path.dirname('CandidateProfileData/')
files = os.listdir(source)

CandidateID = []
Additional_Info = []
Skills = []
Work_Exp_Company = []
Work_Exp_Job_Description = []
Work_Exp_Job_Duration = []
Work_Exp_Job_Title = []
Location = []
Education_Institute = []
Education_School_Duration = []
Education_Qualification = []
Resume_Summary = []
count = []

for f in files:
	with open('Candidate_Profile_Data/'+f) as data_file:    
	    data = json.load(data_file)

	i = 0;
	while 1:
		try:
			CandidateID.append(int(data[i]["CandidateID"]))
			i+=1
		except:
			count.append(int(i))
			break
		try:
			Additional_Info.append(str(data[i]["Additional-Info"]))
		except:
			Additional_Info.append('-1')
		try:
			Skills.append(str(data[i]["Skills"]))
		except:
			Skills.append('-1')
		try:
			Work_Exp_Company.append(str(data[i]["Work-Experience"]["Company"]))
		except:
			Work_Exp_Company.append('-1')
		try:
			Work_Exp_Job_Description.append(str(data[i]["Work-Experience"]["Job-Description"]))
		except:
			Work_Exp_Job_Description.append('-1')
		try:
			Work_Exp_Job_Duration.append(str(data[i]["Work-Experience"]["Job-Duration"]))
		except:
			Work_Exp_Job_Duration.append('-1')
		try:
			Work_Exp_Job_Title.append(str(data[i]["Work-Experience"]["Job Title"]))
		except:
			Work_Exp_Job_Title.append('-1')
		try:
			Location.append(str(data[i]["Location"]))
		except:
			Location.append('-1')
		try:
			Education_Institute.append(str(data[i]["Education"]["Institute"]))
		except:
			Education_Institute.append('-1')
		try:
			Education_School_Duration.append(str(data[i]["Education"]["School-Duration"]))
		except:
			Education_School_Duration.append('-1')
		try:
			Education_Qualification.append(str(data[i]["Education"]["Qualification"]))
		except:
			Education_Qualification.append('-1')
		try:
			Resume_Summary.append(str(data[i]["Resume-Summary"]))
		except:
			Resume_Summary.append('-1')



#CandidateID.sort()
choice = 1
print 'Select any one approach:'
while 1:
	print 'Enter 1: Get career path'
	print 'Enter 2 : Get skills based on career goals'
	print 'Enter 0 : Exit'
	choice = raw_input()
	output = []
	count = 0

	if int(choice) == 1:
		print 'Enter educational institute :'
		institute = raw_input()
		print 'Enter educational qualification :'
		qualification = raw_input()
		print 'Enter the location :'
		location = raw_input()
		for i in Education_Qualification:
			if i.find(qualification)>=0:
				output.append(count)
			count+=1
		count = 0
		for i in Education_Institute:
			if i.find(institute)>=0:
				output.append(count)
			count+=1
		count = 0
		for i in Location:
			if i.find(location)>=0:
				output.append(count)
			count+=1
		output.sort()
		freq = []
		for w in output:
			freq.append(output.count(w))
		maximum = max(freq)
		print maximum
		count = 0
		for i in freq:
			if i == maximum:
				print Skills[output[count]]
				break
			count+=1

		
	elif int(choice) == 2:
		print 'Enter your career goal: '
		career = raw_input()
		for i in Work_Exp_Job_Title:
			if i.find(career)>=0:
				output.append(count)
			count+=1
		print Skills[output[0]]
	elif int(choice) == 0:
		break
	else:
		print '\nPlease Enter the correct choice\n'


