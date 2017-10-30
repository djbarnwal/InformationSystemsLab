# Program to get analysing student marks for different subjects.

import numpy as np

# Generating array for 10 students and 6 subjects
A = np.random.randint(low=0, high=101, size=(10,6))

try:
    choice = int(input("Enter your choice\n"
                      "1) Students with highest and lowest total marks\n"
                      "2) Subjects with highest and lowest average score\n"
                      "3) Student with highest score across all subjects\n"))
except:
    print("Please input an integer")

print("The matrix with random numbers is\n", A)

sumList = np.zeros(6)
topperList = np.zeros(10)

studentNum = 0
subjectNum = 0

sumList = A.sum(axis=0)
topperList = A.sum(axis=1)


def menu(mat, choice) :
    
    if choice == 3 :
        if int(np.argmin(mat)%6) is not 0:
            print('Student No.{} scored the lowest in Subject No.{} ie. {}'.format(int(np.argmin(mat)/6),np.argmin(mat)%6+1,A[int(np.argmin(mat)/6),np.argmin(mat)%6]))
        if int(np.argmin(mat)%6) == 0:
            print('Student No.{} scored the lowest in Subject No.{} ie. {}'.format(int(np.argmin(mat)/6)+1,np.argmin(mat)%6+1,A[int(np.argmin(mat)/6),np.argmin(mat)%6]))
        if int(np.argmax(mat)%6) is not 0:
            print('Student No.{} scored the highest in Subject No.{} ie. {}'.format(int(np.argmax(mat)/6)+1,np.argmax(mat)%6+1,A[int(np.argmax(mat)/6),np.argmax(mat)%6]))
        if int(np.argmax(mat)%6) == 0:
            print('Student No.{} scored the highest in Subject No.{}'.format(int(np.argmax(mat)/6),np.argmax(mat)%6+1),A[int(np.argmax(mat)/6),np.argmax(mat)%6])

    if choice == 2 :
        print('Subject with lowest average is {} with an average of {}\n'
              'Subject with highest average is {} with an average of {}'.format(np.argmin(sumList)+1,min(sumList)/10,np.argmax(sumList)+1,max(sumList)/10))
        
    if choice == 1 :
        print('Student No.{} has secured highest marks ie. {} out of 600'.format(np.argmax(topperList)+1,max(topperList)))
        print('Student No.{} has secured lowest marks ie. {} out of 600'.format(np.argmin(topperList)+1,min(topperList)))
        


menu(A,choice)
