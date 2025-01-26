from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from registrations.models import Role, CustomUser


class Command(BaseCommand):
    help = 'Seeds roles and creates a superuser with manual inputs'

    def handle(self, *args, **kwargs):
        # Create roles if they don't exist
        roles = ['Admin']
        for role_name in roles:
            role, created = Role.objects.get_or_create(name=role_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Role "{role_name}" created successfully.'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Role "{role_name}" already exists.'))

        # Manual input for the superuser creation
        username = self.prompt_for_input('Enter username for superuser: ')
        email = self.prompt_for_input('Enter email for superuser: ')
        password = self.prompt_for_input('Enter password for superuser: ')

        # Create superuser if not already exists
        if not CustomUser.objects.filter(username=username).exists():
            superuser = CustomUser.objects.create(
                username=username,
                email=email,
                is_staff=True,
                is_superuser=True,
                role=None  # No role is assigned to the superuser
            )
            superuser.set_password(password)  # Set password entered by user
            superuser.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser created successfully with username: {username}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superuser with username "{username}" already exists.'))

        # Now handle normal user creation (if needed)
        create_normal_user = self.prompt_for_input('Do you want to create a normal user? (y/n): ').lower()
        if create_normal_user == 'y':
            username = self.prompt_for_input('Enter username for normal user: ')
            email = self.prompt_for_input('Enter email for normal user: ')
            password = self.prompt_for_input('Enter password for normal user: ')

            # Choose role for normal user
            role_name = self.prompt_for_input(f'Select a role from {roles}: ')
            if role_name not in roles:
                self.stdout.write(self.style.ERROR(f'Invalid role selected.'))
                return

            role = Role.objects.get(name=role_name)

            if not CustomUser.objects.filter(username=username).exists():
                normal_user = CustomUser.objects.create(
                    username=username,
                    email=email,
                    role=role  # Assign the selected role to the user
                )
                normal_user.set_password(password)  # Set password entered by user
                normal_user.save()
                self.stdout.write(self.style.SUCCESS(f'Normal user created successfully with username: {username}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'User with username "{username}" already exists.'))

    def prompt_for_input(self, prompt):
        """
        Prompt for user input in the command line.
        """
        return input(self.style.SUCCESS(prompt))