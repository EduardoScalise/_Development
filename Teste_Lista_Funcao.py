# Criando lista dentro de lisa
movie = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
         ["Graham Chapman",
          ["Michel Palin", "John Cleese", "Terry Gillia", "Eric Idle", "Terry Jones"]]]

print(movie)

#Criando função para exibir os dados das três listas
def print_lol (the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movie)