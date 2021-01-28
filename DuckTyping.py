# Duck Typing:

class PyCharm:
              def execute(self):
                             print("Compiling")
                             print("Running")

class MyEditor:
              def execute(self):
                             print("Spell check")
                             print("Convention Check")
                             print("Compiling"
                             print("Running")

class Laptop:
              def code(self,ide):
                             ide.execute(self)

ide=PyCharm() #or ide=MyEditor
lap1=Laptop()
lap1.code(ide)
