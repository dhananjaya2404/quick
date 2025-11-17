from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsEmployerOrReadOnly(BasePermission):
    """
    Employers can create/update/delete their jobs.
    Other authenticated users can read.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        # write operations require employer role
        user = request.user
        return bool(
            user and user.is_authenticated and getattr(user, "role", None) == "employer"
        )


class IsJobOwnerEmployer(BasePermission):
    """
    Only the employer who posted the job can modify it.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        if request.method in SAFE_METHODS:
            return user and user.is_authenticated
        return bool(
            user
            and user.is_authenticated
            and getattr(user, "role", None) == "employer"
            and obj.posted_by_id == user.id
        )


