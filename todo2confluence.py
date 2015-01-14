#!/usr/bin/env python
# this is just a script you can use if you happen to be in the situation I was where you want your team to be aware of  your progress and  tasks and you're using todo.txt app on android and want to use that app to send your todo list to confluence if it's on a private network and you can't do it the usual way, todo.txt android stores in a text file on dropbox, you sync that to a linux box then run this as a cronjob, simple but works
# see https://github.com/ginatrapani/todo.txt-android and 
import sys
from xmlrpclib import Server
import fileinput

# read the todo.txt file
import os

os.system('/home/username/Dropbox/todo/todo.sh -@p ls @work > /home/username/Dropbox/todo/xmlrpc/todo.txt')

f = open('/home/username/Dropbox/todo/xmlrpc/todo.txt')
linelist = f.readlines()
content = '<br/>'.join(map(str,linelist))

#update page

s = Server("http://yourconfluence/rpc/xmlrpc")
token = s.confluence2.login("name", "password")
page = s.confluence2.getPage(token, "~name", "todo.txt")
page["content"] = content
s.confluence2.storePage(token, page)

