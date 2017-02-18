# grades.awk -- average student grades and determine
# letter grade as well as class averages.
# $1 = student name; $2 - $NF = test scores.

# set output field separator to tab.
BEGIN { OFS = "\t" }

# action applied to all input lines
{
  # add up grades
	total = 0
	for (i = 2; i <= NF; ++i)
		total += $i
  # calculate average
	avg = total / (NF - 1)
  # assign student's average to element of array
	student_avg[NR] = avg
  # determine letter grade
	if (avg >= 90)  grade = "A"
	else if (avg >= 80) grade = "B"
	else if (avg >= 70) grade = "C"
	else if (avg >= 60) grade = "D"
	else grade = "F"
  # increment counter for letter grade array
	++class_grade[grade]
  # print student name, average and letter grade
	print $1, avg, grade
}
# print out class statistics
END {
  # calculate class average
	for (x = 1; x <= NR; x++)
		class_avg_total += student_avg[x]
	class_average = class_avg_total / NR
  # determine how many above/below average
	for (x = 1; x <= NR; x++)
		if (student_avg[x] >= class_average)
			++above_average
		else
			++below_average
  # print results
	print ""
	print "Class Average: ", class_average
	print "At or Above Average: ", above_average
	print "Below Average: ", below_average
  # print number of students per letter grade
	for (letter_grade in class_grade)
		print letter_grade ":", class_grade[letter_grade] | "sort"
}
