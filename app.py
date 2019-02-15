blogs = {}


def menu():
	# Show the user the available blogs
	# Let the user make a choice
	# Do something with that choice
	# Eventually exit
	print_blogs()


def print_blogs():
	""" Print available blogs"""
	for key, blog in blogs.items():  # (blog_name, Blog), (blog_name1, Blog1)
		print('- {}'.format(blog))
