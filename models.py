from forms import Form

class Post(Form):
    pass

class Tag:
    def out_print(self):
        print("World")

p = Post
p.charfield(88)

t = Tag
t.out_print("")
