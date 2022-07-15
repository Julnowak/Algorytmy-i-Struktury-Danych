# Skończone

class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


def nil():
    return []


def create():
    return nil()


def first(lst):
    return lst.data


def rest(lst):
    if lst:
        lst = lst.next
        return lst


def cons(el, lst):
    if not isinstance(el, Element):
        el = Element(el)
    el.next = lst
    lst = el
    return lst


def add_end(el, lst):
    if is_empty(lst):
        return cons(el, lst)
    else:
        first_el = first(lst)
        rest_lst = rest(lst)
        recreated_lst = add_end(el, rest_lst)
        return cons(first_el, recreated_lst)


def remove_end(lst):
    if is_empty(lst):
        raise Exception('Nie można usuwać z pustej listy')
    else:
        if is_empty(rest(lst)):
            return nil()
        else:
            first_el = first(lst)
            rest_lst = rest(lst)
            recreated_lst = remove_end(rest_lst)
            return cons(first_el, recreated_lst)


def destroy(lst):
    lst = nil()     # Nie jest to konieczne przypisanie
    return lst


def is_empty(lst):
    if lst:
        return False
    else:
        return True


def get(lst):
    return first(lst)


def add(elem, lst):
    return cons(elem, lst)


def remove(lst):
    return rest(lst)


def length(lst):
    if is_empty(lst):
        return 0
    else:
        lst = rest(lst)
        return 1 + length(lst)


def wypisz(lst, text="", count=0):
    if lst:
        if count == 3:
            text += '\n'
        text += '(' + str(first(lst)[0]) + ', ' + str(first(lst)[1]) + ', ' + str(first(lst)[2]) + ') -> '
        first(lst)
        lst = rest(lst)
        count += 1
        wypisz(lst, text, count)
    else:
        text += 'None'
        print(text)


def take(n, lst, new_head=None):
    if isinstance(n, int) and n >= 0:
        if new_head is None:
            new_head = create()

        if n >= length(lst):
            n = length(lst)

        if n != 0:
            elem = first(lst)
            new_head = add_end(elem, new_head)
            lst = rest(lst)
            n -= 1
            return take(n, lst, new_head)
        else:
            return new_head
    else:
        raise Exception('Wpisano niepoprawną wartość n')


def drop(n, lst, new_head=None):
    if isinstance(n, int) and n >= 0:
        if new_head is None:
            new_head = create()

        if n >= length(lst):
            return new_head

        if n != 0:
            lst = rest(lst)
            n -= 1
            return drop(n, lst, new_head)
        else:
            if lst:
                elem = first(lst)
                new_head = add_end(elem, new_head)
                lst = rest(lst)
                return drop(n, lst, new_head)
            else:
                return new_head
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
    head = create()

    # Sprawdzenie, czy utworzona lista jest pusta, przy pomocy metody is_empty()
    print('---------- TESTOWANIE METODY IS_EMPTY (PUSTA LISTA) ----------')
    print(f'Czy lista jes pusta? {is_empty(head)}\n\n')

    print('---------- TESTOWANIE METOD DODAWANIA ----------')
    # Ustawienie pierwszego elementu (głowy)

    head = add(elem_list[2], head)
    print('Dodano głowę listy wiązanej jednokierunkowej')
    wypisz(head)
    print('\n')

    # Dodanie elementów z tyłu listy
    head = add_end(elem_list[3], head)
    print('Dodano element z tyłu listy')
    wypisz(head)
    print('\n')

    head = add_end(elem_list[4], head)
    print('Dodano element z tyłu listy')
    wypisz(head)
    print('\n')

    head = add_end(elem_list[5], head)
    print('Dodano element z tyłu listy')
    wypisz(head)
    print('\n')

    # Dodanie elementów z przodu listy
    head = add(elem_list[1], head)
    print('Dodano element z przodu listy')
    wypisz(head)
    print('\n')

    head = add(elem_list[0], head)
    print('Dodano element z przodu listy')
    wypisz(head)
    print('\n')

    print('---------- TESTOWANIE METODY IS_EMPTY (NIEPUSTA LISTA) ----------')
    # Sprawdzenie, czy utworzona lista jest pusta, przy pomocy metody is_empty()
    print(f'Czy lista jes pusta? {is_empty(head)}\n\n')

    # Testowanie metody zwracającej pierwszy element
    print('---------- TESTOWANIE METODY GET ----------')
    print(f'Pierwszy element listy to : {get(head)}\n\n')

    # Testowanie metody zliczającej liczbę elementów
    print('---------- TESTOWANIE METODY LENGTH ----------')
    print(f'Lista ma {length(head)} elementów.\n\n')

    # Testowanie metody take()
    print('---------- TESTOWANIE METODY TAKE ----------')
    nowa_lista = take(2, head)
    print('Ze starej listy została utworzona nowa, 2-elementowa: ')
    wypisz(nowa_lista)
    print('\n')

    nowa_lista = take(10, head)
    print('Ze starej listy została utworzona nowa, parametr n większy od długości listy: ')
    wypisz(nowa_lista)
    print('\n')

    # Testowanie metody drop()
    print('---------- TESTOWANIE METODY DROP ----------')
    nowa_lista = drop(3, head)
    print('Ze starej listy została utworzona nowa, 3-elementowa: ')
    wypisz(nowa_lista)
    print('\n')

    nowa_lista = drop(10, head)
    print('Ze starej listy została utworzona nowa, parametr n większy od długości listy: ')
    wypisz(nowa_lista)
    print('\n')

    print('---------- TESTOWANIE METOD USUWANIA I NISZCZENIA ----------')
    # Usuwanie elementu z przodu
    head = remove(head)
    print('Element z przodu został usunięty')
    wypisz(head)
    print('\n')

    # Usuwanie elementu z tyłu
    head = remove_end(head)
    print('Element z tyłu został usunięty')
    wypisz(head)
    print('\n')

    # Zniszczenie listy
    head = destroy(head)
    print('Lista została zniszczona')
    wypisz(head)
