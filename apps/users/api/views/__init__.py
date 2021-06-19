from .seller import SellerAddProductPart1ValidationAPIView
from .registration import RegistrationAuthValidationView
from .mine import MineListCreateAPIView, MineRetrieveUpdateDestroyView
from .address import AddressListCreateAPIView, AddressRetrieveUpdateDestroyView
from .users import (
    UserListAPIView,
    register_buyer_validation,
    register_logistic_validation,
    register_seller_validation,
    user_accept,
    user_reject,
)
