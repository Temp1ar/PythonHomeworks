#!/usr/bin/env python
# coding: UTF-8
#import copy

class Database:
	def __init__(self, filename):
		self.__filename = filename
		self.__list = []
		file = open(self.__filename)
		for line in file.read().split("\n"):
			self.__list.append(Student(line))
	
	def getStudent(self, name):
		for student in self.__list:
			if student.getName() == name:
				return student				
		return
	
	def addStudent(self, str):
		student = Student(str)
		return self.__list.append(student)
		
	def removeStudent(self, str):
		student = Student(str)
		found = self.getStudent(str)
		if found:
			self.__list.remove(found)
			
	def writeDatabase(self, dest = ""):
		dest = dest if len(dest) > 0 else self.__filename
		file = open(dest, 'w')
		for student in self.__list:
			file.write(student.__repr__() + "\n")
	
	def getSmartest(self):
		averages = [x.computeAverage() for x in self.__list]
		maxAverage = max(averages)
		return self.__list[averages.index(maxAverage)]
		
class Student:
	def __init__(self, string):
		if string.count(":") > 0:
			words = string.split(":");
			self.__name = words[0].strip();
			self.__marks = [int(x) for x in words[1].strip().split(" ")]
		else:
			self.__name = string
			self.__marks = []
	
	def __repr__(self):
		return self.__name + ": " + " ".join([str(x) for x in self.__marks])
	
	def getName(self):
		return self.__name
	
	def getMarks(self):
		return self.__marks
		
	def computeAverage(self):
		return sum(self.__marks, 0.0) / len(self.__marks)
		
	def addMark(self, mark):
		return self.__marks.append(mark)

db = Database("bd.txt")
st = Student("Вася Пупкин")
print st

Vasya = db.getStudent(st.getName())
print Vasya

db.removeStudent("Вася Пупкин")
db.addStudent("Вася Пупкинс:3 4 5 1")
print "Самый умный студент —", db.getSmartest()
db.writeDatabase("bd2.txt")

