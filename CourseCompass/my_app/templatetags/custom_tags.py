from django import template
register = template.Library()

# @register.simple_tag
#def grab_data(data):
#	return "<h3>HI</h3>"

@register.simple_tag
def grab_data(data):
# def write_data(data):
	ids = []
	for d in data:
		for j in d.json_data:
			ids.append(j)

	#file = open("catalog_page.html", "w")
	output = ""
	for d in data:
		for i in ids:
			if output == "":
				output = '<div class="course-card">'
			else:
				output += '<div class="course-card">'
			#file.write('<div class="course-card">')
			title = d.json_data[i]["title"]
			string = f'<h3> {title} </h3>'
			output += string
			#file.write(string)
			#file.write('<div class="course-details">')

			output += '<div class="course-details">'

			credit_hr = d.json_data[i]["billing"]["maximum"]
			string = f'<p> {credit_hr} </p>'
			output += string
			#file.write(string)
			#file.write('</div>')
			output += '</div>'
			output += '</div>'
			#file.write('</div>')

	#file.close()
	#with open("catelog_page.html", "w") as file:
	#	file.write(output)
	#	file.close()
	return output

