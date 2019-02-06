from django.test import TestCase

from ..models import Pizza


class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Pizza.objects.create(user_id=123456789, size='Большая', payment_type='Gpay')

    def test_user_id_label(self):
        pizza = Pizza.objects.get(user_id=123456789)

        field_label = pizza._meta.get_field('user_id').verbose_name

        self.assertEquals(field_label, 'user id')

    def test_size_max_length(self):
        pizza = Pizza.objects.get(user_id=123456789)
        max_length = pizza._meta.get_field('size').max_length
        self.assertEquals(max_length, 200)

    def test_object_pizza_is_size_comma_payment_type(self):
        pizza = Pizza.objects.get(user_id=123456789)
        expected_object_name = '%s %s' % (pizza.size, pizza.payment_type)
        self.assertEquals(expected_object_name, str(pizza))