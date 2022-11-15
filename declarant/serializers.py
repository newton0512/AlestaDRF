from rest_framework import serializers
from .models import *


class DeclarantCarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeclarantCarrier
        fields = "__all__"


class ConsignorConsigneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsignorConsignee
        fields = "__all__"


class PIDeclarantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PIDeclarant
        fields = "__all__"


class CarrierRepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarrierRepresentative
        fields = "__all__"


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = "__all__"


class TreeTnvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeTnved
        fields = "__all__"


class TnvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tnved
        fields = "__all__"


class TranshipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transhipment
        fields = "__all__"


class TransportTranshipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportTranshipment
        fields = "__all__"


class ContainerTranshipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerTranshipment
        fields = "__all__"


class TransitGuaranteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransitGuarantee
        fields = "__all__"


class TransportXMLSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportXML
        fields = "__all__"


class ContainerXMLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerXML
        fields = "__all__"


class ConsignmentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsignmentItem
        fields = "__all__"


class ContainerCISerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerCI
        fields = "__all__"


class PIPrecedingDocDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PIPrecedingDocDetails
        fields = "__all__"


class PIGoodsDocDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PIGoodsDocDetails
        fields = "__all__"


class XMLModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = XMLModel
        fields = "__all__"
