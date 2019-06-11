from django.shortcuts import render
from django.views import View



import logging
from django.views import generic
from .models import Goods
from .forms import GoodsSearchForm
from .forms import GoodsSearchForm2
from django.db.models import Q


class IndexView(generic.ListView):

    paginate_by = 5
    template_name = 'TP/index.html'
    model = Goods

    #def post()でセッションに検索フォームの値を渡す。
    def post(self, request, *args, **kwargs):

        form_value = [
            self.request.POST.get('goods_name', None),
            self.request.POST.get('price', None),
            self.request.POST.get('categ', None),
        ]
        request.session['form_value'] = form_value

        # 検索時にページネーションに関連したエラーを防ぐ
        self.request.GET = self.request.GET.copy()
        self.request.GET.clear()

        return self.get(request, *args, **kwargs)

    #def get_context_data()でセッションから検索フォームの値を取得して、検索フォームの初期値としてセットする。
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # sessionに値がある場合、その値をセットする。（ページングしてもform値が変わらないように）
        goods_name = ''
        price = ''
        categ = ''
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            goods_name = form_value[0]
            price = form_value[1]


        default_data = {'goods_name': goods_name,  # 商品名
                        'price': price,  # 価格
                        'categ': categ,  # カテゴリー
                        }

        test_form = GoodsSearchForm(initial=default_data) # 検索フォーム
        context['test_form'] = test_form

        #catadd_form =GoodsSearchForm2(initial=default_data) #プルダウン型検索フォーム
        #context['catadd_form'] = catadd_form

        return context

    #def get_queryset()でセッションから取得した検索フォームの値に応じてクエリ発行を行う。
    def get_queryset(self):

        # sessionに値がある場合、その値でクエリ発行する。
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            goods_name = form_value[0]
            price = form_value[1]

            # 検索条件
            condition_goods_name = Q()
            condition_price = Q()

            if len(goods_name) != 0 and goods_name[0]:
                condition_goods_name = Q(goods_name__contains=goods_name)
            if len(price) != 0 and price[0]:
                condition_price = Q(price__contains=price)

            return Goods.objects.select_related().filter(condition_goods_name & condition_price)
        else:
            # 何も返さない
            return Goods.objects.none()