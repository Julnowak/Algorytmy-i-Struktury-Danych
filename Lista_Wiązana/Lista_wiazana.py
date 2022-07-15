# Skończone

class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def destroy(self):
        if self.head is None:
            raise Exception('Lista jest już pusta')
        else:
            self.head = None

    def add(self, new_elem):
        new_elem.next = self.head
        self.head = new_elem

    def remove(self):
        if self.head is None:
            raise Exception('Nie można usuwać z pustej listy')
        else:
            self.head = self.head.next

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def length(self):
        length = 0
        elem = self.head
        while elem is not None:
            elem = elem.next
            length += 1
        return length

    def add_end(self, new_elem):
        elem = self.head

        if elem is None:
            elem.head = new_elem
        else:
            while elem.next is not None:
                elem = elem.next
            elem.next = new_elem

    def remove_end(self):
        elem = self.head

        if elem is None:
            raise Exception('Nie można usuwać z pustej listy')
        elif elem.next is None:
            self.head = None
        else:
            while elem.next.next is not None:
                elem = elem.next
            elem.next = None

    def get(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def __str__(self):
        elem = self.head
        text = ""
        i = 0
        while elem is not None:
            if i == 3:
                text += '\n(' + str(elem.data[0]) + ', ' + str(elem.data[1]) + ', ' + str(elem.data[2]) + ') -> '
            else:
                text += '(' + str(elem.data[0]) + ', ' + str(elem.data[1]) + ', ' + str(elem.data[2]) + ') -> '
            elem = elem.next
            i += 1
        text += 'None'
        return text

    def take(self, n: int):
        if isinstance(n, int) and n >= 0:
            new_linkedlist = Linkedlist()

            if self.length() == 0 or n == 0:
                return new_linkedlist

            if n > self.length():
                n = self.length()

            elem = self.head
            new_linkedlist.head = Element(elem.data)
            if self.length() != 1:
                for k in range(n - 1):
                    elem = elem.next
                    new_linkedlist.add_end(Element(elem.data))
            return new_linkedlist
        else:
            raise Exception('Wpisano niepoprawną wartość n')

    def drop(self, n):
        if isinstance(n, int) and n >= 0:
            new_linkedlist = Linkedlist()

            if n >= self.length():
                return new_linkedlist

            elem = self.head

            for u in range(n):
                elem = elem.next

            new_linkedlist.head = Element(elem.data)

            while elem.next is not None:
                elem = elem.next
                new_linkedlist.add_end(Element(elem.data))
            return new_linkedlist
        else:
            raise Exception('Wpisano niepoprawną wartość n')


if __name__ == '__main__':

    # Utworzenie listy Elementów
    lis = [('AGH', 'Kraków', 1919), ('UJ', 'Kraków', 1364),
       ('PW', 'Warszawa', 1915), ('UW', 'Warszawa', 1915),
       ('UP', 'Poznań', 1919), ('PG', 'Gdańsk', 1945)]
    elem_list = []

    for i in lis:
        elem_list.append(Element(i))

    # Tworzenie listy wiązanej jednokierunkowej przy pomocy konstruktora
    lista = Linkedlist()

    # Sprawdzenie, czy utworzona lista jest pusta, przy pomocy metody is_empty()
    print('---------- TESTOWANIE METODY IS_EMPTY (PUSTA LISTA) ----------')
    print(f'Czy lista jes pusta? {lista.is_empty()}\n\n')

    print('---------- TESTOWANIE METOD DODAWANIA ----------')
    # Ustawienie pierwszego elementu (głowy)

    lista.head = elem_list[2]
    print('Dodano głowę listy wiązanej jednokierunkowej')
    print(f'{lista}\n')

    # Dodanie elementów z tyłu listy
    lista.add_end(elem_list[3])
    print('Dodano element z tyłu listy')
    print(f'{lista}\n')

    lista.add_end(elem_list[4])
    print('Dodano element z tyłu listy')
    print(f'{lista}\n')

    lista.add_end(elem_list[5])
    print('Dodano element z tyłu listy')
    print(f'{lista}\n')

    # Dodanie elementów z przodu listy
    lista.add(elem_list[1])
    print('Dodano element z przodu listy')
    print(f'{lista}\n')

    lista.add(elem_list[0])
    print('Dodano element z przodu listy')
    print(f'{lista}\n\n')

    print('---------- TESTOWANIE METODY IS_EMPTY (NIEPUSTA LISTA) ----------')
    # Sprawdzenie, czy utworzona lista jest pusta, przy pomocy metody is_empty()
    print(f'Czy lista jes pusta? {lista.is_empty()}\n\n')

    # Testowanie metody zwracającej pierwszy element
    print('---------- TESTOWANIE METODY GET ----------')
    print(f'Pierwszy element listy to : {lista.get()}\n\n')

    # Testowanie metody zliczającej liczbę elementów
    print('---------- TESTOWANIE METODY LENGTH ----------')
    print(f'Lista ma {lista.length()} elementów.\n\n')

    # Testowanie metody take()
    print('---------- TESTOWANIE METODY TAKE ----------')
    nowa_lista = lista.take(2)
    print('Ze starej listy została utworzona nowa, 2-elementowa: ')
    print(f'{nowa_lista}\n')

    nowa_lista = lista.take(10)
    print('Ze starej listy została utworzona nowa, parametr n większy od długości listy: ')
    print(f'{nowa_lista}\n\n')

    # Testowanie metody drop()
    print('---------- TESTOWANIE METODY DROP ----------')
    nowa_lista = lista.drop(3)
    print('Ze starej listy została utworzona nowa, 3-elementowa: ')
    print(f'{nowa_lista}\n')

    nowa_lista = lista.drop(10)
    print('Ze starej listy została utworzona nowa, parametr n większy od długości listy: ')
    print(f'{nowa_lista}\n\n')

    print('---------- TESTOWANIE METOD USUWANIA I NISZCZENIA ----------')
    # Usuwanie elementu z przodu
    lista.remove()
    print('Element z przodu został usunięty')
    print(f'{lista}\n')

    # Usuwanie elementu z tyłu
    lista.remove_end()
    print('Element z tyłu został usunięty')
    print(f'{lista}\n')

    # Zniszczenie listy
    lista.destroy()
    print('Lista została zniszczona')
    print(f'{lista}\n')
