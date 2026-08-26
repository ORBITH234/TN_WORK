def grade_label(score):
    # Bug to fix: branch order and boundary checks must be correct.
    score = int(input("enter your score: \n"))


    if score < 0 or score > 100:
          return "Invalid score"
    elif score >= 90 and score <= 100 :
        return "A"
    elif score >= 80 and score <= 89 :
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    else :
        return "F"
  



# print(grade_label("enter your score :"))

grade = grade_label("score")
print(grade)
# print(grade_label(""))
