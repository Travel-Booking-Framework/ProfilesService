from django.urls import path
from Profile.api.views import UserProfileView, UserBankInfoView


urlpatterns = [
    path('user-profiles/', UserProfileView.as_view()),
    path('user-profiles/<int:pk>/', UserProfileView.as_view()),
    path('user-bank-info/', UserBankInfoView.as_view()),
    path('user-bank-info/<int:pk>/', UserBankInfoView.as_view()),
]