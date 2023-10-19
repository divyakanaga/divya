class Student:

  def __init__(self,name,roll_number,cgpa):
       self.name = name
       self.roll_number = roll_number
       self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list,
                            key =lambda student: student.cgpa,
                            reverse = True)
    return sorted_students
students = [
    Student("Adline","A123",9.9),
    Student("Anu","A124",9.4),
    Student("Apoorvaa","A125",8.9),
    Student("Banupriya","A126",9.1),
]

sorted_students = sort_students(students)

for student in sorted_students:

 print("Name: {} ,Rollno: {} ,CGPA: {} ".format(student.name,student.roll_number,student.cgpa))


def linearSearchProduct(productList,targetProduct):
    indices = []

    for index,product in enumerate(productList):
      if product == targetProduct:
       indices.append(index)

    return indices

  #Example Usages:
product =["shoes","boots","loafer","shoes","converse","shoes"]

target = "shoes"
result = linearSearchProduct(product,target)
print(result)