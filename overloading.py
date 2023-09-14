class A:
    def show(self):
        print("Welcome")

    def show(self, first_name=' '):
        print("welcome", first_name)

    def show(self, first_name=' ', last_name=' '):
        print("Welcome", first_name, last_name)


obj = A()
obj.show()
obj.show("suraj")
obj.show('Suraj', 'Raju')


