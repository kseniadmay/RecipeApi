import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User

from .models import Category, Recipe, Ingredient, Step


class UserFactory(DjangoModelFactory):
    """Фабрика для создания пользователей"""

    class Meta:
        model = User
        skip_postgeneration_save = True  # Убирает warning от factory_boy при установке пароля

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'testpass123')


class CategoryFactory(DjangoModelFactory):
    """Фабрика для создания категорий"""

    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Категория {n}')
    slug = factory.Sequence(lambda n: f'category-{n}')


class RecipeFactory(DjangoModelFactory):
    """Фабрика для создания рецептов"""

    class Meta:
        model = Recipe

    title = factory.Sequence(lambda n: f'Рецепт {n}')
    description = factory.Faker('text', locale='ru_RU')
    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    cook_time = 30
    servings = 4
    difficulty = 'medium'


class IngredientFactory(DjangoModelFactory):
    """Фабрика для создания ингредиентов"""

    class Meta:
        model = Ingredient

    recipe = factory.SubFactory(RecipeFactory)
    name = factory.Faker('word', locale='ru_RU')
    amount = 100
    unit = 'г'


class StepFactory(DjangoModelFactory):
    """Фабрика для создания шагов"""

    class Meta:
        model = Step

    recipe = factory.SubFactory(RecipeFactory)
    order = factory.Sequence(lambda n: n + 1)
    description = factory.Faker('sentence', locale='ru_RU')
