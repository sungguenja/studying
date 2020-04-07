import collections
import re
import os

now = []
f = open('villagers.txt', 'r', encoding='utf-8')
gate=[]

for line, value in enumerate(f):
    gate.append(value[:-1])
    if line%7==6:
        now.append(gate)
        gate=[]



f.close()
context = {
    'now': now
}
print(context)