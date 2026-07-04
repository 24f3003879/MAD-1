from jinja2 import Template


template = Template("Hello {{ name }}")




result = template.render(name="Shubh")


print(result)


