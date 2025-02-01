from Profile.models import UserBankInfo


class UserBankInfoService:
    @staticmethod
    def create_user_bank_info(data):
        return UserBankInfo.objects.create(**data)

    @staticmethod
    def update_user_bank_info(user_bank_info, data):
        for field, value in data.items():
            setattr(user_bank_info, field, value)
        user_bank_info.save()
        return user_bank_info

    @staticmethod
    def delete_user_bank_info(user_bank_info):
        user_bank_info.delete()

    @staticmethod
    def get_all_bank_infos():
        return UserBankInfo.objects.all()