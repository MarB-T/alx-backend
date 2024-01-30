#!/usr/bin/env python3
""" simple helper function """


def index_range(page, page_size):
    """ Gets the start and end index for a given page. """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return ((start_index, end_index))
