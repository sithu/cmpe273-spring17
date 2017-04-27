# -*- coding: utf-8 -*-

print "Loading function..."

def handler(event, context):
    print "Hello World"
    print event
    # Your code goes here!
    #e = event.get('e')
    #pi = event.get('pi')
    return "OK"
