import requests


base_url = 'http://pulse-rest-testing.herokuapp.com/'

data1 = {'title':'Происхождение видов', 'author':'Чарльз Дарвин'} #Создаём книгу POST /books/, вы запоминаете его id.
b_post = requests.post(base_url+'books/', data1)
print(b_post.json())
book_id = b_post.json()['id']

#Создаём роль вы запоминаете его id.
data2 = {'name':'Iron Man', 'type':'superhero', 'level': 100501, 'book': base_url + 'books/' + str(book_id)}
r_post = requests.post(base_url + 'roles/', data=data2)
id = r_post.json()['id']
print(r_post.status_code)
print(r_post.json())

#Проверяете, что _роль_ создалась и доступна по ссылке GET/роль/[id]
r_get = requests.get(base_url + 'roles/' + str(id))
print(r_get.status_code)
print(r_get.json()['name'] == 'Iron Man')
print(r_get.json()['type'] == 'superhero')
print(r_get.json()['level'] == 100501)
print(r_get.json()['book'] == base_url + 'books/' + str(book_id))

#Проверяете, что она есть в списке ролей по запросу GET /роли/
r_get_all_roles = requests.get(base_url+'roles')
print(r_post.json() in r_get_all_roles.json())

#Изменяете данные этой роли методом PUT /books/[id]/
data3 = {'title':'Кобзар', 'author':'Тарас Шевченко'} #Создаём книгу POST /books/, вы запоминаете его id.
b1_post = requests.post(base_url+'books/', data=data3)
book1_id = b1_post.json()['id']
print(b1_post.json())

put_data = {'name':'Superman', 'type':'supersuperhero', 'level': 100502, 'book': base_url + 'books/' + str(book1_id)}
r_put = requests.put(base_url + 'roles/' + str(id), data= put_data)

print(r_put.json())

r_get_all_roles_2 = requests.get(base_url+'roles/') # Проверяете, что роль есть в списке книг по GET /roles/ с новыми данными.
print(r_put.json() in r_get_all_roles_2.json())

r_get_role2 = requests.get(base_url + 'roles/' + str(id))
print(r_get_role2.status_code)
print(r_get_role2.json()['name'] == 'Superman')
print(r_get_role2.json()['type'] == 'supersuperhero')
print(r_get_role2.json()['level'] == 100502)
print(r_get_role2.json()['book'] == base_url + 'books/' + str(book1_id))

#удаляем роль
r_delete = requests.delete(base_url + 'roles/' + str(id))
r_get_deleted_role = requests.get(base_url + 'roles/' + str(id))
print(r_get_deleted_role.status_code)

# #и удаляем книги
b1_delete=requests.delete(base_url + 'books/' + str(book_id))
b1_get_deleted = requests.get(base_url + 'books/' + str(book_id))
print(b1_delete.status_code)

b2_delete = requests.delete(base_url + 'books/' + str(book1_id))
b2_get_deleted = requests.get(base_url + 'books/' + str(book1_id))
print(b2_delete.status_code)




