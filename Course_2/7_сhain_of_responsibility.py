GLOBAL_INT = "INT"
GLOBAL_FLOAT = "FLOAT"
GLOBAL_STRING = "STRING"


class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, _type):
        self.type_ = _type


class EventSet:
    def __init__(self, _value):
        self.value_ = _value


class NullHandler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, obj, event):
        if self._successor is not None:
            return self._successor.handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and event.type_ is str:
            return obj.string_field
        elif isinstance(event, EventSet) and type(event.value_) is str:
            obj.string_field = event.value_
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and event.type_ is float:
            return obj.float_field
        elif isinstance(event, EventSet) and type(event.value_) is float:
            obj.float_field = event.value_
        else:
            return super().handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet) and event.type_ is int:
            return obj.integer_field
        elif isinstance(event, EventSet) and type(event.value_) is int:
            obj.integer_field = event.value_
        else:
            return super().handle(obj, event)


if __name__=='__main__':

    obj = SomeObject()
    obj.integer_field = 433
    obj.float_field = 3.1425972
    obj.string_field = "shoot"
    chain = IntHandler(FloatHandler(StrHandler(NullHandler())))

    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))
    print(chain.handle(obj, EventSet(100)))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventSet('new text')))
    print(chain.handle(obj, EventGet(str)))
    print(chain.handle(obj, EventSet(0.5)))

