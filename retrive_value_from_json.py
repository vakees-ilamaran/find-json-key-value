#!/usr/bin/env python3

"""
Description:
    Retrive the value from a nested object from the given key
Abstract: 
    We have a nested object, we would like a function that you pass in the object and a key and get back the value.
    Example Inputs
        object = {“a”:{“b”:{“c”:”d”}}}
        key = a/b/c
        Output: value = 'd'

        object = {“x”:{“y”:{“z”:”a”}}}
        key = x/y/z
        Output: value = a
Author: 
    vakees.ilamaran@gmail.com
"""

import click
import json

@click.command()
@click.option('--obj', required=True)
@click.option("--val", required=True, help='The value to find.')
def get_nested_value_from_object(obj: dict, val: str) -> None:
    obj = json.loads(obj)
    path_to_the_value = val.split('/')
    for path in path_to_the_value:
        obj = obj[path]
    print(obj)

if __name__ == '__main__':
    try:
        get_nested_value_from_object()
    except Exception as e:
        raise Exception('Script Failed while calling the function') from e