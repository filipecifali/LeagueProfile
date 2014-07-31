__author__ = 'filipe'


class Sample():
    # old-style object
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


p1 = Sample('Filipe', 'Cifali')
print p1.name
print p1.surname

p2 = Sample('Rafael', 'Araujo')
print p2.name, p2.surname


class Parent(object):
    def implicit(self):
        print "%s implicit()" % self.__class__.__name__


class Child(Parent):
    pass


pai = Parent()
filho = Child()

print pai.implicit()
print filho.implicit()

variavel = 'Filipe'

for l in variavel:
    print l


print 10 * variavel

len(variavel)

variavel.__len__()

type(variavel)
type(10)
type(2.1)

import sys

print sys.argv

import re

re.findall(r'\bK[a-z]*', 'KingHost, WebHosting King')

import os

print os.name
print os.getuid()
print os.uname()


import sys

print sys.path

from sys import path
print path

import this

print this

'''O Zen do Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Linear é melhor do que aninhado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Ainda que praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambigüidade, recuse a tentação de adivinhar.
Deveria haver um — e preferencialmente só um — modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca freqüentemente seja melhor que *já*.
Se a implementação é difícil de explicar, é uma má idéia.
Se a implementação é fácil de explicar, pode ser uma boa idéia.
Namespaces são uma grande idéia — vamos ter mais dessas!'''

# pip install wheel

import sys

sys.path.insert(0, '/Users/filipecifalistangler/.site-packages')

import site

site.addsitedir('/Users/filipecifalistangler/.python-eggs')

print site.sys.path
