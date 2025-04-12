# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import *

# router = DefaultRouter()
# router.register(r'auth', AuthViewSet, basename='auth')  # Register AuthViewSet
# router.register(r'register', RegisterViewSet, basename='register')  # Register RegisterViewSet
# router.register(r'users', UserViewSet)  # Register UserViewSet
# router.register(r'FamilyMember', FamilyMemberViewSet)
# router.register(r'FamilyCommunity', FamilyCommunityViewSet)
# router.register(r'garages', GarageViewSet)
# router.register(r'parking-zones', ParkingZoneViewSet)
# router.register(r'parking-slots', ParkingSlotViewSet)
# router.register(r'vehicles', VehicleViewSet)
# router.register(r'reservations', ReservationViewSet)
# router.register(r'payments', PaymentViewSet)
# router.register(r'parking-events', ParkingEventViewSet)
# router.register(r'pricing', PricingViewSet)
# router.register(r'parking-history', ParkingHistoryViewSet)
# router.register(r'parking-alerts', ParkingAlertViewSet)
# router.register(r'parking-subscriptions', ParkingSubscriptionViewSet)
# router.register(r'parking-slot-reservation-history', ParkingSlotReservationHistoryViewSet)
# router.register(r'parking-sensors', ParkingSensorViewSet)
# router.register(r'user-feedbacks', UserFeedbackViewSet)
# router.register(r'discount-coupons', DiscountCouponViewSet)
# router.register(r'parking-notifications', ParkingNotificationViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'register', UserRegistrationViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'forgot-password', ForgotPasswordViewSet, basename='forgot-password')
router.register(r'reset-password', ResetPasswordViewSet, basename='reset-password')
router.register(r'users', UserViewSet)  
router.register(r'FamilyMember', FamilyMemberViewSet)
router.register(r'FamilyCommunity', FamilyCommunityViewSet)
router.register(r'garages', GarageViewSet)
router.register(r'parking-zones', ParkingZoneViewSet)
router.register(r'parking-slots', ParkingSlotViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'cards', CardViewSet, basename='cards')
router.register(r'search-user', UserSearchViewSet, basename='search-user')
router.register(r'parking-events', ParkingEventViewSet)
router.register(r'pricing', PricingViewSet)
router.register(r'parking-history', ParkingHistoryViewSet)
router.register(r'parking-alerts', ParkingAlertViewSet)
router.register(r'parking-subscriptions', ParkingSubscriptionViewSet)
router.register(r'parking-slot-reservation-history', ParkingSlotReservationHistoryViewSet)
router.register(r'parking-sensors', ParkingSensorViewSet)
router.register(r'user-feedbacks', UserFeedbackViewSet)
router.register(r'discount-coupons', DiscountCouponViewSet)
router.register(r'parking-notifications', ParkingNotificationViewSet)

urlpatterns = [
    # path('register/', UserRegistrationView.as_view(), name='register'),
    path('', include(router.urls)),
]
