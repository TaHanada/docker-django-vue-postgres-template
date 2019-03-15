from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.contrib.auth import get_user_model

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView

from .models import Message, MessageSerializer

from backend.users.models import User
from backend.users.serializers import UserSerializer

from backend.bookkeeping.models import Entry
from backend.bookkeeping.serializers import EntrySerializer


# class MessageViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows messages to be viewed or edited.
#     """
#     queryset = Message.objects.all()
#     serializer_class = MessageSerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows entries to be viewed or edited.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     # lookup_field = 'id'
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def list(self, request):
#         """
#         List all users in database.

#         returns:
#           - application/json
#         """
#         return Response({})

#     def retrieve(self, request, id=None):
#         """
#         Returns data on a particular user.

#         returns:
#           - application/json
#         """
#         # queryset = User.objects.all()
#         # user = get_object_or_404(queryset, id=id)
#         # serializer = UserSerializer(user)
#         # return Response(serializer.data)
#         return Response({})

#     # def create(self, request):
#     #     """
#     #     Create a new user.

#     #     returns:
#     #       - application/json
#     #     """
#     #     serializer = self.serializer_class(data=request.data)

#     #     if serializer.is_valid():
#     #         user = User.objects.create_user(**serializer.validated_data)
#     #         new_user = User.objects.get(id=user.id)
#     #         new_user.sex = serializer.validated_data.get('sex', None)
#     #         new_user.age = serializer.validated_data.get('age', None)
#     #         new_user.terms_agreement = serializer.validated_data['terms_agreement']
#     #         new_user.loyalty_agreement = serializer.validated_data['terms_agreement']
#     #         new_user.verified = serializer.validated_data['verified']
#     #         # new_user.user_type = serializer.validated_data.get('user_type', None)
#     #         new_user.status = serializer.validated_data.get('status', User.STATUS_CHOICE[0][0])

#     #         new_user.save()

#     #         user_serialized_data = UserSerializer(new_user).data

#     #         token = generate_token(new_user)

#     #         # if new_user.user_type is not User.USER_TYPE_CHOICE[0][0]:
#     #             # tasks.send_welcome_email_task.delay(user.email,
#     #                                                 # "Thank you for using Strainprint app")
#     #         return Response({"user": user_serialized_data,
#     #                             "token": token},
#     #                         status=status.HTTP_201_CREATED)
#     #     else:
#     #         return Response({
#     #             'status': 'Bad request',
#     #             'errors': serializer.errors
#     #         }, status=status.HTTP_400_BAD_REQUEST)

#     # def update(self, request, id=None):
#     #     """
#     #     Update the information of a user.

#     #     returns:
#     #       - application/json
#     #     """
#     #     user = User.objects.get(id=request.user.id)
#     #     serializer = UserSerializer(user, data=request.data, partial=True)

#     #     if serializer.is_valid():
#     #         new_user = serializer.save()
#     #         token = generate_token(new_user)

#     #         return Response({"user": UserSerializer(new_user).data,
#     #                          "token": token},
#     #                         status=status.HTTP_200_OK)

#     #     return Response({
#     #         'status': 'Bad request',
#     #         'errors': serializer.errors
#     #     }, status=status.HTTP_400_BAD_REQUEST)

# class ChangePasswordView(generics.UpdateAPIView):
#     """
#     Allows the user to change his or her password.
#     """
#     serializer_class = ChangePasswordSerializer
#     model = User

#     def get_object(self, queryset=None):
#         obj = self.request.user
#         return obj

#     def update(self, request, *args, **kwargs):
#         """
#         Allows the user to update his or her password.
#         """
#         self.object = self.get_object()
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid():
#             # Check old password
#             if not self.object.check_password(serializer.data.get("old_password")):
#                 return Response({"old_password": ["Wrong password."]},
#                                 status=status.HTTP_400_BAD_REQUEST)

#             # set_password also hashes the password that the user will get
#             self.object.set_password(serializer.data.get("password"))
#             self.object.save()

#             token = generate_token(self.object)

#             return Response({"user": UserSerializer(self.object).data, "token": token},
#                             status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ForgotPasswordView(views.APIView):
#     renderer_classes = (renderers.JSONRenderer,)

#     def get_permissions(self):
#         if self.request.method in permissions.SAFE_METHODS:
#             return (permissions.AllowAny(),)

#         if self.request.method == 'POST':
#             return (permissions.AllowAny(),)

#         return (permissions.IsAuthenticated(),)

#     def post(self, request, *args, **kw):
#         """
#         Allows the user to reset his or her password by inputing the user's email address.

#         parameters:
#           - email:
#                 - description: user's email address
#                 - required: true
#                 - paramType: form
#                 - type: str
#         returns:
#           - application/json
#         """
#         try:
#             email = request.data['email']
#             validators.validate_email(email)
#             user = User.objects.get(email=email)

#             if user:
#                 activation_code = hashlib.md5(
#                     settings.SECRET_KEY + email).hexdigest()
#                 action_url = "http://" + request.get_host() + "/forgot-password/" + \
#                     activation_code

#                 user.activation_code = activation_code
#                 user.save()

#                 tasks.ac_contact_send_reset_password_email(
#                     user.active_campaign_id, action_url)

#                 return Response({"status": "success"}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"status": "error", "message": "We could not recognize your email"}, status=status.HTTP_400_BAD_REQUEST)
#         except (User.DoesNotExist, ValidationError) as e:
#             return Response({"status": "error", "message": "Your email is not valid"}, status=status.HTTP_400_BAD_REQUEST)
