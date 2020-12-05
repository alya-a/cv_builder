from vars import nationalities,marital_status_list,levels_of_study #import variable and lists

def hs():#ask user for high school name and graduation year
  high_school=(input("High school name: "))
  hs_grad_year=(input("High school graduation year: "))
  hs_gpa=(input("High school GPA: "))

def uni():#ask user for university name,enrollment year,graduation year, major,gpa
  uni_name=(input("University Name: "))
  uni_enroll_year=(input("University Enrollment Year: "))
  uni_grad_year=(input("University Graduation Year: "))
  uni_major=(input("University Major: "))
  uni_gpa=(input("University GPA: "))

def training():#ask user for name of training institution,enrollment year, graduation year
  training_school=(input("Name of the training institution: "))
  ts_enroll_year=(input("Training enrollment year: "))
  ts_grad_year=(input("Training graduation year: "))

def job(): #ask user for job experience details (employer,job title, star/end date)
  employer=(input("Employer: "))
  job_title=(input("Job Title: "))
  start_date=(input("Start Date: "))
  end_date=(input("End Date: "))

def lang():#ask user for language and level
  language=(input("Language: "))
  level=(input("Level: "))

print("\n\nPlease enter the following information: \n\n")
first_name=(input("First name: "))
last_name=(input("Last name: "))
dob=(input("Date of birth (dd-mm-yyyy): "))
while len(dob)!=10:
  dob=(input("Invalid. Please input your date of birth in the following format: dd-mm-yyyy (example: 11-01-2000) "))
nationality=(input("Nationality: "))
while nationality not in nationalities:
  nationality=(input("Invalid input. Please select your nationality: "))
marital_status=(input("Please enter your marital status: "))
while marital_status not in marital_status_list:
  marital_status=(input("Invalid input. Please enter your marital status: "))
phone=(input("Mobile number: "))
email=(input("Email address: "))
while "@" and "." not in email:
    email=(input("Invalid input. Please enter a valid email address: "))
linkdin=(input("Do you have a LinkedIn account? "))
if linkdin=="yes"and"Yes":
  linkdinurl=input("Please enter your LinkedIn URL: ")
driver=(input("Do you have a driver's license? "))
if driver=="yes"and"Yes":
  license_cat=(input("Please enter your driver license category: "))
print("\nPlease select your highest level of education (1-10): ")
for a in levels_of_study:
  print(a)
sel_edu_level=(input("\nHighest level of education: "))
work_ex=(input("Do you have work experience?: "))
if work_ex=="yes"and"Yes":
  num_jobs=int(input("How many jobs have you worked?: "))
languages=int(input("How many languages do you speak?: "))
comp_skills=(input("Do you have any computer skills?: "))
if comp_skills=="yes"and"Yes":
  num_comp_skills=int(input("How many computer skills do you have?: "))
other_skills=(input("Do you have any other skills?: "))
if other_skills=="yes"and"Yes":
  num_other_skills=int(input("How many other skills do you have?: "))

print("\n \n \n=====PERSONAL INFORMATION===== \n")
print("First Name: ", first_name)
print("Last Name: ", last_name)
print("Date of Birth: ", dob)
print("Nationality: ", nationality)
print("Marital Status: ", marital_status)
if driver=="yes"and"Yes":
  print("Driver's License Category: ",license_cat)
if driver=="no"and"No":
  print("Driver's License: No")
print("\n=====CONTACT INFORMATION=====\n")
print("Email Address: ", email)
print("Phone Number: ", phone)
if linkdin=="yes"and"Yes":
  print("LinkedIn URL: ",linkdinurl)
print("\n==========EDUCATION==========\n")

#according to the users selected edu level, the following applies:
if sel_edu_level=="1":
  print("No schooling completed")
elif sel_edu_level=="2":
  print("Middle School")
elif sel_edu_level=="3":
 print("High School, no diploma")
elif sel_edu_level=="4":#high school graduate
  print("-High School Diploma-")
  hs()#recall func to get high school info
elif sel_edu_level=="5":#didn't complete university yet
  print("-Incomplete University Degree-")
  uni_name=(input("University name: "))
  uni_enroll_year=(input("University enrollment year: "))
  uni_major=(input("University major: "))
  print("\n-High School Diploma-")
  hs()#recall func to get high school info
elif sel_edu_level=="6":#training graduate
  print("-Training Certificate-")
  training()#recall func to get training info
  print("\n-High School Diploma-")
  hs()#recall func to get high school info
elif sel_edu_level=="7":#associate degree graduate
  print("-Associate Degree-")
  uni()#recall func to get university
  print("\n-High School Diploma-")
  hs()#recall func to get high school info
elif sel_edu_level=="8":#bachelors degree graduate
  print("-Bachelor's Degree-")
  uni()#recall func to get bachelor degree info
  print("\n-High School Diploma-")
  hs()#recall func to get high school info
elif sel_edu_level=="9":#masters degree graduate
  print("-Master's Degree-")
  uni()#recall func to get masters degree info
  print("\n-Bachelor's Degree-")
  uni()#recall func to get bachelor degree info
  print("\n-High School Diploma-")
  hs()#recall func to get high school info
elif sel_edu_level=="10":#phd graduate
  print("-Doctorate Degree-")
  uni()#recall func to get phd info
  print("\n-Master's Degree-")
  uni()#recall func to get masters degree info
  print("\n-Bachelor's Degree-")
  uni()#recall func to get bachelor degree info
  print("\n-High School Diploma-")
  hs()#recall func to get high school info


print("\n========JOB EXPERIENCE========\n")
if work_ex=="yes"and"Yes":
  if num_jobs>0:
    count=0
    while count<num_jobs:
      print("\n-Job Info-")
      job()#recall func to get work details
      "\n"
      num_jobs=num_jobs-1
elif work_ex=="no"and"No":
  print("No previous work experience")

print("\n============SKILLS============\n")
print("\n-------Language Skills-------")
if languages>0:
  count=0
  while count<languages:
    print("\n")
    lang()#recall func to get users language info
    languages=languages-1

print("\n--------Computer Skills--------")
if comp_skills=="yes"and"Yes":
  if num_comp_skills>0:
    count=0
    while count<num_comp_skills:
      comp_skill=(input("- "))#user lists computer skills
      num_comp_skills=num_comp_skills-1
elif comp_skills=="no"and"No":
  print("\nNo Computer Skills")

if other_skills=="yes"and"Yes":
  print("\n---------Other Skills---------")
  if num_other_skills>0:
    count=0
    while count<num_other_skills:
      other_skill=(input("- "))#user lists other skills
      num_other_skills=num_other_skills-1
elif other_skills=="no"and"No":
  print("\n")

print("==============================")
