# Skończone

class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class TreeAVL:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        self.root = self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if node is None:
            node = Element(key, data)
        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        else:
            node.data = data
            
        if self._height(node.left) > self._height(node.right):
            node.height = 1 + self._height(node.left)
        else:
            node.height = 1 + self._height(node.right)

        if node is None:
            ww = 0
        else:
            ww = self._height(node.left) - self._height(node.right)

        if ww > 1:
            # LL
            if key < node.left.key:
                return self.rotate_right(node)
            # LR
            elif key > node.left.key:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        elif ww < -1:
            # RR
            if key > node.right.key:
                return self.rotate_left(node)

            # RL
            elif key < node.right.key:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def rotate_right(self, node):
        l = node.left
        lr = node.left.right

        l.right = node
        node.left = lr

        if self._height(node.left) > self._height(node.right):
            node.height = 1 + self._height(node.left)
        else:
            node.height = 1 + self._height(node.right)

        if self._height(l.left) > self._height(l.right):
            l.height = 1 + self._height(l.left)
        else:
            l.height = 1 + self._height(l.right)

        return l

    def rotate_left(self, node):
        r = node.right
        rl = node.right.left

        r.left = node
        node.right = rl

        if self._height(node.left) > self._height(node.right):
            node.height = 1 + self._height(node.left)
        else:
            node.height = 1 + self._height(node.right)

        if self._height(r.left) > self._height(r.right):
            r.height = 1 + self._height(r.left)
        else:
            r.height = 1 + self._height(r.right)

        return r

    def search(self, key):
        ans = self._search(self.root, key)
        if ans is None:
            raise Exception('Nie ma takiego klucza')
        else:
            return self._search(self.root, key)

    def _search(self, node, key, counter=0):
        if node is None:
            return None
        if key < node.key:
            counter += 1
            return self._search(node.left, key, counter)
        elif key > node.key:
            counter += 1
            return self._search(node.right, key, counter)
        else:
            return node.data, counter

    def delete(self, key):
        ans = self.search(key)
        if ans is None:
            raise Exception('Nie można usunąć')
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        elif key == node.key:
            if node.right is None and node.left is None:
                node = None

            elif node.left is None:
                child_right = node.right
                node = None
                return child_right

            elif node.right is None:
                child_left = node.left
                node = None
                return child_left

            else:
                helper = node.right
                while helper.left is not None:
                    helper = helper.left
                node.key = helper.key
                node.data = helper.data
                node.right = self._delete(node.right, helper.key)

        if node is None:
            return None

        if self._height(node.left) > self._height(node.right):
            node.height = 1 + self._height(node.left)
        else:
            node.height = 1 + self._height(node.right)

        if node is None:
            ww = 0
        else:
            ww = self._height(node.left) - self._height(node.right)

        if ww > 1:
            if node.left is None:
                wwl = 0
            else:
                wwl = self._height(node.left.left) - self._height(node.left.right)

            # LL
            if wwl > 0:
                return self.rotate_right(node)
            # LR
            elif wwl < 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        elif ww < -1:
            if node.right is None:
                wwr = 0
            else:
                wwr = self._height(node.right.left) - self._height(node.right.right)
                
            # RR
            if wwr < 0:
                return self.rotate_left(node)

            # RL
            elif wwr > 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
        return node

    def print(self):
        kl = dict()
        k = self._print(self.root, kl)
        new_k = sorted(k.items())
        text = '{'
        for i in range(len(new_k)):
            text += f'{new_k[i][0]}:{new_k[i][1]}'
            if i != len(new_k)-1:
                text += ', '
            else:
                text += '}'
        print(text)

    def _print(self, node, kl):
        if node is None:
            return None
        else:
            kl[node.key] = node.data
            self._print(node.left, kl)
            self._print(node.right, kl)
        return kl

    def height(self, key):
        if key == self.root.key:
            return self._height(self.root)
        else:
            try:
                _, counter = self.search(key)
                return self._height(self.root) - counter
            except:
                raise Exception('Nie znaleziono klucza')

    def _height(self, node):
        if node is None:
            return 0
        else:
            left = self._height(node.left)
            right = self._height(node.right)

            if right > left:
                right += 1
                return right
            else:
                left += 1
                return left

    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            self._print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.data)

            self._print_tree(node.left, lvl + 5)


if __name__ == '__main__':
    # Utworzenie pustego drzewa BST
    tree = TreeAVL()

    d = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 2: 'E', 1: 'F', 11: 'G', 100: 'H', 7: 'I',  6: 'J', 55: 'K', 52: 'L',
         51: 'M', 57: 'N', 8: 'O', 9: 'P', 10: 'R', 99: 'S', 12: 'T'}

    # Dodanie kolejno elementy klucz:wartość
    for k, v in d.items():
        tree.insert(k, v)

    # Wyświetl drzewo 2D
    tree.print_tree()

    # Wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
    tree.print()

    # Wyszukaj element o kluczu 10 i wypisz wartość
    print(tree.search(10)[0])

    # Usuń element o kluczu 50
    tree.delete(50)

    # Usuń element o kluczu 52
    tree.delete(52)

    # Usuń element o kluczu 11
    tree.delete(11)

    # Usuń element o kluczu 57
    tree.delete(57)

    # Usuń element o kluczu 1
    tree.delete(1)

    # Usuń element o kluczu 12
    tree.delete(12)

    # Dodaj element o kluczu 3:AA
    tree.insert(3, "AA")

    # Dodaj element o kluczu 4:BB
    tree.insert(4, "BB")

    # Usuń element o kluczu 7
    tree.delete(7)

    # Usuń element o kluczu 8
    tree.delete(8)

    # Wyświetl drzewo 2D
    tree.print_tree()

    # Wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
    tree.print()
