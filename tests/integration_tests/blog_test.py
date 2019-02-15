from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

	def test_json_no_posts(self):
		b = Blog('Test blog title', 'Test blog author')
		expected = {'title': 'Test blog title', 'author': 'Test blog author', 'posts': []}

		self.assertDictEqual(expected, b.json())
		# b.create_post()

	def test_create_post(self):  # this test is not unittest - because test more than one stuff
		b = Blog('Test title', 'Test author')
		b.create_post('My first week in new job', 'some content')

		self.assertEqual(len(b.posts), 1)
		self.assertEqual(b.posts[0].title, 'My first week in new job')
		self.assertEqual(b.posts[0].content, 'some content')

	def test_json(self):
		b = Blog('Test title', 'Test author')
		b.create_post('My first week in new job', 'some content')
		expected = {
			'title': 'Test title',
			'author': 'Test author',
			'posts': [{'title': 'My first week in new job', 'content': 'some content'}]
		}

		self.assertDictEqual(expected, b.json())
