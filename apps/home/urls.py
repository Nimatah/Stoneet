from django.urls import path

from apps.home.views import HomeView, ContactUsView, TermsConditionsView, FAQView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('terms/', TermsConditionsView.as_view(), name='terms'),
    path('faq/', FAQView.as_view(), name='faq'),
]
