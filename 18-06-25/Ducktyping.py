#ducktyping
class duck:
    def Walk(self):
        print("thapak thapak thapak thapak")
class Horse:
    def Walk(self):
        print("tabdak tabdak tabdak tabdak")
def myfunction(obj):
    obj.Walk()
d = duck()
myfunction(d)
h = Horse()
myfunction(h)
