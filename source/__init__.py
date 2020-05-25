# -*- coding: utf-8 -*-

__all__ = []

import pkgutil
import inspect

# формируем ассоциативный массив имён функций и самих функций, вложенных в директории
module_dict = dict()

for loader, name, is_pkg in pkgutil.walk_packages(__path__):
    module = loader.find_module(name).load_module(name)
    modname = name.split('.')[-1]  # имя модуля
    for def_name, value in inspect.getmembers(module):
        if inspect.isfunction(value):
            if inspect.getmodulename(inspect.getfile(value)) == modname:  # если функция определена в этом файле
                module_dict[def_name] = value


__all__.append(module_dict)