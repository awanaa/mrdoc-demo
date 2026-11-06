from django.contrib import admin
from app_doc.models import Space, DocView, DocLike, DocComment

# Register your models here.
admin.site.register(Space)
admin.site.register(DocView)
admin.site.register(DocLike)
admin.site.register(DocComment)

