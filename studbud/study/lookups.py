from ajax_select import register, LookupChannel
from .models import CourseInstance

@register('courses')
class CoursesLookup(LookupChannel):

    model = CourseInstance

    def get_query(self, q, request):
        return CourseInstance.objects.filter(course_name__icontains=q)

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.course_name

    def check_auth(self, request):
        if request.user.get_profile() :
            return True
