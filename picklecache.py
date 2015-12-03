#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Pickle cache module """

import os
import pickle


class PickleCache(object):
    """ Pickle caching class """
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """
        Constructor
        Args:
            file_path (String): Path to pickle file
            autosync (Bool): Autosync flag
        Attributes:
            __file_path (String): Path to pickle file
            __data (Dict): Dictionary of data to pickle
        Examples:
            >>> pcache = PickleCache()
            >>> pcache._PickleCache__file_path
            'datastore.pkl'
            >>> pcache._PickleCache__data
            {}
        """

        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        try:
            self.load()
        except OSError:
            print 'Could not find file ' + self.__file_path

    def __setitem__(self, key, value):
        """
        Store value pairs
        Args:
            key (Mixed): Dict key
            value (Mixed): Value
        Attributes"
        Examples:
            >>> pcache['test'] = 'Hello'
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()
        else:
            print 'Autosync is false'
            print self.autosync

    def __len__(self):
        """ Return length of stored data """
        return len(self.__data)

    def __getitem__(self, key):
        """
        Returns value of stored data
        Args:
            key (Mixed): Dict key
        Attributes:
        Examples:
            >>> pcache['test']
            >>> pcache['test']
            Hello
        """
        return self.__data[key]

    def __delitem__(self, key):
        """
        Delete a stored item
        Args:
            key (Mixed): Dict key
        Attributes:
        Examples:
            >>> del pcache['key']
        """
        del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """
        Loads contents of pickle file
        Args:
        Attributes:
        Examples:
            >>> PickleCache('infile.pkl')
        """

        exists = os.path.exists(self.__file_path)
        nzfile = (os.path.getsize(self.__file_path) > 0)

        if exists and nzfile:
            try:
                with open(self.__file_path, 'r') as pklfile:
                    self.__data = pickle.load(pklfile)
            except IOError:
                print 'Could not open ' + self.__file_path
            else:
                return True

        return False

    def flush(self):
        """
        Flushes pickled object to file
        Args:
        Attributes:
        Examples:
            >>> PickleCache.flush()
        """
        try:
            with open(self.__file_path, 'w') as pklfile:
                pickle.dump(self.__data, pklfile)
        except IOError:
            print 'An IO error occured to file ' + self.__file_path
        else:
            return True

        return False
