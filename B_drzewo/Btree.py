# Skończone

class Element:
    def __init__(self, keys=None, children=None):

        if children is None:
            children = []

        if keys is None:
            keys = []

        self.children = keys
        self.keys = children


class BTree:
    def __init__(self, max_child_num):
        self.root = Element()
        self.max_child_num = max_child_num

    def insert(self, key):
        new, half = self._insert(key, self.root, None)
        if new is None and half is None:
            return None
        else:
            return new, half

    def _insert(self, key, node, parent, new=None, half=None):
        # Gdy węzeł to korzeń
        if node is self.root:

            # Węzeł nie ma dzieci
            if len(node.children) == 0:
                node.keys.append(key)
                node.children.append(None)
                node.children.append(None)
                return new, half

            if len(node.keys) == self.max_child_num - 1:
                node, new, half = self.split(node, parent)

        c = 0
        rever = node.keys[::-1]

        while rever[c] < key:

            c += 1
            if c == len(node.keys):
                c = len(node.keys)
                break
            if c == self.max_child_num - 2:
                c = self.max_child_num - 2
                break

        c = len(node.keys) - c

        # Liść
        if node.children[c] is None:
            node.keys = node.keys[:c] + [key] + node.keys[c:]
            node.children.append(None)
        else:

            # Gdy węzeł pełny
            if node.children[c] is not None and len(node.children[c].keys) == self.max_child_num - 1:
                _, new, half = self.split(node.children[c], node, c)

                if node.keys[c] > key:
                    self._insert(key, node.children[c + 1], node)
                else:
                    self._insert(key, node.children[c], node)
            else:
                self._insert(key, node.children[c], node)
        return new, half

    def split(self, node, parent, c=None):
        idx = self.max_child_num//2

        lk = node.keys[:idx - 1]
        childL = node.children[:idx]

        rk = node.keys[idx:]
        childR = node.children[idx:]

        left = Element()
        right = Element()

        left.keys = lk
        left.children = childL

        right.keys = rk
        right.children = childR

        if parent is None:
            self.root = Element()
            self.root.keys = [node.keys[idx - 1]]
            self.root.children = [left, right]

            return self.root, self.root, node.keys[idx-1]
        else:

            parent.keys = parent.keys[:c] + [node.keys[idx - 1]] + parent.keys[c:]
            parent.children = parent.children[:c] + [left, right] + parent.children[c + 1:]

            return node, node, node.keys[idx-1]

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            if node.keys is not None:
                for i in range(len(node.keys) + 1):
                    if node.children:
                        self._print_tree(node.children[i], lvl + 1)
                    if i < len(node.keys):
                        print(lvl*'  ', node.keys[i])


if __name__ == '__main__':

    # Utwórz puste drzewo o maksymalnej liczbie potomków równej 4
    b1 = BTree(4)

    # dodaj do niego elementy (będące jednocześnie kluczami) po kolei z listy:
    lista = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18, 15, 10, 19]

    for elem in lista:
        b1.insert(elem)

    # Wyświetl drzewo
    b1.print_tree()

    # Utwórz drugie puste drzewo, dodaj do niego 20 kolejnych liczb od 0 do 19
    # (będą to te same liczby co w liście ale dodane w kolejności rosnącej)
    b2 = BTree(4)

    l2 = list(range(20))
    for elem in l2:
        b2.insert(elem)

    # Wyświetl stworzone drzewo (zauważ jak różni się od poprzedniego)
    b2.print_tree()

    # Dodaj do drugiego drzewa kolejne liczby od 20 do 199, wyświetl drzewo
    # (zauważ jak wzrosła jego wysokość)
    l3 = list(range(20, 200))

    for elem in l3:
        b2.insert(elem)

    b2.print_tree()

    # wysokość wzrosła o jeden poziom

    # Utwórz trzecie puste drzewo o maksymalnej liczbie potomków równej 6, dodaj do niego te same liczby
    # co do drugiego drzewa (od 0 do 199) i wyświetl go (zauważ jak zmalała jego wysokość)
    b3 = BTree(6)

    l4 = list(range(200))

    for elem in l4:
        b3.insert(elem)

    b3.print_tree()

    # Wysokość drzewa zmalała o jeden poziom
