# Создание пользователей

from django.contrib.auth.models import User

user=User.objects.create_user('User1', password='User1')
user=User.objects.create_user('User2', password='User2')
user.is_superuser=False
user.is_staff=False
user.save()

# Создать два объекта модели Author, связанные с пользователями

from News.models import *
User.objects.all()
u1 = User.objects.get(username='User1')
Author.objects.create(user=u1, rating='1')
u1.save()
u2 = User.objects.get(username='User2')
Author.objects.create(user=u2, rating='2')
u2.save()


# Добавить 4 категории в модель Category
from News.models import Category
category_1 = Category.objects.create(category_name='Спорт')
category_2 = Category.objects.create(category_name='Экономика')
category_3 = Category.objects.create(category_name='Политика')
category_4 = Category.objects.create(category_name='Культура')

# Добавить 2 статьи и 1 новость

from News.models import Post
post_news1 = Post.objects.create(author=Author.objects.get(pk=1), title='Президент СБР назвал сумму, которую выплатили биатлонистам по итогам сезона', text='Общий призовой фонд российскох соревнований в минувшем сезоне составил более 105 миллионов рублей', choice='news')
post_art1 = Post.objects.create(author=Author.objects.get(pk=1), title='Минэкономразвития оценило ВВП четырех новых регионов в 2 трлн рублей', text='Номинальный объем ВВП России с учетом присоединенных регионов в 2023 году составит 159 трлн рублей', choice='articles')
post_art2 = Post.objects.create(author=Author.objects.get(pk=2), title='Конституционный совет Франции признал пенсионную реформу законной', text='Конституционный совет Франции утвердил повышение пенсионного возраста до 64 лет', choice='articles')

# Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
PostCategory.objects.create(post=post_news1, category=Category.objects.get(category_name='Спорт'))
post_news1.category.add(category_1)
post_art1.category.add(category_2)
post_art2.category.add(category_3)

# Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).

from News.models import Comment

post_news1 = Post.objects.get(pk=4)
comment_1 = Comment.objects.create(comment_user=User.objects.get(pk=1), comment_post=post_news1, comment_text='Надо было заниматься спортом')
post_news1 = Post.objects.get(pk=5)
comment_2 = Comment.objects.create(comment_user=User.objects.get(pk=1), comment_post=post_news1, comment_text='интересно сколько получил каждый спортсмен')
post_art1 = Post.objects.get(pk=5)
comment_3 = Comment.objects.create(comment_user=User.objects.get(pk=1), comment_post=post_art1, comment_text='возвращаем наше)')
post_art2 = Post.objects.get(pk=6)
comment_4 = Comment.objects.create(comment_user=User.objects.get(pk=2), comment_post=post_art2, comment_text='ив европе тоже самое)')

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
post_news1.like()
post_news1.like()
post_news1.like()
post_art1.like()
post_art2.like()
comment_1.like()
comment_3.dislike()
comment_4.dislike()
post_art1.like()
post_art2.like()
post_art2.like()
post_news1.dislike()

#Обновить рейтинги пользователей.

author_1 = Author.objects.get(pk=1)
author_1.update_rating()

author_2 = Author.objects.get(pk=2)
author_2.update_rating()

# Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
Author.objects.all().order_by('-rating').values('user__username', 'rating').first()

# Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
