from datetime import datetime
from typing import Dict, List, Union

from pydantic import BaseModel, Field


class FeedlyCategory(BaseModel):
    id: str | None = Field(None, description="Category ID")
    label: str | None = Field(None, description="Category label")


class FeedlyTag(BaseModel):
    id: str | None = Field(None, description="Tag ID")
    label: str | None = Field(None, description="Tag label")
    addedBy: str | None = Field(None, description="User who added the tag")
    actionTimestamp: int | None = Field(
        None, description="Timestamp of tag action (milliseconds since epoch)"
    )


class FeedlyPart(BaseModel):
    text: str | None = Field(None, description="Text of the part")
    id: str | None = Field(None, description="ID of the part")
    label: str | None = Field(None, description="Label of the part")


class FeedlySearchTerms(BaseModel):
    parts: List[FeedlyPart] | None = Field(None, description="List of matched parts")
    isComplexFilter: bool | None = Field(
        None, description="Indicates if the search filter is complex"
    )


class FeedlySources(BaseModel):
    streamId: str | None = Field(None, description="Stream ID of the source")
    title: str | None = Field(None, description="Title of the source")
    feedlyFeedType: str | None = Field(None, description="Type of the Feedly feed")
    searchTerms: FeedlySearchTerms | None = Field(
        None, description="Search terms used in the source"
    )


class FeedlyArticleContent(BaseModel):
    content: str | None = Field(None, description="HTML content of the article")
    direction: str | None = Field(None, description="Text direction (ltr or rtl)")


class FeedlyOrigin(BaseModel):
    streamId: str | None = Field(None, description="Stream ID of the origin")
    title: str | None = Field(None, description="Title of the origin")
    htmlUrl: str | None = Field(None, description="HTML URL of the origin")


class FeedlyAlternate(BaseModel):
    href: str | None = Field(None, description="Alternate URL of the article")
    type: str | None = Field(
        None, description="Type of the alternate URL (e.g., text/html)"
    )


class FeedlyVisual(BaseModel):
    url: str | None = Field(None, description="URL of the featured visual")
    width: int | None = Field(None, description="Width of the visual")
    height: int | None = Field(None, description="Height of the visual")
    contentType: str | None = Field(
        None, description="Content type of the visual (e.g., image/jpeg)"
    )


class FeedlyAnnotations(BaseModel):
    author: str | None = Field(None, description="Author of the annotation")
    authorFirstInitial: str | None = Field(
        None, description="Initial of the author's first name"
    )
    created: int | None = Field(
        None, description="Creation timestamp (milliseconds since epoch)"
    )
    entryId: str | None = Field(None, description="Entry ID of the annotation")
    highlight: Dict[str, Union[int, str | None]] | None = Field(
        None, description="Highlighted text information"
    )
    comment: str | None = Field(None, description="Comment added by the author")
    authorEmail: str | None = Field(None, description="Email of the author")
    authorName: str | None = Field(None, description="Name of the author")
    authorPicture: str | None = Field(None, description="Picture of the author")
    emailMentions: List[str] | None = Field(
        None, description="List of email mentions in the comment"
    )
    slackMentions: List[str] | None = Field(
        None, description="List of Slack mentions in the comment"
    )
    slackMsgIds: Dict[str, Dict[str, str | None]] | None = Field(
        None, description="Slack message IDs and details"
    )


class FeedlyEntity(BaseModel):
    type: str | None = Field(
        None, description="Type of entity (e.g., org, person, location)"
    )
    disambiguated: bool | None = Field(
        None, description="Whether the entity is disambiguated"
    )
    id: str | None = Field(None, description="ID of the entity")
    label: str | None = Field(None, description="Label of the entity")
    mentions: List[FeedlyPart] | None = Field(
        None, description="List of mentions for the entity"
    )
    salienceLevel: str | None = Field(
        None, description="Salience level (mention/about)"
    )
    causes: List[FeedlyPart] | None = Field(
        None, description="List of cause entities for custom topics"
    )


