import sys, os
sys.path.append('../')

from fileRetrieval import path_list

def test_fileRetrieval():
    file_list, dir_list = path_list('enron/maildir/allen-p/')
    assert type(file_list) == list
    assert type(dir_list) == list
    #assert path_list('./enron/maildir/allen-p/')
    #assert path_list('enron/maildir/allen-p')
    #assert path_list('/enron/maildir/allen-p/')
    #assert path_list('/enron/maildir/allen-p')