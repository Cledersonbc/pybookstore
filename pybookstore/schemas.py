from pybookstore import ma
from pybookstore.models import Book


class BookSchema(ma.ModelSchema):
    class Meta:
        model = Book
