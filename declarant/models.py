from django.db import models


#######################################################################
# модели, для хранения основных данных в БД и подстановки в XML
#######################################################################

# декларант, перевозчик и перевозчик по ТТ ЕАЭС
class DeclarantCarrier(models.Model):
    SubjectBriefName = models.CharField(max_length=120, blank=False)
    TaxpayerId = models.CharField(max_length=20, blank=True)
    UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    RegionName = models.CharField(max_length=120, blank=True)
    CityName = models.CharField(max_length=120, blank=False)
    StreetName = models.CharField(max_length=120, blank=False)
    BuildingNumberId = models.CharField(max_length=50, blank=True)
    RoomNumberId = models.CharField(max_length=20, blank=True)


# отправитель, получатель
class ConsignorConsignee(models.Model):
    SubjectBriefName = models.CharField(max_length=120, blank=False)
    TaxpayerId = models.CharField(max_length=20, blank=True)
    UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    RegionName = models.CharField(max_length=120, blank=True)
    CityName = models.CharField(max_length=120, blank=False)
    StreetName = models.CharField(max_length=120, blank=False)
    BuildingNumberId = models.CharField(max_length=50, blank=True)
    RoomNumberId = models.CharField(max_length=20, blank=True)


# Лицо, предоставившее ПИ
class PIDeclarant(models.Model):
    SubjectBriefName = models.CharField(max_length=120, blank=False)
    TaxpayerId = models.CharField(max_length=20, blank=False)
    UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    RegionName = models.CharField(max_length=120, blank=True)
    CityName = models.CharField(max_length=120, blank=False)
    StreetName = models.CharField(max_length=120, blank=False)
    BuildingNumberId = models.CharField(max_length=50, blank=True)
    RoomNumberId = models.CharField(max_length=20, blank=True)
    RegistrationNumberId = models.CharField(max_length=50, blank=False)


# водитель
class CarrierRepresentative(models.Model):
    FirstName = models.CharField(max_length=120, blank=False)
    MiddleName = models.CharField(max_length=120, blank=True)
    LastName = models.CharField(max_length=120, blank=False)
    PositionName = models.CharField(max_length=120, default='ВОДИТЕЛЬ')
    UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    IdentityDocKindCode = models.CharField(max_length=7, blank=False)
    DocId = models.CharField(max_length=50, blank=False)
    DocCreationDate = models.DateField(blank=False)
    DocValidityDate = models.DateField(blank=True, null=True)


