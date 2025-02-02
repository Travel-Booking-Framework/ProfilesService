from Profile.models import UserProfile


class UserProfileService:
    @staticmethod
    def create_user_profile(data):
        return UserProfile.objects.create(**data)

    @staticmethod
    def update_user_profile(user_profile, data):
        for field, value in data.items():
            setattr(user_profile, field, value)
        user_profile.save()
        return user_profile

    @staticmethod
    def delete_user_profile(user_profile):
        user_profile.delete()

    @staticmethod
    def get_all_profiles():
        return UserProfile.objects.all()

    @staticmethod
    def get_profile_by_national_code(national_code):
        try:
            return UserProfile.objects.get(national_code=national_code)
        except UserProfile.DoesNotExist:
            return None