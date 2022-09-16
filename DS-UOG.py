try:
    class BSTNode(object):

        def __init__(self, char: str):
            self.right = ""
            self.left = ""
            self.key = char


    def search(key, node):
        found = False
        if node.key:
            if key == node.key:
                found = True
            if key < node.key and node.left:
                found = False
                return search(key, node.left)
            if key > node.key and node.right:
                found = False
                return search(key, node.right)
            if not found:
                return False
            else:
                return True


    def add(key, node):
        if node.key:
            if key == node.key:
                return node
            if key < node.key and node.key:
                if not node.left:
                    newed = BSTNode(key)
                    node.left = newed
                    return "{} is added.".format(key)
                return add(key, node.left)
            if key > node.key and node.key:
                if not node.right:
                    newed = BSTNode(key)
                    node.right = newed
                    return "{} is added.".format(key)
                return add(key, node.right)


    def dell(key, node):

        if node.key:
            if key == node.key:
                node.key = ""
                return "{} is removed .".format(key)

            if key < node.key:
                return dell(key, node.left)
            if key > node.key:
                return dell(key, node.right)


    def edit(key, node, word):
        w = word
        if node.key:
            if key == node.key:
                node.key = word
                return "{} is edited .".format(key)

            if key < node.key and node.left:
                return edit(key, node.left, w)
            if key > node.key and node.right:
                return edit(key, node.right, w)


    allwords = list()
    root = BSTNode("#")
    while True:
        print("What do you want to do? \nPlease insert the relevant key and press Enter.")
        print("Q->build BST with file.")
        print("E->add a word.")
        print("W->check a file.")
        print("R->check a word.")
        print("T->delete a word.")
        print("X->edit a word.")
        print("Y->print all words.")
        print("U->exit.")
        x = input("")
        key = x.lower()
        if key == "q":
            # generate a tree
            address = "E:/sample3.txt"
            f = open(address)
            for line in f:
                line = line.replace(".", " ")  # replace . with sapce
                line = line.replace(",", " ")  # replace , with space
                line = line.rstrip()  # remove \n end of line
                words = line.split()  # split all word  in line.
                i = 0
                for word in words:
                    if len(word) >= 3:
                        add(word, root)
                        allwords.append(word)
            mword = allwords
            allwords = list(dict.fromkeys(mword))
        if key == 'w':
            # find a file words
            address = "E:/sample3.txt"
            f = open(address)
            for xline in f:
                xline = xline.replace(".", " ")
                xline = xline.replace(",", " ")
                xline = xline.rstrip()
                words = xline.split()
                i = 0
                for word in words:
                    if search(word, root) is None:
                        print("{} is False".format(word))
                    else:
                        print(word, " is ", search(word, root))
        if key == 'e':
            # add a word to tree
            x = input("Enter the word:")
            wordinsert = x
            add(wordinsert, root)
            allwords.append(wordinsert)
            mword = allwords
            allwords = list(dict.fromkeys(mword))
        if key == 'r':
            # find a word in tree
            x = input("Enter the word:")
            if search(x, root) is None:
                print("{} is False".format(x))
            else:
                print(x, " is ", search(x, root))
        if key == 't':
            # delete a word in tree
            x = input("Enter the word:")
            wordinsert = x
            if search(wordinsert, root) is True:
                print(dell(wordinsert, root))
            else:
                print("not exist!")
            for m in range(len(allwords) - 1):
                if wordinsert == allwords[m - 1]:
                    del (allwords[m - 1])

        if key == 'x':
            key = input("Which word do you want to edit ?:")
            if search(key, root) is None:
                print("Not exist!.")
                break
            print("What word do you want to put instead of ", key, "?:")
            word = input("insert:")
            if len(word) > 2:
                print(edit(key, root, word))
                for m in range(len(allwords) - 1):
                    if key == allwords[m - 1]:
                        del (allwords[m - 1])
                allwords.append(word)
            else:
                print("enter larger than 3 alphabet")
        if key == 'y':
            print(sorted(allwords))
        if key == "u":
            break
except IOError as e:
    print("Several errors were received as %s " % e)
# Reza Chabok
