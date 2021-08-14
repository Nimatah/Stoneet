from django.views.generic import TemplateView


class BuyerSampleListView(TemplateView):
    template_name = 'users/buyer/orders/buyer_sample_list.html'
