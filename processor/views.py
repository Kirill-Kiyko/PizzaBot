import requests

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from transitions import Machine

from .models import Pizza


states = [
    {'name':'start'},
    {'name':'size'},
    {'name':'payment_type'},
    {'name':'confirmation'}
]

machine = Machine(states=states, initial='start')
machine.add_ordered_transitions()


TELEGRAM_URL = 'https://api.telegram.org/bot{TOKEN}/'


class Phrases:
    def get_size(self):
        return "Какую вы хотите пиццу?  Большую или маленькую?"

    def get_payment(self):
        return 'Как вы будете платить?'

    def get_confirm(self, size, payment_type):
        return 'Вы хотите {} пиццу, оплата - {}?'.format(size.lower(), payment_type.lower())

    def get_confirmed(self, answer):
        if answer == 'да':
            text = 'Спасибо за заказ. Если хотите сделать еще 1 заказ, используйте команду /start'
        else:
            text = "Извините, попробуйте еще раз. Используйте команду /start"

        return text

    def get_fallback(self):
        return "Извините, попробуйте еще раз. Используйте команду /start"


class TelegramBot(APIView, Phrases):
    def post(self,request):
        print(request.data)
        message = request.data['message']['text']
        chat_id = request.data['message']['chat']['id']

        if machine.state == 'start':
            Pizza.objects.get_or_create(
                user_id=chat_id
            )

            text = self.get_size()
        elif machine.state == 'size':
            pizza = Pizza.objects.get(user_id=chat_id)
            pizza.size=message
            pizza.save()

            text = self.get_payment()
        elif machine.state == 'payment_type':
            pizza = Pizza.objects.get(user_id=chat_id)
            pizza.payment_type=message
            pizza.save()

            saved_data = Pizza.objects.get(user_id=chat_id)

            text = self.get_confirm(saved_data.size, saved_data.payment_type)
        elif machine.state == 'confirmation':
            text = self.get_confirmed(message)
        else:
            text = self.get_fallback()

        prepared_data = {
            'chat_id': chat_id,
            'text': text
        }

        message_url = BOT_URL + 'sendMessage'
        requests.post(message_url, json=prepared_data)

        machine.next_state()
        return Response(status=status.HTTP_200_OK)