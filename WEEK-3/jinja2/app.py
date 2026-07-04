from jinja2 import Template

my_statement = Template("These are the special numbers are:  {% for n in range(11) if n%2 == 0 %} {{n%3}}" "{% endfor %}")
out = my_statement.render()
print(out)