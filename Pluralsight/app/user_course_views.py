import uuid

class UserCourseViews:
#user_handle,view_date,course_id,author_handle,level,
#view_time_seconds

    __user_handle = None
    __view_date=None
    __course_id = None
    __author_handle = None
    __level = None
    __view_time_seconds = None

    def __init__(self,user_handle,view_date,course_id,author_handle,level,view_time_seconds):
        self.user_handle = user_handle
        self.view_date = view_date
        self.course_id = course_id
        self.author_handle = author_handle
        self.level = level
        self.view_time_seconds = view_time_seconds



    @def user_handle():
        doc = "The user_handle property."
        def fget(self):
            return self._user_handle
        def fset(self, value):
            self._user_handle = value
        def fdel(self):

            del self._user_handle

        return locals()
    user_handle = property(**user_handle())

    @def view_date():
        doc = "The view_date property."
        def fget(self):
            return self._view_date
        def fset(self, value):
            self._view_date = value
        def fdel(self):
            del self._view_date
        return locals()
    view_date = property(**view_date())
    @def course_id():
        doc = "The course_id property."
        def fget(self):
            return self._course_id
        def fset(self, value):
            self._course_id = value
        def fdel(self):
            del self._course_id
        return locals()
    course_id = property(**course_id())
    @def author_handle():
        doc = "The author_handle property."
        def fget(self):
            return self._author_handle
        def fset(self, value):
            self._author_handle = value
        def fdel(self):
            del self._author_handle
        return locals()
    author_handle = property(**author_handle())
    @def level():
        doc = "The level property."
        def fget(self):
            return self._level
        def fset(self, value):
            self._level = value
        def fdel(self):
            del self._level
        return locals()
    level = property(**level()

    @def view_time_seconds():
        doc = "The view_time_seconds property."
        def fget(self):
            return self._view_time_seconds
        def fset(self, value):
            self._view_time_seconds = value
        def fdel(self):
            del self._view_time_seconds
        return locals()
    view_time_seconds = property(**view_time_seconds())

    def serialize(self):
        return{
        'user_handle':self.user_handle
        'view_date':self.view_date
        'course_id':self.course_id
        'author_handle':self.author_handle
        'level':self.level
        'view_time_seconds':self.view_time_seconds
        }
