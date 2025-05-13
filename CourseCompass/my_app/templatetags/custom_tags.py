from django import template
register = template.Library()

# @register.simple_tag
#def grab_data(data):
#	return "<h3>HI</h3>"

def term_value(date):
	term_intiger = date[5:6]

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
			number = d.json_data[i]["number"]
			string = f'<h3> {number}: {title} </h3>'
			output += string
			#file.write(string)
			#file.write('<div class="course-details">')

			output += '<div class="course-details">'

			description = d.json_data[i]["description"]
			string = f'<p><strong>Description:</strong> {description}</p>'
			output += string

			credit_hr_max = d.json_data[i]["billing"]["maximum"]
			string = f'<p><strong>Maximum Credit Hours:</strong> {credit_hr_max}</p>'
			output += string

			credit_hr_min = d.json_data[i]["billing"]["minimum"]
			string = f'<p><strong>Minimum Credit Hours:</strong> {credit_hr_min}</p>'
			output += string

			course_ID = d.json_data[i]["id"]
			string = f'<p><strong>Course ID:</strong> {course_ID}</p>'
			output += string

			#location = d.json_data[i]["reportingDetail"]["type"]
			#string = f'<p><strong>Location:</strong> {location}</p>'
			#output += string

			start_date = d.json_data[i]["schedulingStartOn"][0:10]
			string = f'<p><strong>Start Date:</strong> {start_date}</p>'
			output += string

			end_date = d.json_data[i]["schedulingEndOn"][0:10]
			string = f'<p><strong>End Date:</strong> {end_date}</p>'
			output += string

			#start_date = d.json_data[i]["schedulingStartOn"][0:10]
			#string = f'<p><strong>Start Date:</strong> {start_date}</p>'
			#output += string

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

