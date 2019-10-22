import requests


base_url = 'http://pulse-rest-testing.herokuapp.com/'
data1 = {'title':'Происхождение видов', 'author':'Чарльз Дарвин'}

r_post = requests.post(base_url+'books/', data1) #Создаём книгу POST /books/, вы запоминаете его id.
id = r_post.json()['id']
print(r_post.json())
print(id)

r_get = requests.get(base_url+'books/' + str(id) + '/') #Проверяете, что она создалась и доступна по ссылке GET/books/[id]
print(r_get.json())
print(r_post.json() == r_get.json())

r_get_all_books = requests.get(base_url+'books/') #Проверяете, что она есть в списке книг по запросу GET /books/
print(r_post.json() in r_get_all_books.json())

put_data =  {'title':'Война миров', 'author':'Герберт Уэллс'}
r_post1 = requests.put(base_url+'books/' + str(id) + '/', put_data)       #Изменяете данные этой книги методом PUT /books/[id]/
print(r_post1.status_code)

r_get1 = requests.get(base_url+'books/' + str(id) + '/') #Проверяете, что она изменилась и доступна по ссылке /books/[id]
print(r_post1.json() == r_get1.json())

r_get_all_books_2 = requests.get(base_url+'books/') # Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
print(r_post1.json() in r_get_all_books_2.json())

r_delete = requests.delete(base_url+'books/' + str(id)) # Удаляете эту книгу методом DELETE /books/[id].
r_get_deleted = requests.get(base_url + 'books/' + str(id) + '/')
print(r_get_deleted.status_code)

