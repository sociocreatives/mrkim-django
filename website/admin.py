from django.contrib import admin
from .models import Legal
from .models import Faqs
from .models import ExpertTips

# Register your models here.
admin.site.register(Legal)
admin.site.register(Faqs)
admin.site.register(ExpertTips)