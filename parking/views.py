from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import GarageSerializer, UserSerializer
from .models import *
from .serializers import *
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FamilyCommunityViewSet(viewsets.ModelViewSet):
    queryset = FamilyCommunity.objects.all()
    serializer_class = FamilyCommunitySerializer

class FamilyMemberViewSet(viewsets.ModelViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

    # 🔍 Search for parking around my area
    @action(detail=False, methods=['get'], url_path='search-nearby')
    def search_nearby(self, request):
        try:
            lat = float(request.query_params.get('lat'))
            lng = float(request.query_params.get('lng'))
        except (TypeError, ValueError):
            return Response({'error': 'Invalid coordinates'}, status=400)

        nearby = Garage.objects.filter(
            latitude__range=(lat - 0.05, lat + 0.05),
            longitude__range=(lng - 0.05, lng + 0.05)
        )
        serializer = self.get_serializer(nearby, many=True)
        return Response(serializer.data)

    # ⭐ Favorite garage
    @action(detail=True, methods=['post'], url_path='favorite')
    def favorite(self, request, pk=None):
        garage = self.get_object()
        user = request.user
        user.favorite_garages.add(garage)  # Ensure you have ManyToManyField
        return Response({'status': 'Garage added to favorites'})


class ParkingZoneViewSet(viewsets.ModelViewSet):
    queryset = ParkingZone.objects.all()
    serializer_class = ParkingZoneSerializer


class ParkingSlotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSlot.objects.all()
    serializer_class = ParkingSlotSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ParkingEventViewSet(viewsets.ModelViewSet):
    queryset = ParkingEvent.objects.all()
    serializer_class = ParkingEventSerializer


class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class ParkingHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParkingHistory.objects.all()
    serializer_class = ParkingHistorySerializer


class ParkingAlertViewSet(viewsets.ModelViewSet):
    queryset = ParkingAlert.objects.all()
    serializer_class = ParkingAlertSerializer


class ParkingSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = ParkingSubscription.objects.all()
    serializer_class = ParkingSubscriptionSerializer


class ParkingSlotReservationHistoryViewSet(viewsets.ModelViewSet):
    queryset = ParkingSlotReservationHistory.objects.all()
    serializer_class = ParkingSlotReservationHistorySerializer


class ParkingSensorViewSet(viewsets.ModelViewSet):
    queryset = ParkingSensor.objects.all()
    serializer_class = ParkingSensorSerializer


class UserFeedbackViewSet(viewsets.ModelViewSet):
    queryset = UserFeedback.objects.all()
    serializer_class = UserFeedbackSerializer


class DiscountCouponViewSet(viewsets.ModelViewSet):
    queryset = DiscountCoupon.objects.all()
    serializer_class = DiscountCouponSerializer


class ParkingNotificationViewSet(viewsets.ModelViewSet):
    queryset = ParkingNotification.objects.all()
    serializer_class = ParkingNotificationSerializer



class ResetPasswordSerializer(serializers.Serializer):
    reset_password_token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = User.objects.filter(reset_password_token=data['reset_password_token']).first()
        if user is None:
            raise serializers.ValidationError("Invalid token.")
        
        return data

    def save(self):
        user = User.objects.filter(reset_password_token=self.validated_data['reset_password_token']).first()
        user.set_password(self.validated_data['new_password'])
        user.reset_password_token = ''  # Clear the token
        user.save()
        return user

# 5. Registration View

class UserRegistrationViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 6. Login View
class LoginViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 7. Forgot Password View
class ForgotPasswordViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Password reset email sent!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 8. Reset Password View
class ResetPasswordViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password reset successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


from math import radians, sin, cos, sqrt, atan2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Garage

class CardViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='add')
    def add_card(self, request):
        card_number = request.data.get('card_number')
        exp_date = request.data.get('exp_date')

        # Save card logic here...
        # For demo:
        return Response({'message': 'Card added successfully'})


# 👤 User Search ViewSet
class UserSearchViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='by-email')
    def search_by_email(self, request):
        email = request.query_params.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            data = UserSerializer(user).data
            return Response(data)
        return Response({'error': 'User not found'}, status=404)
