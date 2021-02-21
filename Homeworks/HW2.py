'''Write a program that includes information about the grades of 
5 students in a school.
(take student's info from user)
- Keep these student's midterm, final, homework 
(at some point find average)
- Keep student' names (Names, Surname) in a list.
- Create a dictionary named info and put all the info of students
in a dictionary.
- Sort and list the students' grades here in descending order and
congratulate the student with the highest score.
(use for loops)'''

Std1_name = input('Enter first student\'s name and surname: ')
Std2_name = input('Enter second student\'s name and surname: ')
Std3_name = input('Enter third student\'s name and surname: ')
Std4_name = input('Enter fourth student\'s name and surname: ')
Std5_name = input('Enter fifth student\'s name and surname: ')

Std1_mid = int(input('Enter first student\'s midterm score: '))
Std2_mid = int(input('Enter second student\'s midterm score: '))
Std3_mid = int(input('Enter third student\'s midterm score: '))
Std4_mid = int(input('Enter fourth student\'s midterm score: '))
Std5_mid = int(input('Enter fifth student\'s midterm score: '))

Std1_fin = int(input('Enter first student\'s final exam score: '))
Std2_fin = int(input('Enter second student\'s final exam score: '))
Std3_fin = int(input('Enter third student\'s final exam score: '))
Std4_fin = int(input('Enter fourth student\'s final exam score: '))
Std5_fin = int(input('Enter fifth student\'s final exam score: '))

Std1_hw = int(input('Enter first student\'s homework score: '))
Std2_hw = int(input('Enter second student\'s homework score: '))
Std3_hw = int(input('Enter third student\'s homework score: '))
Std4_hw = int(input('Enter fourth student\'s homework score: '))
Std5_hw = int(input('Enter fifth student\'s homework score: '))

Std1_avg = str(int((Std1_mid + Std1_fin + Std1_hw) / 3))
Std2_avg = str(int((Std2_mid + Std2_fin + Std2_hw) / 3))
Std3_avg = str(int((Std3_mid + Std3_fin + Std3_hw) / 3))
Std4_avg = str(int((Std4_mid + Std4_fin + Std4_hw) / 3))
Std5_avg = str(int((Std5_mid + Std5_fin + Std5_hw) / 3))

info = {Std1_name:Std1_avg, Std2_name:Std2_avg, Std3_name:Std3_avg, Std4_name:Std4_avg, Std5_name:Std5_avg}


#print(info) # to check whether the code is working
#print(type(info))
#print(Std1_avg, Std2_avg, Std3_avg, Std4_avg, Std5_avg) # to check whether the code is working

sorted_info = sorted(info.items(), key = lambda x: x[1], reverse = True)
print(sorted_info)
#print(type(sorted_info))

print("Congratulations " + str(sorted_info[0][0]) + "!")

# I did not use a for loop :(
