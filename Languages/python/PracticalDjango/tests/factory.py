from django.contrib.auth import get_user_model

UserModel = get_user_model()


def create_user(username: str, email: str, password: str) -> UserModel:
    return UserModel.object.create(
        username=username,
        email=email,
        password=password,
    )
