# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T12:09:09+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field, RootModel, conint, constr


class Arn(RootModel[str]):
    root: str


class AssociateEntityToThingResponse(BaseModel):
    pass


class DefinitionLanguage(Enum):
    GRAPHQL = 'GRAPHQL'


class DefinitionText(RootModel[constr(max_length=1048576)]):
    root: constr(max_length=1048576)


class DeleteFlowTemplateResponse(BaseModel):
    pass


class DeleteNamespaceRequest(BaseModel):
    pass


class DeleteSystemInstanceResponse(BaseModel):
    pass


class DeleteSystemTemplateResponse(BaseModel):
    pass


class DeploymentTarget(Enum):
    GREENGRASS = 'GREENGRASS'
    CLOUD = 'CLOUD'


class DeprecateExistingEntities(RootModel[bool]):
    root: bool


class DeprecateFlowTemplateResponse(BaseModel):
    pass


class DeprecateSystemTemplateResponse(BaseModel):
    pass


class DissociateEntityFromThingResponse(BaseModel):
    pass


class Enabled(RootModel[bool]):
    root: bool


class EntityFilterName(Enum):
    NAME = 'NAME'
    NAMESPACE = 'NAMESPACE'
    SEMANTIC_TYPE_PATH = 'SEMANTIC_TYPE_PATH'
    REFERENCED_ENTITY_ID = 'REFERENCED_ENTITY_ID'


class EntityFilterValue(RootModel[str]):
    root: str


class EntityFilterValues(RootModel[List[EntityFilterValue]]):
    root: List[EntityFilterValue]


class EntityType(Enum):
    DEVICE = 'DEVICE'
    SERVICE = 'SERVICE'
    DEVICE_MODEL = 'DEVICE_MODEL'
    CAPABILITY = 'CAPABILITY'
    STATE = 'STATE'
    ACTION = 'ACTION'
    EVENT = 'EVENT'
    PROPERTY = 'PROPERTY'
    MAPPING = 'MAPPING'
    ENUM = 'ENUM'


class EntityTypes(RootModel[List[EntityType]]):
    root: List[EntityType]


class FlowExecutionEventType(Enum):
    EXECUTION_STARTED = 'EXECUTION_STARTED'
    EXECUTION_FAILED = 'EXECUTION_FAILED'
    EXECUTION_ABORTED = 'EXECUTION_ABORTED'
    EXECUTION_SUCCEEDED = 'EXECUTION_SUCCEEDED'
    STEP_STARTED = 'STEP_STARTED'
    STEP_FAILED = 'STEP_FAILED'
    STEP_SUCCEEDED = 'STEP_SUCCEEDED'
    ACTIVITY_SCHEDULED = 'ACTIVITY_SCHEDULED'
    ACTIVITY_STARTED = 'ACTIVITY_STARTED'
    ACTIVITY_FAILED = 'ACTIVITY_FAILED'
    ACTIVITY_SUCCEEDED = 'ACTIVITY_SUCCEEDED'
    START_FLOW_EXECUTION_TASK = 'START_FLOW_EXECUTION_TASK'
    SCHEDULE_NEXT_READY_STEPS_TASK = 'SCHEDULE_NEXT_READY_STEPS_TASK'
    THING_ACTION_TASK = 'THING_ACTION_TASK'
    THING_ACTION_TASK_FAILED = 'THING_ACTION_TASK_FAILED'
    THING_ACTION_TASK_SUCCEEDED = 'THING_ACTION_TASK_SUCCEEDED'
    ACKNOWLEDGE_TASK_MESSAGE = 'ACKNOWLEDGE_TASK_MESSAGE'


class FlowExecutionId(RootModel[str]):
    root: str


class FlowExecutionMessageId(RootModel[str]):
    root: str


class FlowExecutionMessagePayload(RootModel[str]):
    root: str


class FlowExecutionStatus(Enum):
    RUNNING = 'RUNNING'
    ABORTED = 'ABORTED'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'


class FlowTemplateFilterName(Enum):
    DEVICE_MODEL_ID = 'DEVICE_MODEL_ID'


