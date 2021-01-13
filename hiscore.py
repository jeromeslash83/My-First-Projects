student_scores = input("Input a list of student scores ").split()
while True:  
  for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
  print(student_scores)
  x = student_scores[0]
  for score in student_scores:
    if score > x:
      x = score
  print(f'The highest score in the class is: {x}')
  continuation = input('Do you want to continue? (y/n)')
  if continuation == 'y':
    continue
  elif continuation == 'n':
    break
  else:
    print('Wrong input. Try again')
