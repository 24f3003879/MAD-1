from jinja2 import Template

statement_1 = Template("IIT Madras provides eduction in {{value_1}} {{value_2}}")
statement_2 = Template("IIT Madras provides degree in {{value_1}} {{value_2}}")
out_1 = statement_1.render(value_1 = "Programming")
out_2 = statement_2.render(value_2 = "Data Science")
print(out_1)
print(out_2)