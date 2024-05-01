from django.contrib import admin

from djangoapp.lab.models.flask import FlaskModel
from djangoapp.lab.models.lifecase import LifeCaseModel
from djangoapp.lab.models.selected_previous_case import SelectedPreviousCaseModel

admin.site.register(LifeCaseModel)
admin.site.register(FlaskModel)
admin.site.register(SelectedPreviousCaseModel)