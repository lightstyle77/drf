import environ

from users.models import User

env = environ.Env(
    DEBUG=(bool, False),
    DEFAULT_SU_LOGIN=(str, 'admin'),
    DEFAULT_SU_PASS=(str, 'admin'),
    DEFAULT_SU_EMAIL=(str, 'admin@admin.admin')
)

base = environ.Path(__file__) - 4
environ.Env.read_env(env_file=base('.env'))


def create_superuser(
        username=env('DEFAULT_SU_LOGIN'),
        password=env('DEFAULT_SU_PASS'),
        email=env('DEFAULT_SU_EMAIL'),
        first_name="Admin",
        last_name="Django"):
    user = User.objects.create_superuser(username=username,
                                         email=email,
                                         first_name=first_name,
                                         last_name=last_name,
                                         password=password)
    return user
