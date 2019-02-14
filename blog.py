from post import Post


class Blog:

	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.posts = []

	def __repr__(self):
		"""Return string repr of aou blog, ex. for debuggin"""
		return '%s by %s (%i post%s)' % (self.title, self.author, len(self.posts), 's' if len(self.posts) > 1 else '')

	def create_post(self, title, content):
		created_post = Post(title, content)
		return self.posts.append(created_post)

	def json(self):
		return {
			'title': self.title,
			'author': self.author,
			'posts': [post.json() for post in self.posts],
		}
