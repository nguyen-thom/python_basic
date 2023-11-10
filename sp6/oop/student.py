class Student:
    def __init__(self, id, name, birthday="2012-2-21", phone_number="23322-0909-9988"):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.phone_number = phone_number

    def show(self):
        print("Student: {} Name: {} Birthday: {} Phone: {}"
              .format(self.id, self.name, self.birthday, self.phone_number))

    def __str__(self):
        student_format = ("Student: {} Name: {} Birthday: {} Phone: {}"
                          .format(self.id, self.name, self.birthday, self.phone_number))
        return student_format
