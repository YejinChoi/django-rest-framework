from rest_framework import permissions

class IsAuthorUpdateOrReadonly(permissions.BasePermission):
    #인증된 유저에 한해, 목록조회/포스팅등록을 허용
    def has_permission(self,request,view):
        return request.user.is_authenticated


    #superuser에게는 삭제권한만, 작성자에게는 수정권한만
    def has_object_permission(self, request, view, obj):
        #조회(GET,HEAD,OPTIONS)에 대해서는 인증여부에 상관없이 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        #삭제는 superuser에게만 허용
        if (request.method == 'DELETE'):
            return request.user.is_superuser

        #PUT은 작성자만 가능
        return obj.author == request.user