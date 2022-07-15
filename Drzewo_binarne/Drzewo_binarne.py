# Skończone

class Element:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class TreeBST:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = Element(key, data)
        else:
            self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if node is None:
            node = Element(key, data)
        if key < node.key:
            node.left = self._insert(node.left, key, data)
        elif key > node.key:
            node.right = self._insert(node.right, key, data)
        else:
            node.data = data
        return node

    def search(self, key):
        if not isinstance(key, int):
            raise Exception('Niepoprawnie wprowadzony klucz')
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
        return self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
            return node

        elif key > node.key:
            node.right = self._delete(node.right, key)
            return node

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
    tree = TreeBST()

    d = {50: 'A', 15: 'B', 62: 'C', 5: 'D', 20: 'E', 58: 'F', 91: 'G', 3: 'H', 8: 'I', 37: 'J', 60: 'K', 24: 'L'}

    # Dodanie kolejno elementy klucz:wartość
    for k, v in d.items():
        tree.insert(k, v)

    # Wyświetl drzewo 2D
    tree.print_tree()

    # Wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
    tree.print()

    # Znajdź klucz 24 i wypisz wartość
    print(tree.search(24)[0])

    # Zaktualizuj wartość "AA" dla klucza 20
    tree.insert(20, "AA")

    # Dodaj element 6:M
    tree.insert(6, "M")

    # Usuń element o kluczu 62
    tree.delete(62)

    # Dodaj element 59:N
    tree.insert(59, "N")

    # Dodaj element 100:P
    tree.insert(100, "P")

    # Usuń element o kluczu 8
    tree.delete(8)

    # Usuń element o kluczu 15
    tree.delete(15)

    # Wstaw element 55:R
    tree.insert(55, "R")

    # Usuń element o kluczu 50
    tree.delete(50)

    # Usuń element o kluczu 5
    tree.delete(5)

    # Usuń element o kluczu 24
    tree.delete(24)

    # Wypisz wysokość drzewa
    print(tree.height(55))

    # Wyświetl zawartość drzewa jako listę od najmniejszego do największego klucza w formie klucz:wartość
    tree.print()

    # Wyświetl drzewo 2D
    tree.print_tree()
