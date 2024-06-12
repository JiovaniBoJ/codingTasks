# This program creates a CRUD matrix for a student task manager.


class Address:

    # The init method is used to initialise the address details.
    def __init__(self, country, city, street, postcode):
        self.country = country
        self. city = city
        self. street = street
        self. postcode = postcode


class Course:

    # The init method is used to initialize the Course details.
    def __init__(self, name, code, num_courses, professor):
        self.name = name
        self.code = code
        self.num_courses = num_courses
        self.professor = professor
        self.enrollments = []

    # This method adds an instance of an enrollment.
    def add_enrollments(self, enrollment):
        if not isinstance(enrollment, Enrollment):
            raise Exception("INVALID-ENROLLMENT")
        self.enrollments.append(enrollment)


class Enrollment:

    # This init method is used to initialise the Enrollment details.
    def __init__(self, student, course):
        if not isinstance(student, Student):
            raise Exception("INVALID-STUDENT")
        if not isinstance(course, Course):
            raise Exception("INVALID-COURSE")
        self.student = student
        self. course = course
        self. grade = None

    def set_grade(self, grade):
        self.grade = grade


class Person:

    # This init method is used to initialise the Person class details.
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Professor(Person):

    # This init method is used to initialise the Professor class details.
    def __init__(self, first_name, last_name, address, salary):
        super(). __init__(self, first_name, last_name, address)
        self.salary = salary
        self.courses = []

    # This method is an instance of the add course function.
    def add_course(self, course):
        if not isinstance(course, Course):
            raise Exception("INVALID-COURSE")
        self.courses.append(course)


class Mentor(Person):

    # This init method is used to initialise the Mentor class.
    def __init__(self, first_name, last_name, address):
        super(). __init__(self, first_name, last_name, address)
        self.courses = []

    # The add course function is used to add a course in this class.
    def add_course(self, course):
        if not isinstance(course, Course):
            raise Exception("INVALID-COURSE")
        self.courses.append(course)


class Student:
    """ This is the student class that represents
    the attributes: subject_id, subject_title, description"""

    # Initialize a new subject instance
    def __init__(self, subject_id, subject_title, progression):

        self.subject_id = subject_id
        self.subject_title = subject_title
        self.progression = progression

    def __repr__(self) -> str:
        return (f"""Subject ID: {self.subject_id},
Subject Title: {self.subject_title},
Progression: {self.progression}""")


print()
print("""------------------------------------------\n""")


subject_data = [Student("UML2024", "Unified Modeling Language", "improved"),
                Student("ML2024", "Machine Learning", "improved")]

# Display information for the subjects.


def display_subject():
    print("These are the Subjects:")
    print()
    print("""------------------------------------------\n""")
    for subs in subject_data:
        print(subs)
    print()
    print("""------------------------------------------\n""")


# This creates a new subject and adds it to the list subject_data.
def create_subject():

    new_id = input("Please enter the subject ID")
    new_title = input("Please enter new Title")
    new_progression = input("Please enter good, satisfactory or improved")
    new_subject = Student(new_id, new_title, new_progression)
    subject_data.append(new_subject)

    print(f"Subject {new_title}, was  added to the list.")


def __repr__(self) -> str:
    print(f"""Subject ID: {self.new_id},
Subject Title: {self.new_title},
Progression: {self.new_progression}""")


print(subject_data)


# This reads and displays the information for the subjects.
def read_subject(subject_id):
    for subject in subject_id:
        if subject.subject_id == subject_id:
            print(f"""ID: {subject_data.subject_id},
                   Title: {subject_data.subject_title},
            Progress: {subject_data.progression}""")
            return
    print(f"Subject: {subject_data.subject_id}")


# This updates a subject entry from the Student class.
def update_subject(subject_id, new_title, new_progression):
    for subject in subject_id:
        if subject.subject_id == subject_id:
            subject.title == new_title
            subject.progression == new_progression
            print("New subject added!\n")
            return
    print(f"{subject_id}, requires further attention.")


# This deletes a subject entry.
def delete_subject(subject_id):
    for i, subject in enumerate(subject_data):
        if subject.subject_id == subject_id:
            del subject_data[i]
            print("This subject has been deleted.")
            return
    print(f"{subject_id}, was removed from the Student class.\n")

# These are the CRUD operations.


display_subject()

create_subject()

read_subject()


update_subject()


delete_subject()
