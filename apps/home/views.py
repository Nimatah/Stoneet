from django.views.generic import TemplateView

from apps.home.models import StaticContent
from apps.products.models import Product


class _BaseStaticContentView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['static_content'] = StaticContent.objects.first()
        return context


class HomeView(TemplateView):

    PRODUCTS_LIMIT = 8

    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter()[:self.PRODUCTS_LIMIT]
        return context


class ContactUsView(TemplateView):

    template_name = 'home/contact_us.html'


class TermsConditionsView(_BaseStaticContentView):

    template_name = 'home/terms.html'


class FAQView(TemplateView):

    template_name = 'home/faq.html'


class SellerTermsConditionsView(_BaseStaticContentView):

    template_name = 'home/terms_seller.html'


class LogisticTermsConditionsView(_BaseStaticContentView):

    template_name = 'home/terms_logistic.html'


class PrivacyPolicyView(_BaseStaticContentView):

    template_name = 'home/privacy_policy.html'