class FeedlyCommonTopic(BaseModel):
    type: str | None = Field(
        None, description="Type of common topic (e.g., industryTopic, dataMention)"
    )
    id: str | None = Field(None, description="ID of the common topic")
    label: str | None = Field(None, description="Label of the common topic")
    score: float | None = Field(
        None, description="Score indicating the relevance of the topic"
    )
    salienceLevel: str | None = Field(
        None, description="Salience level (mention/about)"
    )
    targets: List[FeedlyEntity] | None = Field(
        None, description="List of target entities for cyber events"
    )
    causes: List[FeedlyEntity] | None = Field(
        None, description="List of cause entities for data mentions"
    )


class FeedlyLeoSummarySentence(BaseModel):
    text: str | None = Field(None, description="Summary sentence text")
    position: int | None = Field(
        None, description="Position of the sentence in the content"
    )
    score: float | None = Field(
        None, description="Score indicating the relevance of the sentence"
    )


class FeedlyLeoSummary(BaseModel):
    sentences: List[FeedlyLeoSummarySentence] | None = Field(
        None, description="List of summary sentences"
    )


class FeedlyDuplicate(BaseModel):
    entryId: str | None = Field(None, description="Entry ID of the duplicate article")
    feedId: str | None = Field(None, description="Feed ID of the duplicate article")
    feedTitle: str | None = Field(
        None, description="Feed title of the duplicate article"
    )
    unread: bool | None = Field(
        None, description="Whether the duplicate article is unread"
    )


class FeedlyCluster(BaseModel):
    id: str | None = Field(None, description="ID of the cluster")


class FeedlyMeme(BaseModel):
    id: str | None = Field(None, description="ID of the featured meme")
    label: str | None = Field(None, description="Label of the featured meme")
    score: float | None = Field(None, description="Score of the featured meme")
    featured: bool | None = Field(None, description="Whether the meme is featured")


class FeedlyEngagement(BaseModel):
    engagement: int | None = Field(None, description="Amount of social engagement")
    engagementRate: float | None = Field(
        None, description="Relative indicator of the article's virality"
    )


class FeedlyLinked(BaseModel):
    id: str | None = Field(None, description="ID of the linked article")
    language: str | None = Field(None, description="Language of the linked article")
    title: str | None = Field(None, description="Title of the linked article")
    url: str | None = Field(None, description="URL of the linked article")


class FeedlyAuthorDetails(BaseModel):
    fullname: str | None = Field(None, description="Full name of the author")
    icon: str | None = Field(None, description="Icon for the author")
    source: str | None = Field(
        None, description="Source of the author details (e.g., Twitter, Reddit)"
    )
    url: str | None = Field(None, description="URL of the author's profile")
    username: str | None = Field(None, description="Username of the author")
    picture: str | None = Field(None, description="Picture of the author")


class FeedlyAiAction(BaseModel):
    created: int | None = Field(
        None, description="Timestamp of the AI action (milliseconds since epoch)"
    )
    type: str | None = Field(
        None, description="Type of AI action (e.g., summary, translation, prediction)"
    )
    summary: str | None = Field(None, description="Summary generated by AI")
    content: str | None = Field(None, description="Translated content")
    title: str | None = Field(None, description="Translated title")
    lang: str | None = Field(None, description="Target language for the translation")
    prompt: str | None = Field(None, description="Prompt for custom prediction action")
    prediction: str | None = Field(None, description="Prediction result")


class FeedlyVulnerabilityInfo(BaseModel):
    description: str | None = Field(
        None, description="Description of the vulnerability"
    )
    cvssScore: float | None = Field(None, description="CVSS score of the vulnerability")
    hasExploit: bool | None = Field(
        None, description="Whether an exploit exists for the vulnerability"
    )
    hasPatch: bool | None = Field(
        None, description="Whether a patch exists for the vulnerability"
    )


class FeedlyEntityWithVulnInfo(FeedlyEntity):
    vulnerabilityInfo: FeedlyVulnerabilityInfo | None = Field(
        None, description="Information about the vulnerability"
    )


class FeedlyIndicatorOfCompromise(BaseModel):
    text: str | None = Field(None, description="Text of the indicator of compromise")
    type: str | None = Field(
        None, description="Type of the indicator of compromise (e.g., domain, ip, hash)"
    )
    canonical: str | None = Field(
        None, description="Canonical representation of the indicator"
    )


