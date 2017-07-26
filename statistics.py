grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print("%s" % grade)

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return round(total, 2)
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return round(average, 4)

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    result = variance / len(scores)
    return round(result, 4)

def grades_std_deviation(variance):
    return round((variance ** 0.5), 4)

if __name__ == '__main__':
    assert grades_sum(grades) == 1045.5
    assert grades_average(grades) == 80.4231
    assert grades_variance(grades) == 334.0710
    assert grades_std_deviation(grades_variance(grades)) == 18.2776
