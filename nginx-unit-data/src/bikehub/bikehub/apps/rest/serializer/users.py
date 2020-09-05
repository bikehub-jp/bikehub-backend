from news.models import News, MainCategoryTag, SubCategoryTag, SubCategoryTagMap, TargetSite
from rest_framework import serializers
# from drf_queryfields import QueryFieldsMixin
from users.models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'disp_name',
            'email',
            'birthday',
            # 'ubike1_by_list',
            # 'ubike2_by_list',
            'accept',
            'password',
            'password2',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def save(self):
        user = CustomUser(
            email=self.validated_data['email'],
            disp_name=self.validated_data['disp_name'],
            birthday=self.validated_data['birthday'],
            # ubike1_by_list=self.validated_data['ubike1_by_list'],
            # ubike2_by_list=self.validated_data['ubike2_by_list'],
            accept=self.validated_data['accept'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user