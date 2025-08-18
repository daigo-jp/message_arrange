# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    pass # AbstractUserを継承するだけなら、フィールドの追加は不要です

    
    # groupsフィールドに、衝突しない一意のrelated_nameを指定します
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="custom_user_set", # 名前を変更
        related_query_name="user",
    )

    # user_permissionsフィールドにも同様に指定します
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions_set", # 名前を変更
        related_query_name="user",
    )