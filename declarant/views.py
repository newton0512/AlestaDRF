from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

import declarant.update_tnved as lib
from declarant.models import *
from declarant.serializers import *

from django.contrib.auth import login

from rest_framework import permissions


class DeclarantTreeTnvedUpdate(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        return Response(lib.update_tnved())


# декларант, перевозчик и перевозчик по ТТ ЕАЭС
class DeclarantCarrierAPI(viewsets.ModelViewSet):
    queryset = DeclarantCarrier.objects.all()
    serializer_class = DeclarantCarrierSerializer
    permission_classes = (IsAuthenticated,)


# отправитель, получатель
class ConsignorConsigneeAPI(viewsets.ModelViewSet):
    queryset = ConsignorConsignee.objects.all()
    serializer_class = ConsignorConsigneeSerializer
    permission_classes = (IsAuthenticated,)


# Лицо, предоставившее ПИ
class PIDeclarantAPI(viewsets.ModelViewSet):
    queryset = PIDeclarant.objects.all()
    serializer_class = PIDeclarantSerializer
    permission_classes = (IsAuthenticated,)


# водитель
class CarrierRepresentativeAPI(viewsets.ModelViewSet):
    queryset = CarrierRepresentative.objects.all()
    serializer_class = CarrierRepresentativeSerializer
    permission_classes = (IsAuthenticated,)


# транспортные средства (список)
class TransportAPI(viewsets.ModelViewSet):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = (IsAuthenticated,)


# дерево кодов
class TreeTnvedAPI(viewsets.ReadOnlyModelViewSet):
    queryset = TreeTnved.objects.all()
    serializer_class = TreeTnvedSerializer
    permission_classes = (IsAuthenticated,)


# коды ТН ВЭД и тарифы
class TnvedAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Tnved.objects.all()
    serializer_class = TnvedSerializer
    permission_classes = (IsAuthenticated,)


# ****************************
# основная инфа по XML
class XMLModelAPI(viewsets.ModelViewSet):
    queryset = XMLModel.objects.all()
    serializer_class = XMLModelSerializer
    permission_classes = (IsAuthenticated,)


# перецепки
class TranshipmentAPI(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Transhipment.objects.all()
    serializer_class = TranshipmentSerializer
    permission_classes = (IsAuthenticated,)


# транспорт в перецепке
class TransportTranshipmentAPI(mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    queryset = TransportTranshipment.objects.all()
    serializer_class = TransportTranshipmentSerializer
    permission_classes = (IsAuthenticated,)


# контейнеры в перецепке
class ContainerTranshipmentAPI(mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    queryset = ContainerTranshipment.objects.all()
    serializer_class = ContainerTranshipmentSerializer
    permission_classes = (IsAuthenticated,)


# гаранты в XML
class TransitGuaranteeAPI(mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    queryset = TransitGuarantee.objects.all()
    serializer_class = TransitGuaranteeSerializer
    permission_classes = (IsAuthenticated,)


# транспорт в XML
class TransportXMLAPI(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = TransportXML.objects.all()
    serializer_class = TransportXMLSerializer
    permission_classes = (IsAuthenticated,)


# контейнеры в XML
class ContainerXMLAPI(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = ContainerXML.objects.all()
    serializer_class = ContainerXMLSerializer
    permission_classes = (IsAuthenticated,)


# товары в XML
class ConsignmentItemAPI(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         viewsets.GenericViewSet):
    queryset = ConsignmentItem.objects.all()
    serializer_class = ConsignmentItemSerializer
    permission_classes = (IsAuthenticated,)


# контейнеры в товаре
class ContainerCIAPI(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = ContainerCI.objects.all()
    serializer_class = ContainerCISerializer
    permission_classes = (IsAuthenticated,)


# предшедствующие документы
class PIPrecedingDocDetailsAPI(mixins.CreateModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    queryset = PIPrecedingDocDetails.objects.all()
    serializer_class = PIPrecedingDocDetailsSerializer
    permission_classes = (IsAuthenticated,)


# документы в товаре
class PIGoodsDocDetailsAPI(mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    queryset = PIGoodsDocDetails.objects.all()
    serializer_class = PIGoodsDocDetailsSerializer
    permission_classes = (IsAuthenticated,)
