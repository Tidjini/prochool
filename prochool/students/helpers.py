# if new student save  (pk is None):  -> if not self.pk: <-
#    1/ check existence by phone / first_name / last_name, these three
#       in managers set Student.exist(**kwargs) some reflexion
#    2/ if not exist : generate barre code and save it as exist now



def student_exist(model, **kwrags):
    keys = ('first_name', 'last_name', 'phone')
    fields = {k: v for k, v in kwrags if k in keys}
    return Student.objects.get(**fields)




# todos: 
#       - is student paied or not 
#            my_memberships.filter(teacher).remain_sessions > 0 and free_membership = False
#       - is student present last course 
#            get last presence, check if student is absent or not
#       - get student place or None -> my_places[id]
#       - get student group -> my_places[id].group
#       For details    
#       - get list of presences -> my_presences
#       - get list of payments -> payments
#       - get list of places -> my_places







# # student manager
# def student_places(barre_code):
#     student = Student.objects.get(barre_code=barre_code, None)
#     if not student:
#         return
#     return student.my_places.all()

# # student manager ?
# def student_groups(barre_code, group):
#     student = Student.objects.get(barre_code=barre_code, None)
#     if not student:
#         return
#     #review this
#     place = student.my_places.group()
#     return place

