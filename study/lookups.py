from ajax_select import register, LookupChannel
from .models import CourseInstance

@register('courses')
class CoursesLookup(LookupChannel):

    model = CourseInstance
    min_length = 3

    def get_query(self, q, request):
        return CourseInstance.objects.filter(course_query__icontains=q)

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.course_name

# <<<<<<< HEAD
#     def check_auth(self, request):
#         if request.user.get_profile() :
#             return True
# =======
    def check_auth(self, request): ##CHANGED TO RETURN TRUE
        return True
# >>>>>>> import-courses
