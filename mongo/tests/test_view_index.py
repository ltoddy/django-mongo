from django.test import TestCase
from django.urls import reverse, resolve
from ..views import index


class IndexTests(TestCase):
    def test_index_status_code(self):
        url = reverse('mongo:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_index_url_resolves_inde_view(self):
        view = resolve('/mongo/')
        self.assertEquals(view.func, index)
