from django.views.generic import TemplateView


class SellerSampleListView(TemplateView):
    template_name = 'users/seller/orders/seller_sample_list.html'
