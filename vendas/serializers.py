from rest_framework import serializers
from produtos.models import Produto
from produtos.serializers import ProdutoSerializer
from vendas.models import Venda
from decimal import Decimal

class ProdutoLigthSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)

class VendaSerializer(serializers.Serializer):
    produto = ProdutoLigthSerializer()
    desconto = serializers.IntegerField()
    valor_total = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True)
    forma_pagamento = serializers.ChoiceField(choices=Venda.formas_pagamento)

    def create(self, validated_data):
        produto_data = validated_data.pop('produto')
        produto = Produto.objects.get(id=produto_data['id'])
        desconto = validated_data.get('desconto')
        valor_total = Decimal(float(produto.valor) *(1- desconto / 100))

        venda = Venda.objects.create(
            produto=produto, 
            valor_total=valor_total, 
            **validated_data
            )
        return venda