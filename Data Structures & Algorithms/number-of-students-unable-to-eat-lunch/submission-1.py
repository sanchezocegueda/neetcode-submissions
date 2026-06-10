from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # top of stack is at beginning of array
        # so pop(0) and insert(0) instead of pop() and append(
        q_students, q_sandwiches = deque(students), deque(sandwiches)
        
        count = 0
        while count < len(q_students):
            
            if q_students[0] == q_sandwiches[0]:
                q_students.popleft()
                q_sandwiches.popleft()
                count = 0 # restart counter
            else:
                q_students.append(q_students.popleft()) # back to the end of the line you go
                count += 1
        return len(q_students)