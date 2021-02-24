import time


class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42

    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


class Foo():
    attribute1 = Verbose_attribute()


class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

    # Makes data desctiptor changes place in lookup ordes and it does not work
    # def __set__(self, obj, value):
        # pass


class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return "Be happy!!!"


# D.R.Y
class EvenNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = (value if value % 2 == 0 else 0)


class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()
    value5 = EvenNumber()


if __name__ == "__main__":
    my_foo_object = Foo()
    x = my_foo_object.attribute1
    print(x)
    print(getattr(my_foo_object, "attribute1"))
    print(my_foo_object.__dict__)

    my_deep_thought_instance = DeepThought()
    print(my_deep_thought_instance.meaning_of_life)
    print(my_deep_thought_instance.meaning_of_life)
    print(my_deep_thought_instance.meaning_of_life)

    my_values = Values()
    my_values.value1 = 1
    my_values.value2 = 4
    print(my_values.value1)
    print(my_values.value2)
