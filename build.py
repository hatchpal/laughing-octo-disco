
#--------------------------------------

# print('This is working')

# def main():

# 	top = ("template/top.html")
# 	bottom = ("template/bottom.html")
# 	about = ("content/about.html")
# 	experience = ("content/experience.html")
# 	skills = ("content/skills.html")
# 	contact = ("content/contact.html")

# #Combine top.html and bottom.html into base.html with {{content}}
# 	top_template = open(top).read()
# 	bottom_template = open(bottom).read()
# 	base_template = top_template + "{{content}}" + bottom_template
# 	open('template/base.html', 'w+').write(base_template)

# if __name__ == "__main__":
# 	main()


# write in base.html the navigation links

template = open("template/base.html").read()


#read files in the content directory

import glob
all_html_files = glob.glob("content/*.html")

i=0
pages = []
template = open("template/base.html").read()
navbar = ""
navbar_output = ""
add_navbar = []
combined_base = ""
filename = {}

# create the auto-generated list:
for html_file in all_html_files:

	import os

	file_path = all_html_files[i]
	file_name = os.path.basename(file_path)
	i = i+1

	name_only, extension = os.path.splitext(file_name)

	path = "content/index.html"
	

	pages.append({
		"filename": "content/" + file_name,
		"title":"" + name_only + "",
		"output": "docs/" + file_name,
	})

	# create the auto-generated navigation bar:
	add_navbar = '<li class="nav-item"> ' + '<a class="nav-link js-scroll-trigger" href="' + file_name + '#' + name_only + '">' + name_only + '</a> ' + '</li>'
	navbar_output = navbar_output + '\n' + add_navbar 

# write the auto-generated navbar in the base template:
template = template.replace("{{navbar}}", navbar_output)


#combine the base template with the content and title:
for page in pages:
	filename = open(page['filename']).read()	
	combined_file = template.replace("{{content}}", filename)
	combined_file = combined_file.replace("{{title}}", page['title']) 
	open(page['output'], 'w+').write(combined_file)


#---------------------------------------

