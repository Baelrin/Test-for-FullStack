def find_article_position(articles, keyword):
    # Создаем словарь, где ключом является позиция артикула, а значением - сам артикул
    articles_dict = {i: article for i, article in enumerate(articles)}
    
    # Проверяем, есть ли ключевое слово в артикуле
    for position, article in articles_dict.items():
        if keyword in article:
            return position
            
    print("Ключевое слово не найдено в любом из артикулов.")
    return None
