from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

	def test_create_blog(self):
		b = Blog('Test Title', 'Test Author')

		self.assertEqual('Test Title', b.title)
		self.assertEqual('Test Author', b.author)
		self.assertListEqual([], b.posts)

	def test_repr(self):
		b = Blog('Test Title', 'Test Author')
		b2 = Blog('My day', 'Susan')

		self.assertEqual(b.__repr__(), 'Test Title by Test Author (0 posts)')
		self.assertEqual(b2.__repr__(), 'My day by Susan (0 posts)')

	def test_repr_multiple_posts(self):
		b = Blog('Meet and eat', 'Tom')
		b.posts = ['food post']
		b1 = Blog('I have a dog', 'Mary P')
		b1.posts = ['some post', 'dog post']

		self.assertEqual(b.__repr__(), 'Meet and eat by Tom (1 post)')
		self.assertEqual(b1.__repr__(), 'I have a dog by Mary P (2 posts)')
