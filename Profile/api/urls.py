from django.urls import path
from Profile.api.views import UserProfileView, UserBankInfoView, ProfileLists, ProfileDetails, BankInfoLists, BankInfoDetails


urlpatterns = [
    # UserProfile CRUD
    path('user-profiles/', UserProfileView.as_view(), name='create_or_update_user_profile'),
    path('user-profiles/<int:pk>/', UserProfileView.as_view(), name='update_or_delete_user_profile'),

    # UserProfile queries
    path('user-profiles/all/', ProfileLists.as_view(), name='list_user_profiles'),
    path('user-profiles/<str:national_code>/', ProfileDetails.as_view(), name='detail_user_profile'),

    # UserBankInfo CRUD
    path('user-bank-info/', UserBankInfoView.as_view(), name='create_or_update_bank_info'),
    path('user-bank-info/<int:pk>/', UserBankInfoView.as_view(), name='update_or_delete_bank_info'),

    # UserBankInfo queries
    path('bank-info/all/', BankInfoLists.as_view(), name='list_user_bank_infos'),
    path('user-bank-info/<str:card_number>/', BankInfoDetails.as_view(), name='detail_user_bank_info'),
]