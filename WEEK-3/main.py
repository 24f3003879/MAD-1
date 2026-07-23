from string import Template
my_statemenet = Template("Today is $today and tomorrow is $tomorrow.")
out = my_statemenet.substitute(today = "Modday", tomorrow = "dkjd")
print(out)