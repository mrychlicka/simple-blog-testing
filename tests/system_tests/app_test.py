from unittest import TestCase
from unittest.mock import patch  # for testing sth which is printed
import app
from blog import Blog


class AppTest(TestCase):

	def test_print_blogs(self):
		blog = Blog('Test blog title', 'Test blog author')
		app.blogs = {'Test blog': blog}
		with patch('builtins.print') as mocked_print:
			app.print_blogs()
			mocked_print.assert_called_with('- Test blog title by Test blog author (0 posts)')