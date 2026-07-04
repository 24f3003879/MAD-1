import csv
import sys
from jinja2 import Template
import matplotlib.pyplot as plt

student_template = """
<!DOCTYPE html>
<html>
  <head>
    <title>Student Data</title>
  </head>

  <body>
    <h1>Student Details </h1>
    <table border="1">
      <tr>
        <th>Student id</th>
        <th>Course id</th>
        <th>Total Marks</th>
      </tr>
      {% for row in rows %}
      <tr>
        <td>{{ row[0] }}</td>
        <td>{{ row[1] }}</td>
        <td>{{ row[2] }}</td>
      </tr>
      {% endfor %}
      <tr>
        <td colspan="2"><strong>Total</strong></td>
        <td><strong>{{ total }}</strong></td>
      </tr>
    </table>
  </body>
</html>


"""

course_template = """
<!DOCTYPE html>
<html>
  <head>
    <title>Course Data</title>
  </head>

  <body>
    <h1>Course Details</h1>
    <table border="1">
      <tr>
        <th>Average Marks</th>
        <th>Maximum Marks</th>
      </tr>

      <tr>
        <td>{{ avg_marks }}</td>
        <td>{{ max_marks }}</td>
      </tr>
    </table>
    <img src="histogram.png">
  </body>
</html>

"""
error_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Something went wrong</title>
</head>

<body>

<h1>Wrong Inputs</h1>
<p>Something went wrong</p>

</body>
</html>

"""



#keeping user command line input in a list(user_input)
user_input = sys.argv

# Validate command-line arguments
if len(user_input) != 3 or user_input[1] not in ["-s", "-c"]:
    template = Template(error_template)
    html = template.render()

    with open("output.html", "w") as file:
        file.write(html)

    sys.exit()

matching_rows = []
marks = []


#reading csv file
with open("data.csv") as file:
    reader = csv.reader(file, skipinitialspace=True)
    next(reader)
    

    for row in reader:
        

        #filtering rows for student mode
        if user_input[1] == '-s' and user_input[2] == row[0]:
            matching_rows.append(row)
        # filtering rows for course mode
        elif user_input[1] == "-c" and row[1] == user_input[2]:
            matching_rows.append(row)
    
    if len(matching_rows) == 0:
        template = Template(error_template)
        html = template.render()

        with open("output.html", "w") as file:
            file.write(html)

        sys.exit()




if user_input[1] == "-s":

    total = 0

    for row in matching_rows:
        total += int(row[2])

    
    template = Template(student_template)

    html = template.render(
        rows=matching_rows,
        total=total
    )

    with open("output.html", "w") as file:
        file.write(html)  

elif user_input[1] == '-c':
    max_marks = 0
    avg_marks = 0
    marks = []

    
    for row in matching_rows:
        marks.append(int(row[2]))
    max_marks = max(marks)
    avg_marks = sum(marks)/len(marks)
   
    plt.clf()
    plt.hist(marks)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.savefig("histogram.png")
    plt.close()
    
    template = Template(course_template)
    html = template.render(
        max_marks = max_marks,
        avg_marks = avg_marks
    )
    with open("output.html", "w") as file:
        file.write(html)


        