# транспортные средства
class Transport(models.Model):
    TransportMeansRegId = models.CharField(max_length=40, blank=False)
    countryCode = models.CharField(max_length=2, blank=False)
    VehicleId = models.CharField(max_length=40, blank=False)
    TransportTypeCode = models.CharField(max_length=3, blank=False)
    VehicleMakeCode = models.CharField(max_length=3, blank=False)
    VehicleMakeName = models.CharField(max_length=25, blank=False)
    VehicleModelName = models.CharField(max_length=250, blank=True)
    Carrier = models.ForeignKey(DeclarantCarrier, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('TransportMeansRegId', 'Carrier')


class TreeTnved(models.Model):
    #ParentID - ссылка на родительский элемент дерева или null для корневых элементов.
    ParentID = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    # Name - наименование элемента дерева
    Name = models.CharField(max_length=1000, blank=False)

    # Code - форматированный код элемента дерева (может отсутствовать!)
    Code = models.CharField(max_length=13, null=True)

    # DateFrom - дата начала действия элемента, если она установлена. YYYY-MM-DD.
    DateFrom = models.DateTimeField(null=True)

    # DateTo - дата завершения действия элемента, если она установлена. YYYY-MM-DD.
    DateTo = models.DateTimeField(null=True)


# коды ТН ВЭД и тарифы
class Tnved(models.Model):
    TreeID = models.ForeignKey(TreeTnved, on_delete=models.CASCADE)
    Name = models.CharField(max_length=1000, blank=False)    # "чистопородные племенные животные: 🡺 коровы",
    Code = models.CharField(max_length=13, blank=False)     # "0102 21 300 0",

    # текстовое представление таможенного тарифа, действующего на дату запроса.
    # Например "5%", "15%, но не менее 0,15 EUR за 1кг", "8,2% плюс 0,4 EUR за 1 шт" и т.п.
    TariffText = models.CharField(max_length=50, blank=False)

    # адвалорная ставка действующего таможенного тарифа в процентах.
    # Если адвалорная ставка не установлена, поле отсутствует
    TariffAdvalor = models.FloatField(null=True, blank=True)

    # специфическая ставка действующего таможенного тарифа в единицах валюты.
    # Если специфическая ставка не установлена, поле отсутствует
    TariffSpecific = models.FloatField(null=True, blank=True)

    # валюта, в которой указана ставка действующего таможенного тарифа, текстовый трёхбуквенный код.
    # Например, "EUR", "USD" и т.п.
    # Если специфическая ставка не установлена, поле отсутствует.
    TariffSpecificCurrency = models.CharField(max_length=3, null=True, blank=True)

    # Количество единиц измерения, за которое установлена специфическая
    # ставка действующего таможенного тарифа.
    # Если специфическая ставка не установлена, поле отсутствует
    TariffSpecificMeasureAmount = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)

    # Единица измерения, за которую установлена специфическая ставка действующего
    # таможенного тарифа, краткое наименование. Например "кг", "шт" и т.п.
    # Если специфическая ставка не установлена, поле отсутствует
    TariffSpecificMeasureUnit = models.CharField(null=True, max_length=20, blank=True)

    # Признак сложения адвалорной и специфической ставок действующего таможенного тарифа.
    # Если заданы обе ставки и это поле установлено в "1", то тариф сформулирован
    # в виде "X% плюс Y [валюта] за Z [единица измерения]". Если заданы обе ставки и это поле отсутствует,
    # то тариф сформулирован в виде "X%, но не менее Y [валюта] за Z [единица измерения]".
    TariffSpecificAddedToAdvalor = models.CharField(null=True, max_length=1, blank=True)

    # Дополнительная единица измерения, краткое наименование. Например "кг", "шт" и т.п.
    # Если дополнительная единица к коду ТНВЭД не установлена, поле отсутствует
    AdditionalMeasureUnit =  models.CharField(null=True, max_length=20, blank=True)

    # Признак наличия (1 = да) действующих антидемпинговых пошлин для кода ТНВЭД.
    # Для более подробной информации можно выполнить запрос R12.
    # Если антидемпинговые пошлины к коду ТНВЭД не добавлены, поле отсутствует.
    Ad = models.CharField(null=True, max_length=1, blank=True)

    # Признак наличия (1 = да) действующих специальных тарифов для кода ТНВЭД.
    # Для более подробной информации можно выполнить запрос R12.
    # Если специальные тарифы к коду ТНВЭД не добавлены, поле отсутствует.
    Sp = models.CharField(null=True, max_length=1, blank=True)

    # Признак наличия (1 = да) действующих в Республике Беларусь акцизов для кода ТНВЭД.
    # Для более подробной информации можно выполнить запрос R12.
    # Если акцизы к коду ТНВЭД не добавлены, поле отсутствует.
    Ex = models.CharField(null=True, max_length=1, blank=True)

    # Признак наличия (1 = да) действующих в Республике Беларусь записей таможенного реестра
    # интеллектуальной собственности для кода ТНВЭД. Для более подробной информации выполнить запрос R12.
    # Если записей таможенного реестра интеллектуальной собственности к коду ТНВЭД не добавлены, поле отсутствует
    Ip = models.CharField(null=True, max_length=1, blank=True)

    # действующая ставка сбора за таможенное оформление
    F = models.DecimalField(null=True, blank=True, max_digits=8, decimal_places=2)

    # Дата начала действия кода ТНВЭД, если она установлена. YYYY-MM-DD.
    DateFrom = models.DateField(null=True)

    # Дата завершения действия кода ТНВЭД, если она установлена. YYYY-MM-DD.
    DateTo = models.DateField(null=True)

