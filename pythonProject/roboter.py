import csv
import string
import termcolor
import os
import sys

colord = termcolor.colored
grn = "green"

class robot(object):

    def greeting(self):
        with open('text_template/greetmg.txt', encoding="utf-8") as grt:
            t = string.Template(grt.read())
            grt_contents = t.substitute()
            name = input(colord(grt_contents, grn))
            return name

    def asking(self, name):
        with open('text_template/ask.txt', encoding="utf-8") as ask:
            a = string.Template(ask.read())
            ask_contents = a.substitute(name= name)
            rst = input(colord(ask_contents, grn))
            return rst

    def byebye(self, name):
        with open('text_template/byebye.txt', encoding="utf-8") as byb:
            b = string.Template(byb.read())
            byb_contents = b.substitute(name= name)
            print(colord(byb_contents,grn))

