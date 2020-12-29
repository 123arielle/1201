from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from mainsite.models import Post, AccessInfo, Branch, StoreIncome, Kindergarten, SchoolStu, Photo, Visitor, Visitors, HelloVisit, Asiacountry

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)
admin.site.register(AccessInfo)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('shop_name', 'boss_name')
admin.site.register(Branch, BranchAdmin)

class StoreIncomeAdmin(admin.ModelAdmin):
    list_display = ('branch','income_year', 'income_month', 'income')
admin.site.register(StoreIncome, StoreIncomeAdmin)

class KindergartenAdmin(admin.ModelAdmin):
    list_display = ('president','branch_school')
admin.site.register(Kindergarten, KindergartenAdmin)

class SchoolStuAdmin(admin.ModelAdmin):
    list_display = ('kindergarten','recruit_year','recruit_num')
admin.site.register(SchoolStu, SchoolStuAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'upload_date')
admin.site.register(Photo, PhotoAdmin)

class VisitorAdmin(admin.ModelAdmin):
    list_display = ('states','country','year','visitor_num')
admin.site.register(Visitor, VisitorAdmin)

class VisitorsAdmin(ImportExportModelAdmin):
    list_display = ('states','country','year','visitors_num')
admin.site.register(Visitors, VisitorsAdmin)

class HelloVisitAdmin(ImportExportModelAdmin):
    list_display = ('states','country','year','visitors_num')
admin.site.register(HelloVisit, HelloVisitAdmin)

class AsiacountryAdmin(admin.ModelAdmin):
    list_display = ('asia_country','leader')
admin.site.register(Asiacountry, AsiacountryAdmin)