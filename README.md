1.  add_product_to_recipe с параметрами recipe_id, product_id, weight. Функция добавляет к указанному рецепту указанный продукт с указанным весом. Если в рецепте уже есть такой продукт, то функция должна поменять его вес в этом рецепте на указанный.
  Пример запроса: http://127.0.0.1:8000/add_product_to_recipe/?recipe_id=3&product_id=3&weight=15

2. cook_recipe c параметром recipe_id. Функция увеличивает на единицу количество приготовленных блюд для каждого продукта, входящего в указанный рецепт.
  Пример запроса: http://127.0.0.1:8000/cook_recipe/?recipe_id=1

3. show_recipes_without_product с параметром product_id. Функция возвращает HTML страницу, на которой размещена таблица. В таблице отображены id и названия всех рецептов, в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм.
   Пример запроса: http://127.0.0.1:8000/show_recipes_without_product/?product_id=2 

Админка: http://127.0.0.1:8000/admin
