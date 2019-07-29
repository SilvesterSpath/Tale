import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
for i in bookshelf:
  print(i)
  
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_lenght(book_a, book_b):
  return book_a['title'] + book_a['author'] > book_b['title'] + book_b['author']

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
for i in sort_1:
  print(i['title'])
  
bookshelf_v1 = bookshelf[:]
bookshelf_v2 = bookshelf[:]

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
for i in sort_2:
  print(i['author'])  

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2)-1, by_author_ascending)

for i in bookshelf_v2:
  print(i['author'])
  
long_bookshelf = utils.load_books("books_large.csv")

#sort_3 = sorts.bubble_sort(long_bookshelf, by_total_lenght)
#for i in sort_3:
#  print(i)

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) -1, by_total_lenght)
for i in long_bookshelf:
  print(i)
  

