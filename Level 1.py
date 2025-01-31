import numpy as np

#5  vari test w weight

u1 = np.zeros([2,5])

# QUES 1

l1 = (0)

while l1 == (0):

 print('1.Political alignment \n a.Left \n b.right')
 a1=input("")

 if a1 =='a':
  u1[0,0] = 1
  l1 = 1

 elif a1 =='b':
  u1[0,0] = 2
  l1 = 1

 else:
     l1 = 0
     print('please select an option')

print('_'*40)

# QUES 2

l2 = (0)

while l2 == (0):

 print('2.Gender \n a.Male \n b.Female')
 a2=input("")

 if a2 =='a':
  u1[0,1] = 1
  l2 = 1

 elif a2 =='b':
  u1[0,1] = 2
  l2 = 1

 else:
     l1 = 0
     print('please select an option')

print('_'*40)

# QUES 3

l3 = (0)

while l3 == (0):

 print('3.Monthly income \n a.0-3k \n b.3k-5k \n c.5k-8k \n d.8k-12k \n e.12k and above \n f.Does not matter')
 a3=input("")

 if a3 =='a':
  u1[0,2] = 1
  l3 = 1

 elif a3 =='b':
  u1[0,2] = 2
  l3 = 1

 elif a3 =='c':
  u1[0,2] = 3
  l3 = 1

 elif a3 =='d':
  u1[0,2] = 4
  l3 = 1

 elif a3 =='e':
  u1[0, 2] = 5
  l3 = 1

 elif a3 =='f':
  u1[0, 2] = 6
  l3 = 1

 else:
     l1 = 0
     print('please select an option')

print('_'*40)

# QUES 4

l4 = (0)

while l4 == (0):

 print('4.Height in cm \n a.140-150 \n b.150-160 \n c.160-170 \n d.170-180 \n e.180 and above \n f.Does not matter')
 a4=input("")

 if a4 =='a':
  u1[0,3] = 1
  l4 = 1

 elif a4 =='b':
  u1[0,3] = 2
  l4 = 1

 elif a4 =='c':
  u1[0,3] = 3
  l4 = 1

 elif a4 =='d':
  u1[0,3] = 4
  l4 = 1

 elif a4 =='e':
  u1[0, 3] = 5
  l4 = 1

 elif a4 =='f':
  u1[0, 3] = 6
  l4 = 1

 else:
     l4 = 0
     print('please select an option')

print('_'*40)

# QUES 5

l5 = (0)

while l5 == (0):

 print('5.interests \n a.Reading \n b.Music \n c.Making music \n d.Gaming \n e.Sports \n f.Food \n g.others')
 a5=input("")

 if a5 =='a':
  u1[0,4] = 1
  l5 = 1

 elif a5 =='b':
  u1[0,4] = 2
  l5 = 1

 elif a5 =='c':
  u1[0,4] = 3
  l5 = 1

 elif a5 =='d':
  u1[0,4] = 4
  l5 = 1

 elif a5 =='e':
  u1[0, 4] = 5
  l5 = 1

 elif a5 =='f':
  u1[0, 4] = 6
  l5 = 1

 elif a5 =='g':
  u1[0, 4] = 7
  l5 = 1

 else:
     l4 = 0
     print('please select an option')

print('_'*40)

# CHECK WEIGHT QUESTION

print('Please input the order of importance of the questions asked previously')

print('a.Political alignment \n b.Gender \n c.Income \n d.Height \n e.Interests')

uw1 = np.zeros([1,5])

w1 = input('Most important : ')

# WEIGHT 1

