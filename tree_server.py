class Item:
    id = None
    def serialize(self):
        pass
    def deserialize(self, data):
        pass
    def parents(self, tree):
        pass


class Folder(Item):
    def __init__(self):
        self.children = []
        
    def add_item(self, item, at=None):
        at = at or len(self.children)
        self.children.insert(at, item)
        
    def remove_item(self, item):
        pass
    def serialize(self):
        pass
    def deserialize(self, data):
        pass
    def get_item(self, id):
        pass

    @staticmethod
    def initialize_type(type, id=None):
        #set up new item
        item_class = Item if type == "item" else Folder
        item = item_class()
        item.id = id
        return item


class CourseData(Folder):
    def __init__(self):
        self.folder_structure = "[{'title':'', 'children':[]}]";
    
    def initialize_tree(self):
        tree = Folder()
        tree.deserialize(self.folder_structure)
        return tree
        
    def save_tree(self, tree):
        self.folder_structure = tree.serialize()

def add_item(cd, type, id, folder_id=None, position=None):
    tree = cd.initialize_tree()


    parent_folder = tree.get_item(id)
    parent_folder.add_item(item, at=position)

    cd.save_tree(tree)

def remove_item(cd, id):
    tree = cd.initialize_tree()

    item = tree.get_item(id)
    for parent in item.parents(tree):
        parent.remove_item(item)

    cd.save_tree(tree)

def move_item(cd, id, old_folder_id, new_folder_id, position):
    tree = cd.initialize_tree()

    old_folder = tree.get_item(old_folder_id)
    new_folder = tree.get_item(new_folder_id)
    item = old_folder.get_item(id)

    old_folder.remove_item(item)
    new_folder.insert_item(item, at=position)

    cd.save_tree(tree)

def set_folder_hidden(fs, folder_id, hidden_status):
    pass


##f = Folder()
##f.deserilize(course_data.folder_structure)
##....
##course_data.folder_structure = f.serialize()
##course_data.save()

#class FolderStructure():
    #folder_structure = '[]'

    #def decode(self):
        #return simplejson.loads(self.folder_structure)

    #def encode(self, folder_json):
        #self.folder_structure = simplejson.loads(folder_json)

    #def serialized(self):
        #structure = self.decode()
        #structure = [{"children": structure}]
        #return simplejson.dumps(structure)

    #def set_folder_hidden(self, id, hidden_status):
        #pass

    #def generate_item(self, type, id):
        #if type == "folder":
            #return {
                #"title": id,
                #"children": [],
                #"hidden": False,
                #"constructor_ref": "FolderConstructorRef"
            #}
        #elif type == "module_item":
            #return {
                #"title": id,
                #"constructor_ref": "TreeItemConstructorRef"
            #}

    #def add_child(self, folder, item):
        #pass
    #def remove_child(self, folder, item):
        #pass
    #def move_child(self, folder, item):
        #pass
##    def add_item(self, type, id):
##        structure = self.decode()
##        structure.append( self.generate_item(type, id) )
##        self.structure = self.encode(structure)
##
##    def move_item(self, type, id, parent_folder, position):
##        item = self.get_item(type, id)
##        self.remove_item(item)
##        self.add_item(item, parent_folder, position)
##
##    def remove_item(self, type, id):
##        structure = self.decode()
##
##        def navigate(items):
##            for item in items:
##                if item["title"] == id:
##                    return item
##        navigate(structure)
##
##
##        self.structure = self.encode(structure)
