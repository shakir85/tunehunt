from jinja2 import Template

# Load the Jinja template from a file
with open('template.jinja') as file:
    template = Template(file.read())

# Define the values for the variables
context = {
    'name': 'John Doe',
    'age': 25
}

# Render the template with the provided context
output = template.render(context)

# Print the rendered output
print(output)
