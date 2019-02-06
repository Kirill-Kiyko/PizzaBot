from django.test import TestCase


class PizzaViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.post('/telegram-bot', content_type='application/json', data={'message': {'from': {'username': 'kiyochek', 'last_name': 'Kiyko', 'id': 566740057, 'first_name': 'Kirill', 'language_code': 'ru', 'is_bot': False}, 'chat': {'username': 'kiyochek', 'last_name': 'Kiyko', 'id': 566740057, 'first_name': 'Kirill', 'type': 'private'}, 'date': 1549452303, 'message_id': 313, 'entities': [{'offset': 0, 'length': 6, 'type': 'bot_command'}], 'text': '/start'}, 'update_id': 106629564})
        self.assertEqual(resp.status_code, 200)