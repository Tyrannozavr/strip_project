# Для запуска проекта
### git clone https://github.com/Tyrannozavr/strip_project
###  cd strip_project/
### sudo chmod +x scrypt.sh
### docker-compose up
## теперь проект доступен по адресу: http://0.0.0.0:8000/
на первой странице для удобста я вывел все продукты списком со ссылками на требуемые в задании страницы
также на ней есть ссылка на админку и на страницу orders которая была как дополнительное задание
в админке можно создать несколько orders и создать / добавить к orders discounts
все они создаются и удаляются напрямую из админки без необходимости посещать сайт
набор параметров пока ограничен, решил не загромождать админку кучей параметров доступных на сайте

## для тестирования создан суперпользователь - login: dmiv password: 123456
для тестирования оплаты можно использовать карту: 
номер - 4242 4242 4242 4242, cvc код любой, срок действия любой не меньше текущего месяца