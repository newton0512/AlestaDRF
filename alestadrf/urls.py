"""alestadrf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view

from declarant.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


router = routers.DefaultRouter()
router.register(r'declarant_carrier', DeclarantCarrierAPI, basename='declarant_carrier')
router.register(r'consignor_consignee', ConsignorConsigneeAPI, basename='consignor_consignee')
router.register(r'pideclarant', PIDeclarantAPI, basename='pideclarant')
router.register(r'carrier_representative', CarrierRepresentativeAPI, basename='carrier_representative')
router.register(r'transport', TransportAPI, basename='transport')
router.register(r'tree_tnved', TreeTnvedAPI, basename='tree_tnved')
router.register(r'tnved', TnvedAPI, basename='tnved')

# маршруты по XML
xml_router = routers.DefaultRouter()
xml_router.register(r'xml_info', XMLModelAPI, basename='xml_info')
xml_router.register(r'transhipment', TranshipmentAPI, basename='transhipment')
xml_router.register(r'transport_transhipment', TransportTranshipmentAPI, basename='transport_transhipment')
xml_router.register(r'container_transhipment', ContainerTranshipmentAPI, basename='container_transhipment')
xml_router.register(r'transit_guarantee', TransitGuaranteeAPI, basename='transit_guarantee')
xml_router.register(r'transport_xml', TransportXMLAPI, basename='transport_xml')
xml_router.register(r'container_xml', ContainerXMLAPI, basename='container_xml')
xml_router.register(r'consignment_item', ConsignmentItemAPI, basename='consignment_item')
xml_router.register(r'container_ci', ContainerCIAPI, basename='container_ci')
xml_router.register(r'preceding_doc', PIPrecedingDocDetailsAPI, basename='preceding_doc')
xml_router.register(r'goods_doc', PIGoodsDocDetailsAPI, basename='goods_doc')

schema_view = get_swagger_view(title='AlestaDRF API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/treeupdate', DeclarantTreeTnvedUpdate.as_view()),
    path('api/v1/', include(router.urls)),
    path('api/v1/xml', include(xml_router.urls)),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path(r'api/docs/', schema_view),

]
