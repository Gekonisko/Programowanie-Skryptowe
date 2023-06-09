from inspect import signature


def argumenty(argumenty):
    def inner(f):
        def wew(*args, **kwargs):
            functionArg = len(signature(f).parameters)
            pArgs = list(args)
            k = functionArg - len(pArgs)
            if k > len(argumenty):
                raise TypeError(
                    f'{f.__name__}() takes exactly {functionArg} arguments ({len(argumenty) + len(pArgs)} given)')
            global last
            last = 0
            if len(list(args)) == 0:
                last = argumenty[functionArg]
            for i in range(0, k):
                pArgs.append(argumenty[i])
            return f(*pArgs)
        return wew
    return inner


def user(*args):
    pass


@user(admin)
class Operacje:
    argumentySuma = [4, 5]
    argumentyRoznica = [4, 5, 6]

    def __init__(self):
        self.update()

    @argumenty(argumentySuma)
    def suma(self, a, b, c):
        pass

    def updated_suma(self, a, b, c):
        if last != 0:
            return last
        else:
            return a + b + c

    @argumenty(argumentyRoznica)
    def roznica(self, x, y):
        pass

    def updated_roznica(self, x, y):
        if last != 0:
            return last
        else:
            return x - y

    def update(self):
        self.suma = (argumenty(Operacje.argumentySuma))(self.updated_suma)
        self.roznica = (argumenty(Operacje.argumentyRoznica))(self.updated_roznica)

    def __setitem__(self, key, value):
        for val in value:
            if type(val) != int:
                raise TypeError
        if key == 'suma':
            Operacje.argumentySuma = value
        elif key == 'roznica':
            Operacje.argumentyRoznica = value
        self.update()