#######################################################################
# модели, непосредственно относящиеся к формированию XML
#######################################################################

# перецепки
class Transhipment(models.Model):
    CargoOperationKindCode = models.CharField(max_length=1, blank=False)
    ContainerIndicator = models.CharField(max_length=1, blank=False)
    CACountryCode = models.CharField(max_length=2, blank=False)
    ShortCountryName = models.CharField(max_length=40, blank=False)
    PlaceName = models.CharField(max_length=120, blank=True)
    CustomsOfficeCode = models.CharField(max_length=43, blank=True)
    UnifiedTransportModeCode = models.CharField(max_length=2, blank=False)
    RegistrationNationalityCode = models.CharField(max_length=2, blank=False)
    TransportMeansQuantity = models.IntegerField(blank=False)
    # внешний ключ
    xml = models.ForeignKey('XMLModel', on_delete=models.CASCADE)


# транспорт в перецепке
class TransportTranshipment(models.Model):
    TransportMeansRegId = models.CharField(max_length=40, blank=False)
    countryCode = models.CharField(max_length=2, blank=False)
    TransportTypeCode = models.CharField(max_length=3, blank=False)
    # внешний ключ
    transhipment_xml = models.ForeignKey(Transhipment, models.CASCADE)


# контейнеры в перецепке
class ContainerTranshipment(models.Model):
    ContainerId = models.CharField(max_length=17, blank=False)
    # внешний ключ
    transhipment_xml = models.ForeignKey(Transhipment, models.CASCADE)


# гаранты в XML
class TransitGuarantee(models.Model):
    TransitGuaranteeMeasureCode = models.CharField(max_length=2, blank=False)
    GuaranteeAmount = models.DecimalField(blank=True, null=True, max_digits=11, decimal_places=1)
    currencyCode = models.CharField(max_length=3, blank=True, default='BYN')
    # секция для номера сертификата
    GC_CustomsOfficeCode = models.CharField(max_length=8, blank=True)
    GC_DocCreationDate = models.DateField(blank=True, null=True)
    GC_CustomsDocumentId = models.CharField(max_length=10, blank=True)
    # секция для подтверждающего документа
    RD_UnifiedCountryCode = models.CharField(max_length=2, blank=True)
    RD_RegistrationNumberId = models.CharField(max_length=50, blank=True)
    # секция для таможенного сопровождения
    ES_SubjectBriefName = models.CharField(max_length=120, blank=True)
    ES_TaxpayerId = models.CharField(max_length=20, blank=True)
    ES_BankId = models.CharField(max_length=9, blank=True)
    # внешний ключ
    xml = models.ForeignKey('XMLModel', on_delete=models.CASCADE)


# транспорт в XML
class TransportXML(models.Model):
    TransportMeansRegId = models.CharField(max_length=40, blank=False)
    countryCode = models.CharField(max_length=2, blank=False)
    VehicleId = models.CharField(max_length=40, blank=False)
    TransportTypeCode = models.CharField(max_length=3, blank=False)
    VehicleMakeCode = models.CharField(max_length=3, blank=False)
    VehicleMakeName = models.CharField(max_length=25, blank=False)
    VehicleModelName = models.CharField(max_length=250, blank=True)
    # внешний ключ
    xml = models.ForeignKey('XMLModel', on_delete=models.CASCADE)


# контейнеры в XML
class ContainerXML(models.Model):
    ContainerId = models.CharField(max_length=17, blank=False)
    # внешний ключ
    xml = models.ForeignKey('XMLModel', on_delete=models.CASCADE)


