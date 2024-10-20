# TODO Найдите количество книг, которое можно разместить на дискете
disk=1.44 #Мб
pages=100
line=50
symbols=25
size_symbol=4 #байта
books=disk*1024*1024//(size_symbol*symbols*line*pages)
print("Количество книг, помещающихся на дискету:", round(books))
