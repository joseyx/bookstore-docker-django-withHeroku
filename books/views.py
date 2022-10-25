"""books views"""
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from django.views import View
from django.db.models import Q

# pylint: disable=no-name-in-module
from .models import Book
from .forms import ReviewForm


# Create your views here.
class BookListView(ListView):
    """Book list view"""

    model = Book
    context_object = "book_list"
    template_name = "books/book_list.html"


class ReviewGet(DetailView):
    """Review get"""

    model = Book
    template_name = "books/book_detail.html"
    # pylint: disable=no-member
    queryset = Book.objects.all().prefetch_related(
        "reviews__author",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context


class ReviewPost(SingleObjectMixin, FormView):
    """review post"""

    model = Book
    form_class = ReviewForm
    template_name = "books/book_detail.html"

    def post(self, request, *args, **kwargs):
        # pylint: disable=attribute-defined-outside-init
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.book = self.object
        review.author = self.request.user
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        """get_success_url"""
        book = self.get_object()
        return reverse("book_detail", args=[str(book.id)])


class BookDetailView(View):
    """BookDetailView"""

    def get(self, request, *args, **kwargs):
        """get function"""
        view = ReviewGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """post function"""
        view = ReviewPost.as_view()
        return view(request, *args, **kwargs)


# class BookDetailView(DetailView):
#     """Book detail view"""

#     model = Book
#     context_object = "book"
#     templates_name = "books/book_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = ReviewForm()
#         return context


class SearchResultListView(ListView):
    """SearchResultListView"""

    model = Book
    context_object_name = "book_list"
    template_name = "books/search_result.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        # pylint: disable=no-member
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