# товары в XML
class ConsignmentItem(models.Model):
    ConsignmentItemOrdinal = models.PositiveIntegerField(blank=False)
    CommodityCode = models.CharField(max_length=10, blank=True)
    GoodsDescriptionText = models.CharField(max_length=250, blank=True)
    GoodsDescriptionText1 = models.CharField(max_length=250, blank=True)
    GoodsDescriptionText2 = models.CharField(max_length=250, blank=True)
    GoodsDescriptionText3 = models.CharField(max_length=250, blank=True)
    UnifiedGrossMassMeasure = models.DecimalField(blank=True, null=True, max_digits=17, decimal_places=6)
    measurementUnitCode = models.CharField(max_length=3, blank=True, default='166')
    # GoodsMeasureDetails
    GM_GoodsMeasure = models.DecimalField(blank=True, null=True, max_digits=17, decimal_places=6)
    GM_measurementUnitCode = models.CharField(max_length=3, blank=True)
    GM_MeasureUnitAbbreviationCode = models.CharField(max_length=20, blank=True)
    # AddGoodsMeasureDetails
    AGM_GoodsMeasure = models.DecimalField(blank=True, null=True, max_digits=17, decimal_places=6)
    AGM_measurementUnitCode = models.CharField(max_length=3, blank=True)
    AGM_MeasureUnitAbbreviationCode = models.CharField(max_length=20, blank=True)
    # CargoPackagePalletDetails
    PackageAvailabilityCode = models.CharField(max_length=1, blank=False)
    CargoQuantity = models.PositiveIntegerField(blank=False)
    PackageKindCode = models.CharField(max_length=2, blank=False)
    PackageQuantity = models.PositiveIntegerField(blank=False)
    # стоимость
    CAValueAmount = models.DecimalField(blank=True, null=True, max_digits=17, decimal_places=2)
    currencyCode = models.CharField(max_length=3, blank=True)
    # внешний ключ
    xml = models.ForeignKey('XMLModel', on_delete=models.CASCADE)

# контейнеры в товаре
class ContainerCI(models.Model):
    ContainerId = models.CharField(max_length=17, blank=False)
    # внешний ключ на товар
    ci = models.ForeignKey(ConsignmentItem, on_delete=models.CASCADE)


# предшедствующие документы
class PIPrecedingDocDetails(models.Model):
    DocKindCode = models.CharField(max_length=5, blank=False)
    DocId = models.CharField(max_length=50, blank=False)
    DocCreationDate = models.DateField(blank=False)
    # внешний ключ на товар
    ci = models.ForeignKey(ConsignmentItem, on_delete=models.CASCADE)

# документы в товаре
class PIGoodsDocDetails(models.Model):
    DocKindCode = models.CharField(max_length=5, blank=False)
    DocId = models.CharField(max_length=50, blank=False)
    DocCreationDate = models.DateField(blank=False)
    # внешний ключ на товар
    ci = models.ForeignKey(ConsignmentItem, on_delete=models.CASCADE)