class FlowTemplateFilterValue(
    RootModel[
        constr(
            pattern=r'^urn:tdm:(([a-z]{2}-(gov-)?[a-z]{4,9}-[0-9]{1,3}/[0-9]+/)*[\p{Alnum}_]+(/[\p{Alnum}_]+)*):([\p{Alpha}]*):([\p{Alnum}_]+(/[\p{Alnum}_]+)*)$'
        )
    ]
):
    root: constr(
        pattern=r'^urn:tdm:(([a-z]{2}-(gov-)?[a-z]{4,9}-[0-9]{1,3}/[0-9]+/)*[\p{Alnum}_]+(/[\p{Alnum}_]+)*):([\p{Alpha}]*):([\p{Alnum}_]+(/[\p{Alnum}_]+)*)$'
    )


class FlowTemplateFilterValues(RootModel[List[FlowTemplateFilterValue]]):
    root: List[FlowTemplateFilterValue]


class GetNamespaceDeletionStatusRequest(BaseModel):
    pass


class GreengrassDeploymentId(RootModel[str]):
    root: str


class GreengrassGroupId(RootModel[str]):
    root: str


class GreengrassGroupVersionId(RootModel[str]):
    root: str


class GroupName(RootModel[str]):
    root: str


class InternalFailureException(RootModel[Any]):
    root: Any


class InvalidRequestException(RootModel[Any]):
    root: Any


class LimitExceededException(RootModel[Any]):
    root: Any


class MaxResults(RootModel[conint(ge=1, le=250)]):
    root: conint(ge=1, le=250)


