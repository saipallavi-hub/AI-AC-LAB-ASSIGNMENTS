#Task 1: Sorting Student Records for Placement Drive
#Scenario:During campus placements SR University’s Training and Placement Cell needs to shortlist candidates efficiently tudent records must be sorted by CGPA in descending order.
#Tasks:1. Use GitHub Copilot to generate a program that stores student records (Name, Roll Number, CGPA). 2. Implement the following sorting algorithms using AI assistance:Quick Sort, Merge Sort 3. Measure and compare runtime performance for large datasets. 4. Write a function to display the top 10 students based on CGPA.
#Expected Outcome:Correctly sorted student records,Performance comparison between Quick Sort and Merge Sort,Clear output of top-performing students.
import random
import time

# Student class
class Student:
    def __init__(self, name, roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa

    def __repr__(self):
        return f"{self.name} ({self.roll}) - CGPA: {self.cgpa}"


# Generate sample data
def generate_students(n):
    students = []
    for i in range(n):
        students.append(Student(f"Student{i}", i, round(random.uniform(5.0, 10.0), 2)))
    return students


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2].cgpa
    left = [x for x in arr if x.cgpa > pivot]
    middle = [x for x in arr if x.cgpa == pivot]
    right = [x for x in arr if x.cgpa < pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].cgpa > right[j].cgpa:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Display top 10 students
def top_10(students):
    for s in students[:10]:
        print(s)


# MAIN
students = generate_students(1000)

start = time.time()
qs = quick_sort(students)
print("Quick Sort Time:", time.time() - start)

start = time.time()
ms = merge_sort(students)
print("Merge Sort Time:", time.time() - start)

print("\nTop 10 Students:")
top_10(qs)