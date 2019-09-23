from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        new_group, created = Group.objects.get_or_create(name='Authors')

        # Code to add permission to group
        ct = ContentType.objects.get_for_model(User)

        # If I want to add 'Can go Haridwar' permission to level0 ?
        permission = Permission.objects.create(codename='can_create_posts',
                                               name='Can create new post',
                                               content_type=ct)
        new_group.permissions.add(permission)
