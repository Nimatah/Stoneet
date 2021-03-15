from rest_framework.generics import ListAPIView


from ..serializers.users import UserSerializer
from ...models import User


class UserListAPIView(ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        query = {'use_type': User.TYPE_SELLER}
        seller_id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        mobile_number = self.request.query_params.get('mobile_number', None)
        if seller_id is not None:
            query.update({'id': seller_id})
        if mobile_number is not None:
            query.update({'mobile_number': mobile_number})
        if name is not None:
            query.update({'profile__full_name__icontains': name})
        return User.objects.filter(**query)
