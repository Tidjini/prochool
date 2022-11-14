# if new student save  (pk is None):  -> if not self.pk: <-
#    1/ check existence by phone / first_name / last_name, these three
#       in managers set Student.exist(**kwargs) some reflexion
#    2/ if not exist : generate barre code and save it as exist now

from .models.student import Student


def student_exist(**kwrags):
    keys = ('first_name', 'last_name', 'phone')
    fields = {k: v for k, v in kwrags if k in keys}
    return Student.objects.get(**fields)
