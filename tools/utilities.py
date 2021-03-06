#------------------------------------------------------------------------------
#
# Copyright (c) 2014 Glympse Inc.  All rights reserved.
#
#------------------------------------------------------------------------------

import os
import json


class File:

    @staticmethod
    def read(path):          
        file = open(path, "r")
        text = file.read() 
        file.close()
        return text

    @staticmethod
    def write(path, text):   
        file = open(path, "w")        
        file.write(text) 
        file.close()

    @staticmethod
    def read_json(path):     
        return json.loads(File.read(path))

    @staticmethod
    def write_json(path, obj):   
        File.write(path, json.dumps(obj, indent=2, separators=(',', ': ')))

    @staticmethod
    def read_relative(path):
        absolute_path = "{}/{}".format(File.local_path(), path)
        return File.read(absolute_path)

    @staticmethod
    def local_path():
        return os.path.dirname(os.path.realpath(__file__))
