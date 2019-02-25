from unittest import TestCase
from unittest.mock import patch  # for testing sth which is printed
import app
from blog import Blog
from post import Post


class AppTest(TestCase):

	def setUp(self):
		blog = Blog('Test blog title', 'Test blog author')
		app.blogs = {'Test': blog}

	def test_menu_calls_create_blog(self):
		with patch('builtins.input') as mocked_input:
			mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')

			app.menu()
			self.assertIsNotNone(app.blogs['Test Create Blog'])

	def test_menu_prints_prompt(self):
		""" Check if MENU_PROMPT opens when menu called (?) """
		with patch('builtins.input', return_value='q') as mocked_input:
			app.menu()
			mocked_input.assert_called_with(app.MENU_PROMPT)

	def test_menu_calls_print_blogs(self):
		with patch('app.print_blogs') as mocked_print_blogs:
			with patch('builtins.input', return_value='q'):  # zatykamy odpowiedzia q - quit
				app.menu()
				mocked_print_blogs.assert_called()

	def test_print_blogs(self):
		with patch('builtins.print') as mocked_print:
			app.print_blogs()  # this is what method returns
			mocked_print.assert_called_with('- Test blog title by Test blog author (0 posts)')  # this is what should be

	def test_ask_create_blog(self):
		with patch('builtins.input') as mocked_input:
			mocked_input.side_effect = ('Test title', 'Test author')  # side_effect is because there are more than one input I suppose
			app.ask_create_blog()

			self.assertIsNotNone(app.blogs.get('Test title'))

	# def test_ask_read_blog(self):  # we test if this function has another function
	# 	blog = app.blogs['Test blog']
	# 	with patch('builtins.input', return_value='Test blog'):
	# 		with patch('app.print_posts') as mocked_print_posts:
	# 			app.ask_create_blog()
	# 			mocked_print_posts.assert_called_with(blog)

	def test_print_posts(self):
		blog = app.blogs['Test']
		blog.create_post('Test post', 'Test content')

		with patch('app.print_post') as mocked_print_post:
			app.print_posts(blog)
			mocked_print_post.assert_called_with(blog.posts[0])

	def test_print_post(self):
		post = Post('Post title', 'Post content')
		expected_print = '''{} {}'''.format(post.title, post.content)
		with patch('builtins.print') as mocked_print:
			app.print_post(post)

			mocked_print.assert_called_with(expected_print)

	def test_ask_create_post(self):
		blog = app.blogs['Test']

		with patch('builtins.input') as mocked_input:
			mocked_input.side_effect = {'Test', 'Sample blog name', 'Sample blog content'}

			app.ask_create_post()

			self.assertEqual(blog.posts[0].title, 'Sample blog name')
			self.assertEqual(blog.posts[0].content, 'Sample blog content')
