from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.sitemaps import Sitemap
from .models import TestItem
# Create your views here.


class TestItemList(ListView):
    model = TestItem
    template_name = 'testitem_list.html'
    context_object_name = 'objects'

    def get_context_data(self, **kwargs):
        context = super(TestItemList, self).get_context_data(**kwargs)
        con = self.context_object_name
        url = self.request.get_host()
        context[con] = context[con].filter(site__domain=url.split(':')[0])
        return context


class TestItemDetail(DetailView):
    model = TestItem
    context_object_name = 'item'
    template_name = 'testitem_detail.html'


class TestItemSitemap(Sitemap):
    name = 'items'
    changefreq = 'daily'
    limit = 5000

    def items(self):
        return TestItem.objects.all()


class TestItemSitemapSOF(Sitemap):
    _cached_site = None

    def items(self):
        return TestItem.objects.filter(site=self._cached_site)

    def get_urls(self, page=1, site=None, protocol=None):
        self._cached_site = site
        return super(TestItemSitemapSOF, self).get_urls(page=page, site=site, protocol=protocol)

