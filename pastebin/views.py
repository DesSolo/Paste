from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse
from django.views.generic import View, CreateView, DetailView
from django.utils import timezone
from .models import CodePaste


class CreateCodePasteView(CreateView):
    template_name = 'pastebin/create.html'
    model = CodePaste
    fields = ['title', 'author', 'body', 'language', 'expired']


class PasteDetails(DetailView):
    template_name = 'pastebin/detail.html'
    model = CodePaste
    queryset = CodePaste.objects.filter(expired_at__gte=timezone.now())


class Raw(View):
    @staticmethod
    def get(request, pk):
        paste = get_object_or_404(CodePaste, pk=pk, expired_at__gte=timezone.now())
        return HttpResponse(paste.body, content_type='text/plain; charset=utf-8')


class Download(View):
    @staticmethod
    def get(request, pk):
        paste = get_object_or_404(CodePaste, pk=pk, expired_at__gte=timezone.now())
        response = HttpResponse(paste.body, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename={pk}'
        return response


def handler404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


def handler500(request, exception, template_name="500.html"):
    response = render_to_response(template_name)
    response.status_code = 500
    return response
