#!/usr/bin/python3
# -*- coding: utf-8 -*-

class ClassLoaderException(Exception):
    pass

class ClassLoader():
    """ loads class from the given module path """

    def load(self, module_path, classname):

        try:
            # import the class
            #mod_to_import = path.join(module_path, classname.lower()).replace('/','.')
            mod_to_import = module_path.replace('/','.')

            mod = __import__(mod_to_import, fromlist=[classname])
            LoadedClass = getattr(mod, classname)

        except:
            raise ClassLoaderException('Unable to load class')

        return LoadedClass