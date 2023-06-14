from rest_framework.permissions import IsAdminUser


class isAdminOrReadOnly(IsAdminUser):
    pass