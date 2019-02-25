from blog import Blog
from post import Post

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: '
POST_TEMPLATE = '{} {}'

blogs = {}


def menu():
	# Show the user the available blogs
	# Let the user make a choice
	# Do something with that choice
	# Eventually exit
	print_blogs()
	selection = input(MENU_PROMPT)
	while selection != 'q':
		if selection == 'c':
			ask_create_blog()
		elif selection == 'l':
			print_blogs()
		elif selection == 'r':
			ask_read_blog()
		elif selection == 'p':
			ask_create_post()
		selection = input(MENU_PROMPT)


def print_blogs():
	""" Print available blogs"""
	for key, blog in blogs.items():  # (blog_name, Blog), (blog_name1, Blog1)
		print('- {}'.format(blog))


def ask_create_blog():
	title = input('Please input blog title: ')
	author = input('Please input author title: ')
	blogs[title] = Blog(title, author)


def ask_read_blog():
	blog_title1 = input('Please, enter blog title: ')

	print(print_posts(blogs[blog_title1]))


def print_posts(blog):
	for post in blog.posts:
		print_post(post)


def print_post(post):
	print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
	blog_name = input('Type the blog title you want to write a post in: ')
	title = input('Type your post title: ')
	content = input('Type post content: ')

	blogs[blog_name].create_post(title, content)
