# TODO Напишите функцию для поиска индекса товара
def find_item_index(items, item): #items — это список товаров, item — это товар, который мы ищем
    for i, value in enumerate(items):
        if value == item:  #Если текущий товар равен тому, который мы ищем, то возвращаем индекс этого товара
            return i
    return None #Если мы прошли весь список и ничего не нашли - верни None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item) # где в списке items_list находится товар find_item, TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
