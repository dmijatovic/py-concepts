
students=[]

class Student:
  def __init__(self, name):
    self.name = name
    self.marks=[]

  def addMark(self, mark):
    self.marks.append(mark)

  def calculateMeanMark(self):
    n = len(self.marks)
    if n == 0:
      return 0
    mean = sum(self.marks)/n
    return mean


def createStudent(name):
  student = Student(name)

def main():
  select = ""
  while select!='q':

    if select == 'a':
      name = input("What is student name? ")
      students.append(Student(name))

    elif select == 'm':
      name = input("Which student name? ")

      selectedStudent = None

      for student in students:
        if student.name == name:
          selectedStudent = student

      if selectedStudent:
        mark = input("Found student! What mark to give? ")
        selectedStudent.addMark(mark)
      else:
        print("No student with name {}. Adding mark failed".format(name))

    select = input("Select a to add, m to add mark and q to quit: ")

if __name__=="__main__":
  main()