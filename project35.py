#Build a Mini Social Media Platform Problem: Design classes for User, Post, and Comment. Users can post messages, like posts, and comment. Use object relationships (e.g., posts have comments), class variables to count total posts, and override the string representation methods to print user-friendly content.
class User:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def create_post(self, msg):
        p = Post(msg, self)
        self.posts.append(p)
        return p


class Post:
    total_posts = 0

    def __init__(self, msg, user):
        self.msg = msg
        self.user = user
        self.comments = []
        self.likes = 0
        Post.total_posts += 1

    def add_comment(self, text):
        c = Comment(text)
        self.comments.append(c)

    def like(self):
        self.likes += 1

    def show(self):
        print("\nPost by:", self.user.name)
        print("Message:", self.msg)
        print("Likes:", self.likes)
        print("Comments:")
        for c in self.comments:
            print("-", c.text)


class Comment:
    def __init__(self, text):
        self.text = text


# usage
u1 = User("Dibyajyoti")

p1 = u1.create_post("Hello World!")
p1.like()
p1.like()
p1.add_comment("Nice post")
p1.add_comment("Awesome")

p1.show()

print("Total Posts:", Post.total_posts)