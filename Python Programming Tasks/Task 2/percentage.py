if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for name, scores in student_marks.items():
        if name==query_name:
            AVG= (scores[0]+scores[1]+scores[2])/3
            print("{:.2f}".format(AVG))