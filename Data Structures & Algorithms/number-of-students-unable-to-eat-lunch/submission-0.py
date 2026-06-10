class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # top of stack is at beginning of array
        # so pop(0) and insert(0) instead of pop() and append(
        
        count = 0
        while len(students) > 0 and len(sandwiches) > 0:
            if count == len(students) + 1:
                break
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                count = 0 # restart counter
            else:
                students.append(students.pop(0)) # back to the end of the line you go
            count += 1
        return len(students)