class FeedlyIoCExports(BaseModel):
    type: str | None = Field(
        None, description="Type of export (e.g., markdown, stix2.1)"
    )
    url: str | None = Field(None, description="URL of the export")


class FeedlyIoC(BaseModel):
    mentions: List[FeedlyIndicatorOfCompromise] | None = Field(
        None, description="List of identified IoCs"
    )
    exports: List[FeedlyIoCExports] | None = Field(
        None, description="List of export options"
    )


class FeedlyAttackNavigator(BaseModel):
    ttpCount: int | None = Field(None, description="Count of TTPs")
    url: str | None = Field(None, description="URL to the attack navigator JSON")


class FeedlyMetadata(BaseModel):
    id: str | None = Field(None, description="Unique, immutable article ID")
    originId: str | None = Field(None, description="Origin ID of the article")
    recrawled: int | None = Field(
        None,
        description="Timestamp when the article was last recrawled (milliseconds since epoch)",
    )
    language: str | None = Field(
        None, description="Language associated with the article"
    )
    content: FeedlyArticleContent | None = Field(
        None, description="Content of the article"
    )
    title: str | None = Field(None, description="Title of the article")
    crawled: int | None = Field(
        None,
        description="Timestamp when the article was first crawled by Feedly (milliseconds since epoch)",
    )
    author: str | None = Field(None, description="Author of the article")
    origin: FeedlyOrigin | None = Field(
        None, description="Information about the source/origin publishing the RSS feed"
    )
    alternate: List[FeedlyAlternate] | None = Field(
        None, description="List of alternate links to the article"
    )
    updated: int | None = Field(
        None,
        description="Updated date provided by the publisher (milliseconds since epoch)",
    )
    published: int | None = Field(
        None,
        description="Published date provided by the publisher (milliseconds since epoch)",
    )
    canonicalUrl: str | None = Field(None, description="Canonical URL of the article")
    summary: FeedlyArticleContent | None = Field(
        None, description="Summary of the content"
    )
    fullContent: str | None = Field(None, description="Full content of the article")
    visual: FeedlyVisual | None = Field(
        None, description="Featured visual for the article"
    )
    categories: List[FeedlyCategory] | None = Field(
        None, description="List of categories"
    )
    sources: List[FeedlySources] | None = Field(None, description="List of sources")
    canonicalUrl: str | None = Field(None, description="Canonical URL of the article")
    unread: bool | None = Field(None, description="Read/unread status of the article")
    readTime: int | None = Field(
        None,
        description="Timestamp when the article was read (milliseconds since epoch)",
    )
    tags: List[FeedlyTag] | None = Field(
        None, description="List of tags associated with the article"
    )
    annotations: List[FeedlyAnnotations] | None = Field(
        None, description="List of annotations associated with the article"
    )
    entities: List[FeedlyEntityWithVulnInfo] | None = Field(
        None, description="List of entities associated with the article"
    )
    commonTopics: List[FeedlyCommonTopic] | None = Field(
        None, description="List of common topics associated with the article"
    )
    leoSummary: FeedlyLeoSummary | None = Field(
        None, description="Feedly AI summary sentences"
    )
    duplicates: List[FeedlyDuplicate] | None = Field(
        None, description="List of duplicate articles"
    )
    clusters: List[FeedlyCluster] | None = Field(
        None, description="List of clusters the article belongs to"
    )
    featuredMeme: FeedlyMeme | None = Field(
        None, description="Featured meme information"
    )
    engagement: FeedlyEngagement | None = Field(
        None, description="Engagement and engagement rate"
    )
    linked: List[FeedlyLinked] | None = Field(
        None, description="List of linked entries"
    )
    authorDetails: FeedlyAuthorDetails | None = Field(
        None, description="Details about the author for Twitter/Reddit sources"
    )
    previewSearchTerms: FeedlySearchTerms | None = Field(
        None, description="Search terms matched during a search request"
    )
    aiActions: List[FeedlyAiAction] | None = Field(
        None, description="AI actions performed on the article"
    )
    indicatorsOfCompromise: FeedlyIoC | None = Field(
        None, description="Indicators of compromise identified in the article"
    )
    attackNavigator: FeedlyAttackNavigator | None = Field(
        None, description="MITRE ATT&CK navigator link"
    )