# основная информация в XML
class XMLModel(models.Model):
    EDocCode = models.CharField(max_length=10, default='R.042')
    EDocId = models.CharField(max_length=36, blank=False)
    EDocDateTime = models.DateTimeField(auto_now_add=True)
    EDocIndicatorCode = models.CharField(max_length=2, blank=False)
    PreliminaryInformationUsageCode1 = models.CharField(max_length=2, blank=False)
    PreliminaryInformationUsageCode2 = models.CharField(max_length=2, blank=False)
    PreliminaryInformationUsageCode3 = models.CharField(max_length=2, blank=False)

    # PIATEntryCheckPointDetails
    ECP_CustomsOfficeCode = models.CharField(max_length=8, blank=False)
    ECP_BorderCheckpointName = models.CharField(max_length=50, blank=False)

    # PIDeclarantDetails
    PIDeclarant_SubjectBriefName = models.CharField(max_length=120, blank=False)
    PIDeclarant_TaxpayerId = models.CharField(max_length=20, blank=False)
    PIDeclarant_UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    PIDeclarant_RegionName = models.CharField(max_length=120, blank=True)
    PIDeclarant_CityName = models.CharField(max_length=120, blank=False)
    PIDeclarant_StreetName = models.CharField(max_length=120, blank=False)
    PIDeclarant_BuildingNumberId = models.CharField(max_length=50, blank=True)
    PIDeclarant_RoomNumberId = models.CharField(max_length=20, blank=True)
    PIDeclarant_RegistrationNumberId = models.CharField(max_length=50, blank=False)

    # PIATBorderTransportDetails и PITransitTransportMeansDetails
    UnifiedTransportModeCode = models.CharField(max_length=2, blank=False)
    TransportMeansQuantity = models.PositiveSmallIntegerField(blank=False)
    ContainerIndicator = models.CharField(max_length=1, default='0')
    Transport_EqualIndicator = models.CharField(max_length=1, default='1')

    # TIRCarnetIdDetails
    TIRCarnetIndicator = models.CharField(max_length=1, blank=False)
    TIRSeriesId = models.CharField(max_length=2, blank=True)
    TIRId = models.CharField(max_length=8, blank=True)
    TIRPageOrdinal = models.PositiveSmallIntegerField(blank=True)
    TIRHolderId = models.CharField(max_length=18, blank=True)

    DeclarationKindCode = models.CharField(max_length=10, blank=False)
    TransitProcedureCode = models.CharField(max_length=10, blank=False)
    TransitFeatureCode = models.CharField(max_length=10, blank=True)

    LoadingListsQuantity = models.PositiveIntegerField(blank=False)
    LoadingListsPageQuantity = models.PositiveIntegerField(blank=False)
    GoodsQuantity = models.PositiveIntegerField(blank=False)
    CargoQuantity = models.PositiveIntegerField(blank=False)
    SealQuantity = models.PositiveIntegerField(blank=True)
    SealId = models.CharField(max_length=120, blank=True)

    # TransitTerminationDetails
    TT_CustomsOfficeCode = models.CharField(max_length=8, blank=False)
    TT_CustomsOfficeName = models.CharField(max_length=50, blank=False)
    TT_CustomsControlZoneId = models.CharField(max_length=50, blank=False)

    # PIATTransportDocumentDetails
    TD_DocKindCode = models.CharField(max_length=5, blank=False)
    TD_DocId = models.CharField(max_length=50, blank=False)
    TD_DocCreationDate = models.DateField(blank=False)

    # DepartureCountryDetails
    DepartureCountry_CACountryCode = models.CharField(max_length=2, blank=False)
    DepartureCountry_ShortCountryName = models.CharField(max_length=40, blank=False)

    # DestinationCountryDetails
    DestinationCountry_CACountryCode = models.CharField(max_length=2, blank=False)
    DestinationCountry_ShortCountryName = models.CharField(max_length=40, blank=False)

    CAInvoiceValueAmount = models.DecimalField(blank=False, default=0, max_digits=17, decimal_places=2)
    IVA_currencyCode = models.CharField(max_length=3, blank=False, default='EUR')
    UnifiedGrossMassMeasure = models.DecimalField(blank=False, default=0, max_digits=17, decimal_places=6)
    measurementUnitCode = models.CharField(max_length=3, blank=False, default='166')

    # ОТПРАВИТЕЛЬ
    # PIATConsignorDetails
    Consignor_SubjectBriefName = models.CharField(max_length=120, blank=False)
    Consignor_TaxpayerId = models.CharField(max_length=20, blank=True)
    Consignor_UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    Consignor_RegionName = models.CharField(max_length=120, blank=True)
    Consignor_CityName = models.CharField(max_length=120, blank=False)
    Consignor_StreetName = models.CharField(max_length=120, blank=False)
    Consignor_BuildingNumberId = models.CharField(max_length=50, blank=True)
    Consignor_RoomNumberId = models.CharField(max_length=20, blank=True)

    # ПОЛУЧАТЕЛЬ
    # PIATConsigneeDetails
    Consignee_SubjectBriefName = models.CharField(max_length=120, blank=False)
    Consignee_TaxpayerId = models.CharField(max_length=20, blank=True)
    Consignee_UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    Consignee_RegionName = models.CharField(max_length=120, blank=True)
    Consignee_CityName = models.CharField(max_length=120, blank=False)
    Consignee_StreetName = models.CharField(max_length=120, blank=False)
    Consignee_BuildingNumberId = models.CharField(max_length=50, blank=True)
    Consignee_RoomNumberId = models.CharField(max_length=20, blank=True)

    # ДЕКЛАРАНТ
    # PITransitDeclarantDetails
    TransitDeclarant_EqualIndicator = models.CharField(max_length=1, default='0')
    TransitDeclarant_SubjectBriefName = models.CharField(max_length=120, blank=False)
    TransitDeclarant_TaxpayerId = models.CharField(max_length=20, blank=True)
    TransitDeclarant_UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    TransitDeclarant_RegionName = models.CharField(max_length=120, blank=True)
    TransitDeclarant_CityName = models.CharField(max_length=120, blank=False)
    TransitDeclarant_StreetName = models.CharField(max_length=120, blank=False)
    TransitDeclarant_BuildingNumberId = models.CharField(max_length=50, blank=True)
    TransitDeclarant_RoomNumberId = models.CharField(max_length=20, blank=True)

    # ПЕРЕВОЗЧИК ПО ТТ ЕАЭС
    # PIUnionCarrierDetails
    UnionCarrier_SubjectBriefName = models.CharField(max_length=120, blank=False)
    UnionCarrier_TaxpayerId = models.CharField(max_length=20, blank=True)
    UnionCarrier_UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    UnionCarrier_RegionName = models.CharField(max_length=120, blank=True)
    UnionCarrier_CityName = models.CharField(max_length=120, blank=False)
    UnionCarrier_StreetName = models.CharField(max_length=120, blank=False)
    UnionCarrier_BuildingNumberId = models.CharField(max_length=50, blank=True)
    UnionCarrier_RoomNumberId = models.CharField(max_length=20, blank=True)

    # ПЕРЕВОЗЧИК
    # CarrierRepresentativeDetails
    CarrierRepresentative_FirstName = models.CharField(max_length=120, blank=False)
    CarrierRepresentative_MiddleName = models.CharField(max_length=120, blank=True)
    CarrierRepresentative_LastName = models.CharField(max_length=120, blank=False)
    CarrierRepresentative_PositionName = models.CharField(max_length=120, default='ВОДИТЕЛЬ')
    CarrierRepresentative_UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    CarrierRepresentative_IdentityDocKindCode = models.CharField(max_length=7, blank=False)
    CarrierRepresentative_DocId = models.CharField(max_length=50, blank=False)
    CarrierRepresentative_DocCreationDate = models.DateField(blank=False)
    CarrierRepresentative_DocValidityDate = models.DateField(blank=True, null=True)
    CarrierRepresentative_RoleCode = models.CharField(max_length=1, default='1')

    # PIATCarrierDetails
    Carrier_SubjectBriefName = models.CharField(max_length=120, blank=False)
    Carrier_TaxpayerId = models.CharField(max_length=20, blank=True)
    Carrier_UnifiedCountryCode = models.CharField(max_length=2, blank=False)
    Carrier_RegionName = models.CharField(max_length=120, blank=True)
    Carrier_CityName = models.CharField(max_length=120, blank=False)
    Carrier_StreetName = models.CharField(max_length=120, blank=False)
    Carrier_BuildingNumberId = models.CharField(max_length=50, blank=True)
    Carrier_RoomNumberId = models.CharField(max_length=20, blank=True)