import nodes


class Queue:
    """A class queue utiliza uma lista mas acede à lista utilizando o get e o add.
    É uma pilha com tamanho ilimitado. Ainda tem funções para retornar o número de elementos,
    da fila, de retornar como lista e a impressão de elemento a elemento
    da fila do topo à base, assumindo que o elemento tem uma função "print" própria."""
    def __init__(self):
        self._queue = []
    def add(self,elem:nodes.Node):
        self._queue.append(elem)

    def get(self) -> nodes.Node:
        return self._queue.pop(0)

    def get_sorted(self) -> nodes.Node:
        """
        Get Sorted
        Instead of returning the first element, it first sorts
        the queue, using function Lambda.
        Lambda is a functional element in Python programming.
        It consider value as a general value of the list to sort,
        and it calls that element when the sort function is executed.
        It is equal to say: Sort the list but get from each object inside
        the list, the value that I want to sort, that is, in this case, the total cost.
        """
        self._queue.sort(key= lambda value: value.get_total_cost())
        return self._queue.pop(0)

    def get_size(self):
        return len(self._queue)

    def empty(self) -> bool:
        if not self._queue:
            return True
        else:
            return False

    def get_list(self):
        return self._queue

    def print_queue(self,desc:str):
        print(desc,":")
        print("+last element+")
        for i in range(1,len(self._queue) + 1):
            self._queue[(-1)*i].print()
        print("+first element+")
