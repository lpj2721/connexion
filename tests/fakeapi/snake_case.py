#!/usr/bin/env python3
def get_path_snake(some_id):
    data = {'SomeId': some_id}
    return data


def get_path_shadow(id_):
    data = {'id': id_}
    return data


def get_query_snake(some_id):
    data = {'someId': some_id}
    return data


def get_query_shadow(list_):
    data = {'list': list_}
    return data


def post_path_snake(some_id, some_other_id):
    data = {'SomeId': some_id, 'SomeOtherId': some_other_id}
    return data


def post_path_shadow(id_, reduce_):
    data = {'id': id_, 'reduce': reduce_}
    return data


def post_query_snake(some_id, some_other_id):
    data = {'someId': some_id, 'someOtherId': some_other_id}
    return data


def post_query_shadow(id_, format_):
    data = {'id': id_, 'format': format_}
    return data
