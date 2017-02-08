class A:
    message = "class message"

    @classmethod
    def cfoo(cls):
        print(cls.message)

    def foo(self, msg):
        self.message = msg
        print(self.message)

    @staticmethod
    def sfoo():
        print('Static Method')

if __name__ == '__main__':
    a = A()
    A.cfoo()
    a.foo('Instance method')
    A.sfoo()

