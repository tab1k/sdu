from django.shortcuts import render
from django.views import View



class PortalIndexView(View):
    template_name = 'portal/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class GradesView(View):
    template_name = 'portal/grades_list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

