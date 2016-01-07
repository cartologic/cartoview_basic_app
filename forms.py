from cartoview.app_manager.forms import AppInstanceForm
from models import BasicApp


# configuration form to add/edit new instance.
class BasicAppForm(AppInstanceForm):
    class Meta(AppInstanceForm.Meta):
        model = BasicApp
        # append new fields to typical app instance form fields.
        fields = AppInstanceForm.Meta.fields  # + ['field1', 'field2']
