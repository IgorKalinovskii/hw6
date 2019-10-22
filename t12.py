import requests


base_url = 'http://pulse-rest-testing.herokuapp.com/'

data1 = {'title':'Происхождение видов', 'author':'Чарльз Дарвин'} #Создаём книгу POST /books/, вы запоминаете его id.
r_post = requests.post(base_url+'books/', data1)
print(r_post.json())
book_id = r_post.json()['id']

#Создаём роль вы запоминаете его id.
data2 = {'name':'Iron Man', 'type':'superhero', 'level': 100501, 'book': base_url + 'books/' + str(book_id)}
b_post = requests.post(base_url + 'roles/', data=data2)
id = b_post.json()['id']
print(b_post.status_code)
print(b_post.json())

#Проверяете, что _роль_ создалась и доступна по ссылке GET/роль/[id]
b_get = requests.get(base_url + 'roles/' + str(id))
print(b_get.status_code)
print(b_get.json()['name'] == 'Iron Man')
print(b_get.json()['type'] == 'superhero')
print(b_get.json()['level'] == 100501)
print(b_get.json()['book'] == base_url + 'books/' + str(book_id))

#Проверяете, что она есть в списке ролей по запросу GET /роли/
r_get_all_roles = requests.get(base_url+'roles')
print(b_post.json() in r_get_all_roles.json())



# import requests
#
#
# base_url = 'http://pulse-rest-testing.herokuapp.com/'
# data1 = {'title':'Происхождение видов', 'author':'Чарльз Дарвин'}
#
# r_post = requests.post(base_url+'books/', data1) #Создаём книгу POST /books/, вы запоминаете его id.
# id = r_post.json()['id']
# print(id)
#
# r_get = requests.get(base_url+'books/' + str(id) + '/') #Проверяете, что она создалась и доступна по ссылке GET/books/[id]
# print(r_post.json())
# print(r_post.json() == r_get.json())
# print(r_post.json()['title'] == 'Происхождение видов')
# print(r_post.json()['author'] == 'Чарльз Дарвин')
# print(r_get.json()['id'] == r_post.json()['id'])
#
# r_get_all_books = requests.get(base_url+'books/') #Проверяете, что она есть в списке книг по запросу GET /books/
# print(r_post.json() in r_get_all_books.json())
#
# put_data =  {'title':'Война миров', 'author':'Герберт Уэллс'}
# r_post1 = requests.put(base_url+'books/' + str(id) + '/', put_data)       #Изменяете данные этой книги методом PUT /books/[id]/
# print(r_post1.status_code)
#
# r_get1 = requests.get(base_url+'books/' + str(id) + '/') #Проверяете, что она изменилась и доступна по ссылке /books/[id]
# print(r_get1.status_code)
# print(r_get1.json())
# print(r_post1.json() == r_get1.json())
# print(r_get1.json()['title'] == 'Война миров')
# print(r_get1.json()['author'] == 'Герберт Уэллс')
# print(r_get1.json()['id'] == r_post1.json()['id'])
#
#
# r_get_all_books_2 = requests.get(base_url+'books/') # Проверяете, что она есть в списке книг по GET /books/ с новыми данными.
# print(r_post1.json() in r_get_all_books_2.json())
#
# r_delete = requests.delete(base_url+'books/' + str(id)) # Удаляете эту книгу методом DELETE /books/[id].
# r_get_deleted = requests.get(base_url + 'books/' + str(id) + '/')
# print(r_get_deleted.status_code)


