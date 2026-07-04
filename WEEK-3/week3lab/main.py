import csv
import sys
from jinja2 import Environment, FileSystemLoader
import matplotlib.pyplot as plt

#keeping user command line input in a list(user_input)
user_input = sys.argv

# Validate command-line arguments
if len(user_input) != 3 or user_input[1] not in ["-s", "-c"]:
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("error.html")
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
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("error.html")
        html = template.render()

        with open("output.html", "w") as file:
            file.write(html)

        sys.exit()




if user_input[1] == "-s":

    total = 0

    for row in matching_rows:
        total += int(row[2])

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("student.html")

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
    plt.savefig("histogram.png")
    
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("course.html")
    html = template.render(
        max_marks = max_marks,
        avg_marks = avg_marks
    )
    with open("output.html", "w") as file:
        file.write(html)


        

