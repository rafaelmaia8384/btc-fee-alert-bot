from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


from api.models import Alert


class UserCountView(View):
    def get(self, request, *args, **kwargs):
        unique_users = Alert.objects.values("user_id").distinct().count()
        return HttpResponse(f"{unique_users}", status=200)


@method_decorator(csrf_exempt, name="dispatch")
class ManageFeesView(View):
    def post(self, request, *args, **kwargs):
        print(request.body)
        return HttpResponse(status=200)
