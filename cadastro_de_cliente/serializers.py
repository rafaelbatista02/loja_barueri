from rest_framework import serializers
from cadastro_de_cliente.models import Clientes


class ClientesSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=255)
    telefone = serializers.IntegerField()
    cpf = serializers.IntegerField()
    email = serializers.EmailField()
    nascimento = serializers.IntegerField()
    idade =  serializers.IntegerField()

    def create(self, validated_data):
        cleinte = Clientes.objects.create(**validated_data)
        return cleinte

    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.telefone = validated_data.get('telefone', instance.telefone)
        instance.cpf = validated_data.get('cpf', instance.cpf)
        instance.email = validated_data.get('email', instance.email)
        instance.nascimento = validated_data.get('nascimento', instance.nascimento)
        instance.idade = validated_data.get('idade',instance.idade)  
        
        instance.save()
        return instance