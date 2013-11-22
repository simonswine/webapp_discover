from copy import deepcopy

__author__ = 'christian'

import os

class FileTree(object):

    @classmethod
    def file_list2dict(cls,file_list):

        tree = {}

        for file in file_list:

            # Split path
            file_split = file.split('/')

            # Remove starting with . or ..
            if file_split[0] in ['.' or '..'] and len(file_split) > 1:
                del file_split[0]

            FileTree.add_to_dict(tree,file_split)

        # TODO LOG print(FileTree.dict_count(tree),len(file_list))

        return tree


    @classmethod
    def add_to_dict(cls,d, file_list):

        first_key = file_list.pop(0)

        if len(file_list) > 0:
            # Not last key -> i'm a dir

            if not first_key in d:
                # Create if not exist
                d[first_key] = {}

            # Recurse
            FileTree.add_to_dict(d[first_key],file_list)

        else:
            # i'm a file

            if first_key in d:
                # should never happen
                raise RuntimeError("Key shouldn't exist")

            d[first_key] = {}

    @classmethod
    def dict_count(cls,d):

        count = 0

        for key in d.keys():
            if d[key] == {}:
                count += 1
            else:
                count += FileTree.dict_count(d[key])

        return count

    @classmethod
    def check_recurse(self,path,d):

        queue_delete = []
        queue_recurse = []

        # Check for files on my level
        for key in d.keys():
            key_path = os.path.join(path,key)
            if os.path.exists(key_path):
                if d[key] != {}:
                    queue_recurse.append((key_path,d[key]))
            else:
                queue_delete.append(key)

        # Remove entries not found
        for key in queue_delete:
            del d[key]
        for args in queue_recurse:
            FileTree.check_recurse(*args)




    def __init__(self,file_list):

        self.dict = FileTree.file_list2dict(file_list)#


    def check(self,path,ratio=0.7):

        # TODO implement early continue

        d = deepcopy(self.dict)
        len_d = FileTree.dict_count(d)

        FileTree.check_recurse(path,d)


        return FileTree.dict_count(d)/len_d


