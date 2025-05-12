
def grab_data(data):
	ids = []
	for d in data:
		for j in d.json_data:
			ids.append(j)

	file = open("catalog_page.html", "w")
	for d in data:
		for i in ids:
			file.write('<div class="course-card">')
			title = d.json_data[i]["title"]
			file.write('<h3>' + title + '</h3>')
			file.write('<div class="course-details">')
			credit_hr = d.json_data[i]["billing"]["maximum"]
			file.write('<p>' + credit_hr + '</p>')
			file.write('</div>')
			file.write('</div>')

	file.close()