class NamespaceDeletionStatus(Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'


class NamespaceDeletionStatusErrorCodes(Enum):
    VALIDATION_FAILED = 'VALIDATION_FAILED'


class NamespaceName(RootModel[constr(max_length=128)]):
    root: constr(max_length=128)


class NextToken(RootModel[str]):
    root: str


class ResourceAlreadyExistsException(RootModel[Any]):
    root: Any


class ResourceArn(RootModel[constr(min_length=1, max_length=2048)]):
    root: constr(min_length=1, max_length=2048)


class ResourceInUseException(RootModel[Any]):
    root: Any


class ResourceNotFoundException(RootModel[Any]):
    root: Any


class RoleArn(RootModel[constr(min_length=20, max_length=2048)]):
    root: constr(min_length=20, max_length=2048)


class S3BucketName(RootModel[str]):
    root: str


class String(RootModel[str]):
    root: str


class StringList(RootModel[List[String]]):
    root: List[String]


class SyncWithPublicNamespace(RootModel[bool]):
    root: bool


class SystemInstanceDeploymentStatus(Enum):
    NOT_DEPLOYED = 'NOT_DEPLOYED'
    BOOTSTRAP = 'BOOTSTRAP'
    DEPLOY_IN_PROGRESS = 'DEPLOY_IN_PROGRESS'
    DEPLOYED_IN_TARGET = 'DEPLOYED_IN_TARGET'
    UNDEPLOY_IN_PROGRESS = 'UNDEPLOY_IN_PROGRESS'
    FAILED = 'FAILED'
    PENDING_DELETE = 'PENDING_DELETE'
    DELETED_IN_TARGET = 'DELETED_IN_TARGET'


class SystemInstanceFilterName(Enum):
    SYSTEM_TEMPLATE_ID = 'SYSTEM_TEMPLATE_ID'
    STATUS = 'STATUS'
    GREENGRASS_GROUP_NAME = 'GREENGRASS_GROUP_NAME'


class SystemInstanceFilterValue(RootModel[str]):
    root: str


class SystemInstanceFilterValues(RootModel[List[SystemInstanceFilterValue]]):
    root: List[SystemInstanceFilterValue]


class SystemTemplateFilterName(Enum):
    FLOW_TEMPLATE_ID = 'FLOW_TEMPLATE_ID'


class SystemTemplateFilterValue(
    RootModel[
        constr(
            pattern=r'^urn:tdm:(([a-z]{2}-(gov-)?[a-z]{4,9}-[0-9]{1,3}/[0-9]+/)*[\p{Alnum}_]+(/[\p{Alnum}_]+)*):([\p{Alpha}]*):([\p{Alnum}_]+(/[\p{Alnum}_]+)*)$'
        )
    ]
):
    root: constr(
        pattern=r'^urn:tdm:(([a-z]{2}-(gov-)?[a-z]{4,9}-[0-9]{1,3}/[0-9]+/)*[\p{Alnum}_]+(/[\p{Alnum}_]+)*):([\p{Alpha}]*):([\p{Alnum}_]+(/[\p{Alnum}_]+)*)$'
    )


class SystemTemplateFilterValues(RootModel[List[SystemTemplateFilterValue]]):
    root: List[SystemTemplateFilterValue]


class TagKey(
    RootModel[
        constr(pattern=r'^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$', min_length=1, max_length=128)
    ]
):
    root: constr(
        pattern=r'^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$', min_length=1, max_length=128
    )


class TagKeyList(RootModel[List[TagKey]]):
    root: List[TagKey] = Field(..., max_length=50, min_length=1)


class TagResourceResponse(BaseModel):
    pass


class TagValue(RootModel[constr(min_length=1, max_length=256)]):
    root: constr(min_length=1, max_length=256)


class ThingArn(RootModel[str]):
    root: str


class ThingName(
    RootModel[constr(pattern=r'[a-zA-Z0-9:_-]+', min_length=1, max_length=128)]
):
    root: constr(pattern=r'[a-zA-Z0-9:_-]+', min_length=1, max_length=128)


class ThrottlingException(RootModel[Any]):
    root: Any


class Timestamp(RootModel[datetime]):
    root: datetime


class UntagResourceRequest(BaseModel):
    resourceArn: ResourceArn
    tagKeys: TagKeyList


class UntagResourceResponse(BaseModel):
    pass


class UploadId(RootModel[constr(min_length=1, max_length=40)]):
    root: constr(min_length=1, max_length=40)


class UploadStatus(Enum):
    IN_PROGRESS = 'IN_PROGRESS'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'


class Urn(
    RootModel[
        constr(
            pattern=r'^urn:tdm:(([a-z]{2}-(gov-)?[a-z]{4,9}-[0-9]{1,3}/[0-9]+/)*[\p{Alnum}_]+(/[\p{Alnum}_]+)*):([\p{Alpha}]*):([\p{Alnum}_]+(/[\p{Alnum}_]+)*)$',
            max_length=160,
        )
    ]
):
    root: constr(
        pattern=r'^urn:tdm:(([a-z]{2}-(gov-)?[a-z]{4,9}-[0-9]{1,3}/[0-9]+/)*[\p{Alnum}_]+(/[\p{Alnum}_]+)*):([\p{Alpha}]*):([\p{Alnum}_]+(/[\p{Alnum}_]+)*)$',
        max_length=160,
    )


class Urns(RootModel[List[Urn]]):
    root: List[Urn] = Field(..., max_length=25, min_length=0)


class Version(RootModel[int]):
    root: int


class XAmzTarget(Enum):
    IotThingsGraphFrontEndService_AssociateEntityToThing = (
        'IotThingsGraphFrontEndService.AssociateEntityToThing'
    )


class XAmzTarget1(Enum):
    IotThingsGraphFrontEndService_CreateFlowTemplate = (
        'IotThingsGraphFrontEndService.CreateFlowTemplate'
    )


class XAmzTarget2(Enum):
    IotThingsGraphFrontEndService_CreateSystemInstance = (
        'IotThingsGraphFrontEndService.CreateSystemInstance'
    )


class XAmzTarget3(Enum):
    IotThingsGraphFrontEndService_CreateSystemTemplate = (
        'IotThingsGraphFrontEndService.CreateSystemTemplate'
    )


class XAmzTarget4(Enum):
    IotThingsGraphFrontEndService_DeleteFlowTemplate = (
        'IotThingsGraphFrontEndService.DeleteFlowTemplate'
    )


class XAmzTarget5(Enum):
    IotThingsGraphFrontEndService_DeleteNamespace = (
        'IotThingsGraphFrontEndService.DeleteNamespace'
    )


class XAmzTarget6(Enum):
    IotThingsGraphFrontEndService_DeleteSystemInstance = (
        'IotThingsGraphFrontEndService.DeleteSystemInstance'
    )


class XAmzTarget7(Enum):
    IotThingsGraphFrontEndService_DeleteSystemTemplate = (
        'IotThingsGraphFrontEndService.DeleteSystemTemplate'
    )


class XAmzTarget8(Enum):
    IotThingsGraphFrontEndService_DeploySystemInstance = (
        'IotThingsGraphFrontEndService.DeploySystemInstance'
    )


class XAmzTarget9(Enum):
    IotThingsGraphFrontEndService_DeprecateFlowTemplate = (
        'IotThingsGraphFrontEndService.DeprecateFlowTemplate'
    )


class XAmzTarget10(Enum):
    IotThingsGraphFrontEndService_DeprecateSystemTemplate = (
        'IotThingsGraphFrontEndService.DeprecateSystemTemplate'
    )


class XAmzTarget11(Enum):
    IotThingsGraphFrontEndService_DescribeNamespace = (
        'IotThingsGraphFrontEndService.DescribeNamespace'
    )


class XAmzTarget12(Enum):
    IotThingsGraphFrontEndService_DissociateEntityFromThing = (
        'IotThingsGraphFrontEndService.DissociateEntityFromThing'
    )


class XAmzTarget13(Enum):
    IotThingsGraphFrontEndService_GetEntities = (
        'IotThingsGraphFrontEndService.GetEntities'
    )


class XAmzTarget14(Enum):
    IotThingsGraphFrontEndService_GetFlowTemplate = (
        'IotThingsGraphFrontEndService.GetFlowTemplate'
    )


class XAmzTarget15(Enum):
    IotThingsGraphFrontEndService_GetFlowTemplateRevisions = (
        'IotThingsGraphFrontEndService.GetFlowTemplateRevisions'
    )


class XAmzTarget16(Enum):
    IotThingsGraphFrontEndService_GetNamespaceDeletionStatus = (
        'IotThingsGraphFrontEndService.GetNamespaceDeletionStatus'
    )


class XAmzTarget17(Enum):
    IotThingsGraphFrontEndService_GetSystemInstance = (
        'IotThingsGraphFrontEndService.GetSystemInstance'
    )


class XAmzTarget18(Enum):
    IotThingsGraphFrontEndService_GetSystemTemplate = (
        'IotThingsGraphFrontEndService.GetSystemTemplate'
    )


class XAmzTarget19(Enum):
    IotThingsGraphFrontEndService_GetSystemTemplateRevisions = (
        'IotThingsGraphFrontEndService.GetSystemTemplateRevisions'
    )


class XAmzTarget20(Enum):
    IotThingsGraphFrontEndService_GetUploadStatus = (
        'IotThingsGraphFrontEndService.GetUploadStatus'
    )


class XAmzTarget21(Enum):
    IotThingsGraphFrontEndService_ListFlowExecutionMessages = (
        'IotThingsGraphFrontEndService.ListFlowExecutionMessages'
    )


class XAmzTarget22(Enum):
    IotThingsGraphFrontEndService_ListTagsForResource = (
        'IotThingsGraphFrontEndService.ListTagsForResource'
    )


class XAmzTarget23(Enum):
    IotThingsGraphFrontEndService_SearchEntities = (
        'IotThingsGraphFrontEndService.SearchEntities'
    )


class XAmzTarget24(Enum):
    IotThingsGraphFrontEndService_SearchFlowExecutions = (
        'IotThingsGraphFrontEndService.SearchFlowExecutions'
    )


class XAmzTarget25(Enum):
    IotThingsGraphFrontEndService_SearchFlowTemplates = (
        'IotThingsGraphFrontEndService.SearchFlowTemplates'
    )


class XAmzTarget26(Enum):
    IotThingsGraphFrontEndService_SearchSystemInstances = (
        'IotThingsGraphFrontEndService.SearchSystemInstances'
    )


class XAmzTarget27(Enum):
    IotThingsGraphFrontEndService_SearchSystemTemplates = (
        'IotThingsGraphFrontEndService.SearchSystemTemplates'
    )


class XAmzTarget28(Enum):
    IotThingsGraphFrontEndService_SearchThings = (
        'IotThingsGraphFrontEndService.SearchThings'
    )


class XAmzTarget29(Enum):
    IotThingsGraphFrontEndService_TagResource = (
        'IotThingsGraphFrontEndService.TagResource'
    )


class XAmzTarget30(Enum):
    IotThingsGraphFrontEndService_UndeploySystemInstance = (
        'IotThingsGraphFrontEndService.UndeploySystemInstance'
    )


class XAmzTarget31(Enum):
    IotThingsGraphFrontEndService_UntagResource = (
        'IotThingsGraphFrontEndService.UntagResource'
    )


class XAmzTarget32(Enum):
    IotThingsGraphFrontEndService_UpdateFlowTemplate = (
        'IotThingsGraphFrontEndService.UpdateFlowTemplate'
    )


class XAmzTarget33(Enum):
    IotThingsGraphFrontEndService_UpdateSystemTemplate = (
        'IotThingsGraphFrontEndService.UpdateSystemTemplate'
    )


class XAmzTarget34(Enum):
    IotThingsGraphFrontEndService_UploadEntityDefinitions = (
        'IotThingsGraphFrontEndService.UploadEntityDefinitions'
    )


class AssociateEntityToThingRequest(BaseModel):
    entityId: Urn
    namespaceVersion: Optional[Version] = None
    thingName: ThingName


class DefinitionDocument(BaseModel):
    language: DefinitionLanguage
    text: DefinitionText


class DeleteFlowTemplateRequest(BaseModel):
    id: Urn


class DeleteNamespaceResponse(BaseModel):
    namespaceArn: Optional[Arn] = None
    namespaceName: Optional[NamespaceName] = None


class DeleteSystemInstanceRequest(BaseModel):
    id: Optional[Urn] = None


class DeleteSystemTemplateRequest(BaseModel):
    id: Urn


class DependencyRevision(BaseModel):
    id: Optional[Urn] = None
    revisionNumber: Optional[Version] = None


class DependencyRevisions(RootModel[List[DependencyRevision]]):
    root: List[DependencyRevision]


class DeploySystemInstanceRequest(BaseModel):
    id: Optional[Urn] = None


class DeprecateFlowTemplateRequest(BaseModel):
    id: Urn


class DeprecateSystemTemplateRequest(BaseModel):
    id: Urn


class DescribeNamespaceRequest(BaseModel):
    namespaceName: Optional[NamespaceName] = None


class DescribeNamespaceResponse(BaseModel):
    namespaceArn: Optional[Arn] = None
    namespaceName: Optional[NamespaceName] = None
    namespaceVersion: Optional[Version] = None
    trackingNamespaceName: Optional[NamespaceName] = None
    trackingNamespaceVersion: Optional[Version] = None


class DissociateEntityFromThingRequest(BaseModel):
    entityType: EntityType
    thingName: ThingName


class EntityDescription(BaseModel):
    arn: Optional[Arn] = None
    createdAt: Optional[Timestamp] = None
    definition: Optional[DefinitionDocument] = None
    id: Optional[Urn] = None
    type: Optional[EntityType] = None


class EntityDescriptions(RootModel[List[EntityDescription]]):
    root: List[EntityDescription]


class EntityFilter(BaseModel):
    name: Optional[EntityFilterName] = None
    value: Optional[EntityFilterValues] = None


class EntityFilters(RootModel[List[EntityFilter]]):
    root: List[EntityFilter]


class FlowExecutionMessage(BaseModel):
    eventType: Optional[FlowExecutionEventType] = None
    messageId: Optional[FlowExecutionMessageId] = None
    payload: Optional[FlowExecutionMessagePayload] = None
    timestamp: Optional[Timestamp] = None


class FlowExecutionMessages(RootModel[List[FlowExecutionMessage]]):
    root: List[FlowExecutionMessage]


class FlowExecutionSummary(BaseModel):
    createdAt: Optional[Timestamp] = None
    flowExecutionId: Optional[FlowExecutionId] = None
    flowTemplateId: Optional[Urn] = None
    status: Optional[FlowExecutionStatus] = None
    systemInstanceId: Optional[Urn] = None
    updatedAt: Optional[Timestamp] = None


class FlowTemplateFilter(BaseModel):
    name: FlowTemplateFilterName
    value: FlowTemplateFilterValues


class FlowTemplateFilters(RootModel[List[FlowTemplateFilter]]):
    root: List[FlowTemplateFilter]


class FlowTemplateSummary(BaseModel):
    arn: Optional[Arn] = None
    createdAt: Optional[Timestamp] = None
    id: Optional[Urn] = None
    revisionNumber: Optional[Version] = None


class GetEntitiesRequest(BaseModel):
    ids: Urns
    namespaceVersion: Optional[Version] = None


class GetEntitiesResponse(BaseModel):
    descriptions: Optional[EntityDescriptions] = None


class GetFlowTemplateRequest(BaseModel):
    id: Urn
    revisionNumber: Optional[Version] = None


class GetFlowTemplateRevisionsRequest(BaseModel):
    id: Urn
    maxResults: Optional[MaxResults] = None
    nextToken: Optional[NextToken] = None


class GetNamespaceDeletionStatusResponse(BaseModel):
    errorCode: Optional[NamespaceDeletionStatusErrorCodes] = None
    errorMessage: Optional[String] = None
    namespaceArn: Optional[Arn] = None
    namespaceName: Optional[NamespaceName] = None
    status: Optional[NamespaceDeletionStatus] = None


class GetSystemInstanceRequest(BaseModel):
    id: Urn


class GetSystemTemplateRequest(BaseModel):
    id: Urn
    revisionNumber: Optional[Version] = None


class GetSystemTemplateRevisionsRequest(BaseModel):
    id: Urn
    maxResults: Optional[MaxResults] = None
    nextToken: Optional[NextToken] = None


class GetUploadStatusRequest(BaseModel):
    uploadId: UploadId


class GetUploadStatusResponse(BaseModel):
    createdDate: Timestamp
    failureReason: Optional[StringList] = None
    namespaceArn: Optional[Arn] = None
    namespaceName: Optional[NamespaceName] = None
    namespaceVersion: Optional[Version] = None
    uploadId: UploadId
    uploadStatus: UploadStatus


class ListFlowExecutionMessagesRequest(BaseModel):
    flowExecutionId: FlowExecutionId
    maxResults: Optional[MaxResults] = None
    nextToken: Optional[NextToken] = None


class ListFlowExecutionMessagesResponse(BaseModel):
    messages: Optional[FlowExecutionMessages] = None
    nextToken: Optional[NextToken] = None


class ListTagsForResourceRequest(BaseModel):
    maxResults: Optional[MaxResults] = None
    nextToken: Optional[NextToken] = None
    resourceArn: ResourceArn


class MetricsConfiguration(BaseModel):
    cloudMetricEnabled: Optional[Enabled] = None
    metricRuleRoleArn: Optional[RoleArn] = None


class SearchEntitiesRequest(BaseModel):
    entityTypes: EntityTypes
    filters: Optional[EntityFilters] = None
    maxResults: Optional[MaxResults] = None
    namespaceVersion: Optional[Version] = None
    nextToken: Optional[NextToken] = None


class SearchEntitiesResponse(BaseModel):
    descriptions: Optional[EntityDescriptions] = None
    nextToken: Optional[NextToken] = None


class SearchFlowExecutionsRequest(BaseModel):
    endTime: Optional[Timestamp] = None
    flowExecutionId: Optional[FlowExecutionId] = None
    maxResults: Optional[MaxResults] = None
    nextToken: Optional[NextToken] = None
    startTime: Optional[Timestamp] = None
    systemInstanceId: Urn


class SearchFlowTemplatesRequest(BaseModel):
    filters: Optional[FlowTemplateFilters] = None
    maxResults: Optional[MaxResults] = None
    nextToken: Optional[NextToken] = None


class SearchThingsRequest(BaseModel):
    entityId: Urn
    maxResults: Optional[MaxResults] = None
    namespaceVersion: Optional[Version] = None
    nextToken: Optional[NextToken] = None


class SystemInstanceFilter(BaseModel):
    name: Optional[SystemInstanceFilterName] = None
    value: Optional[SystemInstanceFilterValues] = None


class SystemInstanceFilters(RootModel[List[SystemInstanceFilter]]):
    root: List[SystemInstanceFilter]


class SystemInstanceSummary(BaseModel):
    arn: Optional[Arn] = None
    createdAt: Optional[Timestamp] = None
    greengrassGroupId: Optional[GreengrassGroupId] = None
    greengrassGroupName: Optional[GroupName] = None
    greengrassGroupVersionId: Optional[GreengrassGroupVersionId] = None
    id: Optional[Urn] = None
    status: Optional[SystemInstanceDeploymentStatus] = None
    target: Optional[DeploymentTarget] = None
    updatedAt: Optional[Timestamp] = None


class SystemTemplateFilter(BaseModel):
    name: SystemTemplateFilterName
    value: SystemTemplateFilterValues


class SystemTemplateFilters(RootModel[List[SystemTemplateFilter]]):
    root: List[SystemTemplateFilter]


class SystemTemplateSummary(BaseModel):
    arn: Optional[Arn] = None
    createdAt: Optional[Timestamp] = None
    id: Optional[Urn] = None
    revisionNumber: Optional[Version] = None


class Tag(BaseModel):
    key: TagKey
    value: TagValue


class TagList(RootModel[List[Tag]]):
    root: List[Tag] = Field(..., max_length=50, min_length=0)


class TagResourceRequest(BaseModel):
    resourceArn: ResourceArn
    tags: TagList


class Thing(BaseModel):
    thingArn: Optional[ThingArn] = None
    thingName: Optional[ThingName] = None


class Things(RootModel[List[Thing]]):
    root: List[Thing]


class UndeploySystemInstanceRequest(BaseModel):
    id: Optional[Urn] = None


class UndeploySystemInstanceResponse(BaseModel):
    summary: Optional[SystemInstanceSummary] = None


class UpdateFlowTemplateRequest(BaseModel):
    compatibleNamespaceVersion: Optional[Version] = None
    definition: DefinitionDocument
    id: Urn


class UpdateFlowTemplateResponse(BaseModel):
    summary: Optional[FlowTemplateSummary] = None


class UpdateSystemTemplateRequest(BaseModel):
    compatibleNamespaceVersion: Optional[Version] = None
    definition: DefinitionDocument
    id: Urn


class UpdateSystemTemplateResponse(BaseModel):
    summary: Optional[SystemTemplateSummary] = None


class UploadEntityDefinitionsRequest(BaseModel):
    deprecateExistingEntities: Optional[DeprecateExistingEntities] = None
    document: Optional[DefinitionDocument] = None
    syncWithPublicNamespace: Optional[SyncWithPublicNamespace] = None


class UploadEntityDefinitionsResponse(BaseModel):
    uploadId: UploadId


class CreateFlowTemplateRequest(BaseModel):
    compatibleNamespaceVersion: Optional[Version] = None
    definition: DefinitionDocument


class CreateFlowTemplateResponse(BaseModel):
    summary: Optional[FlowTemplateSummary] = None


class CreateSystemInstanceRequest(BaseModel):
    definition: DefinitionDocument
    flowActionsRoleArn: Optional[RoleArn] = None
    greengrassGroupName: Optional[GroupName] = None
    metricsConfiguration: Optional[MetricsConfiguration] = None
    s3BucketName: Optional[S3BucketName] = None
    tags: Optional[TagList] = None
    target: DeploymentTarget


class CreateSystemInstanceResponse(BaseModel):
    summary: Optional[SystemInstanceSummary] = None


class CreateSystemTemplateRequest(BaseModel):
    compatibleNamespaceVersion: Optional[Version] = None
    definition: DefinitionDocument


class CreateSystemTemplateResponse(BaseModel):
    summary: Optional[SystemTemplateSummary] = None


class DeploySystemInstanceResponse(BaseModel):
    greengrassDeploymentId: Optional[GreengrassDeploymentId] = None
    summary: SystemInstanceSummary


class FlowExecutionSummaries(RootModel[List[FlowExecutionSummary]]):
    root: List[FlowExecutionSummary]


class FlowTemplateDescription(BaseModel):
    definition: Optional[DefinitionDocument] = None
    summary: Optional[FlowTemplateSummary] = None
    validatedNamespaceVersion: Optional[Version] = None


class FlowTemplateSummaries(RootModel[List[FlowTemplateSummary]]):
    root: List[FlowTemplateSummary]


class GetFlowTemplateResponse(BaseModel):
    description: Optional[FlowTemplateDescription] = None


class GetFlowTemplateRevisionsResponse(BaseModel):
    nextToken: Optional[NextToken] = None
    summaries: Optional[FlowTemplateSummaries] = None


class ListTagsForResourceResponse(BaseModel):
    nextToken: Optional[NextToken] = None
    tags: Optional[TagList] = None


class SearchFlowExecutionsResponse(BaseModel):
    nextToken: Optional[NextToken] = None
    summaries: Optional[FlowExecutionSummaries] = None


class SearchFlowTemplatesResponse(BaseModel):
    nextToken: Optional[NextToken] = None
    summaries: Optional[FlowTemplateSummaries] = None


class SearchSystemInstancesRequest(BaseModel):
    filters: Optional[SystemInstanceFilters] = None
    maxResults: Optional[MaxResults] = None
    nextToken: Optional[NextToken] = None


class SearchSystemTemplatesRequest(BaseModel):
    filters: Optional[SystemTemplateFilters] = None
    maxResults: Optional[MaxResults] = None
    nextToken: Optional[NextToken] = None


class SearchThingsResponse(BaseModel):
    nextToken: Optional[NextToken] = None
    things: Optional[Things] = None


class SystemInstanceDescription(BaseModel):
    definition: Optional[DefinitionDocument] = None
    flowActionsRoleArn: Optional[RoleArn] = None
    metricsConfiguration: Optional[MetricsConfiguration] = None
    s3BucketName: Optional[S3BucketName] = None
    summary: Optional[SystemInstanceSummary] = None
    validatedDependencyRevisions: Optional[DependencyRevisions] = None
    validatedNamespaceVersion: Optional[Version] = None


class SystemInstanceSummaries(RootModel[List[SystemInstanceSummary]]):
    root: List[SystemInstanceSummary]


class SystemTemplateDescription(BaseModel):
    definition: Optional[DefinitionDocument] = None
    summary: Optional[SystemTemplateSummary] = None
    validatedNamespaceVersion: Optional[Version] = None


class SystemTemplateSummaries(RootModel[List[SystemTemplateSummary]]):
    root: List[SystemTemplateSummary]


class GetSystemInstanceResponse(BaseModel):
    description: Optional[SystemInstanceDescription] = None


class GetSystemTemplateResponse(BaseModel):
    description: Optional[SystemTemplateDescription] = None


class GetSystemTemplateRevisionsResponse(BaseModel):
    nextToken: Optional[NextToken] = None
    summaries: Optional[SystemTemplateSummaries] = None


class SearchSystemInstancesResponse(BaseModel):
    nextToken: Optional[NextToken] = None
    summaries: Optional[SystemInstanceSummaries] = None


class SearchSystemTemplatesResponse(BaseModel):
    nextToken: Optional[NextToken] = None
    summaries: Optional[SystemTemplateSummaries] = None
