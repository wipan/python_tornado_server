# Handlers of each request routing

from tornado.web import RequestHandler

# Main Page
class MainHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("This is a tornado project server\n")
        self.set_header("traceId", "xyz")

# Post Information Page
class PostPageHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("postpage.html")
    def post(self, *args, **kwargs):
        name = self.get_body_argument("username")
        passwd = self.get_body_argument("passwd")
        hobby_list = self.get_body_arguments("hobby")
        print("Name is: " + name)
        print("Password is: xxx" + passwd + "xxx")
        for hobby in hobby_list:
            print("Hobby are: " + hobby)
        self.write("login successfully!")

# Home
class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("This is a tornado project server\n")
        temp = 10
        flag = 1
        self.render("home.html", num = temp, flag = flag)

# Function render
class FuncHandler(RequestHandler):
    def get(self, *args, **kwargs):
        def my_sum(a, b):
            return a + b
        self.render("function.html", my_sum = my_sum)

# Escape
# tornado默认转义
class EscapeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h1>This is a tornado server</h1>"
        self.render("escape.html", str = str)

# templates 用遍历
class StudentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        students = [
            {
                'name': 'Alex',
                'age': 18
            },
            {
                'name': 'Bob',
                'age': 17
            }
        ]
        self.render("students.html", students = students)



