from django import forms

class GoodsSearchForm(forms.Form):
    goods_name = forms.CharField(
        initial='',
        label='商品名',
        required = False, # 必須ではない
    )
    price = forms.IntegerField(
        initial='',
        label='価格',
        required=False,  # 必須ではない
    )
    categ = forms.CharField(
        initial = '',
        label='カテゴリー',
        required = False,
    )


class GoodsSearchForm2(forms.Form):
    goods_name = forms.CharField(
        initial='',
        label='商品名',
        required = False, # 必須ではない
    )
    price = forms.IntegerField(
        initial='',
        label='価格',
        required=False,  # 必須ではない
    )
    categ = forms.ChoiceField(
        label='カテゴリー',
        required = True,
        disabled=False,
        widget=forms.Select(attrs={
            'id': 'categ',})
    )
