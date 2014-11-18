__author__ = 'Alicia'
import copy


class Foo:  #1
    notagoodidea = "What am I now?"

you = Foo()  #2
you.notagoodidea = "Who knows"

youtoo = you
youtoo.notagoodidea = "who's on first?"

print(Foo.notagoodidea)  #4
print(you.notagoodidea)
print(youtoo.notagoodidea)
print('\n')

youwho = copy.copy(you)  #5
youwho.notagoodidea = "I'm lost"

print(Foo.notagoodidea, id(Foo.notagoodidea), id(Foo))  #6 this means that objects and classes are mutable so when we
print(you.notagoodidea, id(you.notagoodidea), id(you))  #created the alias and changed the value it also changed the original.
print(youtoo.notagoodidea, id(youtoo.notagoodidea), id(youtoo))
print(youwho.notagoodidea, id(youwho.notagoodidea), id(youwho))


