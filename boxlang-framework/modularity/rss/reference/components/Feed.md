# Component: `Feed`

Reads RSS/Atom feeds from URLs or files, and creates new RSS/Atom feeds from data. Compatible with CFML's `cffeed` tag.

## Syntax

### Read Action

```boxlang
<bx:feed
    action="read"
    source="string"
    result="string"
    properties="string"
    query="string"
    xmlVar="string"
    outputFile="string"
    overwrite="boolean"
    timeout="numeric"
    userAgent="string"
    maxItems="numeric"
    itunes="boolean"
    mediaRss="boolean" />
```

### Create Action

```boxlang
<bx:feed
    action="create"
    properties="struct"
    data="array|query"
    xmlVar="string"
    outputFile="string"
    overwrite="boolean"
    columnMap="struct"
    feedType="string"
    escapeChars="boolean"
    result="string" />
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `action` | `string` | No | Action to perform: "read" or "create" | `"read"` |
| `source` | `string` | Yes (read) | URL or file path to the feed to read | |
| `result` | `string` | No | Variable name to store the full feed structure | |
| `name` | `struct/string` | No | For read: alias for result. For create: input struct containing full feed data | |
| `properties` | `struct/string` | Yes (create) | For create: feed metadata. For read: output variable for channel metadata | |
| `data` | `array/query` | Yes (create) | Feed items/entries for creation | |
| `query` | `any` | No | For create: alias for data. For read: output variable for items | |
| `columnMap` | `struct` | No | Map query columns to feed fields (for query data) | `{}` |
| `outputFile` | `string` | No | File path to write the feed XML | |
| `overwrite` | `boolean` | No | Whether to overwrite existing output file | `false` |
| `xmlVar` | `string` | No | Variable name to store the raw XML string | |
| `timeout` | `numeric` | No | HTTP timeout in seconds for read action | `60` |
| `userAgent` | `string` | No | Custom User-Agent for HTTP requests | `""` |
| `maxItems` | `numeric` | No | Maximum number of items to return (read action) | `0` (unlimited) |
| `itunes` | `boolean` | No | Parse iTunes podcast extensions (read action) | `false` |
| `mediaRss` | `boolean` | No | Parse Media RSS extensions (read action) | `false` |
| `feedType` | `string` | No | Feed format for creation: "rss_2.0" or "atom" | `"rss_2.0"` |
| `escapeChars` | `boolean` | No | Escape special characters in create action | `false` |

## Examples

### Basic Feed Reading

```boxlang
<!-- Read a feed and store in result variable -->
<bx:feed
    action="read"
    source="https://example.com/feed.xml"
    result="feedData" />

<bx:output>
    <h2>#feedData.channel.title#</h2>
    <p>Found #arrayLen(feedData.items)# items</p>

    <bx:loop array="#feedData.items#" index="item">
        <h3><a href="#item.link#">#item.title#</a></h3>
        <p>#item.description#</p>
        <small>Published: #item.pubDate#</small>
    </bx:loop>
</bx:output>
```

### Reading with Multiple Output Variables

```boxlang
<!-- Read feed with separate output variables for different data -->
<bx:feed
    action="read"
    source="https://news.example.com/rss.xml"
    result="fullFeed"
    properties="channelInfo"
    query="feedItems"
    xmlVar="rawXml"
    timeout="30" />

<bx:output>
    <h1>#channelInfo.title#</h1>
    <p>#channelInfo.description#</p>

    <!-- feedItems contains just the items array -->
    <bx:loop array="#feedItems#" index="item">
        <div>
            <h3>#item.title#</h3>
            <p>#item.description#</p>
        </div>
    </bx:loop>
</bx:output>
```

### Reading Podcast Feed with iTunes Extensions

```boxlang
<!-- Read podcast feed with iTunes metadata -->
<bx:feed
    action="read"
    source="https://podcast.example.com/feed.xml"
    result="podcastData"
    itunes="true"
    maxItems="10" />

<bx:output>
    <h1>#podcastData.channel.title#</h1>
    <p>Author: #podcastData.channel.itunesAuthor#</p>
    <p>Category: #podcastData.channel.itunesCategory#</p>

    <bx:loop array="#podcastData.items#" index="episode">
        <div>
            <h3>#episode.title#</h3>
            <p>Duration: #episode.itunesDuration ?: 'Unknown'#</p>
            <p>Author: #episode.itunesAuthor ?: 'Unknown'#</p>
            <p>#episode.itunesSummary ?: episode.description#</p>
        </div>
    </bx:loop>
</bx:output>
```

### Reading with Media RSS Extensions

```boxlang
<!-- Read video/media feed with thumbnails -->
<bx:feed
    action="read"
    source="https://video.example.com/feed.xml"
    result="mediaFeed"
    mediaRss="true" />

<bx:output>
    <bx:loop array="#mediaFeed.items#" index="video">
        <div>
            <h3>#video.title#</h3>
            <bx:if condition="structKeyExists(video, 'mediaThumbnailUrl')">
                <img src="#video.mediaThumbnailUrl#" alt="Thumbnail" />
            </bx:if>
            <p>#video.description#</p>
            <bx:if condition="structKeyExists(video, 'mediaContentUrl')">
                <a href="#video.mediaContentUrl#">Watch Video</a>
            </bx:if>
        </div>
    </bx:loop>
</bx:output>
```

### Saving Feed to File

```boxlang
<!-- Read feed and save raw XML to file -->
<bx:feed
    action="read"
    source="https://example.com/feed.xml"
    result="feedData"
    outputFile="/backups/feed-backup.xml"
    overwrite="true" />
```

### Creating a Basic RSS Feed

```boxlang
<!-- Create feed properties -->
<bx:set feedProperties = {
    title: "My Blog",
    link: "https://myblog.com",
    description: "Latest posts from my blog",
    language: "en-us",
    pubDate: now(),
    generator: "BoxLang RSS Module"
} />

<!-- Create feed items -->
<bx:set feedItems = [
    {
        title: "First Post",
        link: "https://myblog.com/post1",
        description: "This is my first blog post",
        pubDate: now(),
        guid: "https://myblog.com/post1"
    },
    {
        title: "Second Post",
        link: "https://myblog.com/post2",
        description: "This is my second blog post",
        pubDate: dateAdd("d", -1, now()),
        guid: "https://myblog.com/post2"
    }
] />

<!-- Create the RSS feed -->
<bx:feed
    action="create"
    properties="#feedProperties#"
    data="#feedItems#"
    xmlVar="rssXml"
    outputFile="/feeds/myblog.xml"
    overwrite="true" />

<bx:output>
    <p>RSS feed created successfully!</p>
    <textarea rows="10" cols="80">#rssXml#</textarea>
</bx:output>
```

### Creating Feed from Query Data

```boxlang
<!-- Get blog posts from database -->
<bx:query name="blogPosts">
    SELECT title, slug, content, published_date, author
    FROM blog_posts
    WHERE published = 1
    ORDER BY published_date DESC
    LIMIT 20
</bx:query>

<!-- Map query columns to RSS fields -->
<bx:set columnMapping = {
    title: "title",
    link: "slug",  // Will be processed to create full URL
    description: "content",
    pubDate: "published_date",
    author: "author"
} />

<!-- Create feed properties -->
<bx:set feedProps = {
    title: "Company Blog",
    link: "https://company.com/blog",
    description: "Latest updates from our company blog"
} />

<!-- Create RSS feed from query -->
<bx:feed
    action="create"
    properties="#feedProps#"
    data="#blogPosts#"
    columnMap="#columnMapping#"
    xmlVar="blogRss"
    outputFile="/public/feeds/blog.xml"
    overwrite="true" />
```

### Creating Atom Feed

```boxlang
<!-- Create Atom feed instead of RSS -->
<bx:feed
    action="create"
    properties="#feedProperties#"
    data="#feedItems#"
    feedType="atom"
    xmlVar="atomXml"
    outputFile="/feeds/myblog.atom" />
```

### Using Name Attribute for Simplified Creation

```boxlang
<!-- All-in-one feed structure -->
<bx:set feedStruct = {
    title: "My Podcast",
    link: "https://mypodcast.com",
    description: "Weekly tech discussions",
    items: [
        {
            title: "Episode 1: Getting Started",
            link: "https://mypodcast.com/episode1",
            description: "Introduction to our podcast",
            pubDate: now()
        }
    ]
} />

<!-- Create feed using name attribute -->
<bx:feed
    action="create"
    name="#feedStruct#"
    xmlVar="podcastXml"
    outputFile="/feeds/podcast.xml" />
```

### Reading Local Feed File

```boxlang
<!-- Read feed from local file -->
<bx:feed
    action="read"
    source="/data/feeds/local-feed.xml"
    result="localFeed" />
```

### Creating Feed with Result Information

```boxlang
<!-- Create feed and get creation details -->
<bx:feed
    action="create"
    properties="#feedProperties#"
    data="#feedItems#"
    result="createResult"
    xmlVar="feedXml" />

<bx:output>
    <p>Feed Type: #createResult.feedType#</p>
    <p>Item Count: #createResult.itemCount#</p>
    <p>XML Size: #len(createResult.xml)# characters</p>
</bx:output>
```

## Output Variables

### Read Action Output

When using the read action, the component can populate multiple output variables:

#### `result` Variable Structure

```javascript
{
    items: [
        {
            title: "Item title",
            link: "Item URL",
            description: "Item content",
            pubDate: "Publication date",
            author: "Item author",
            categories: ["category1", "category2"],
            guid: "Unique identifier"
            // Additional fields based on extensions
        }
    ],
    channel: {
        title: "Feed title",
        link: "Feed URL",
        description: "Feed description",
        language: "Feed language",
        lastBuildDate: "Last update",
        generator: "Feed generator"
        // Additional metadata fields
    }
}
```

#### `properties` Variable (Channel Metadata Only)

Contains only the channel/feed metadata without the items array.

#### `query` Variable (Items Only)

Contains only the items array without the channel metadata.

#### `xmlVar` Variable

Contains the raw XML content as retrieved from the source.

### Create Action Output

#### `xmlVar` Variable

Contains the generated RSS/Atom XML as a string.

#### `result` Variable Structure (Create)

```javascript
{
    xml: "Generated XML content",
    feedType: "rss_2.0 or atom",
    itemCount: 10
}
```

## Usage Notes

### Read Action

- Supports RSS 2.0, RSS 1.0 (RDF), and Atom feeds
- Can read from HTTP/HTTPS URLs or local file paths
- Multiple output variables can be used simultaneously
- iTunes and Media RSS extensions provide additional metadata
- Use `maxItems` to limit memory usage for large feeds

### Create Action

- Generates RSS 2.0 or Atom feeds
- Accepts data as arrays of structs or query objects
- Use `columnMap` to map query columns to RSS fields
- Set `escapeChars=true` to escape special characters in content
- Can output to variable, file, or both

### File Operations

- Set `overwrite=true` to replace existing files
- Component will create parent directories if they don't exist
- File paths can be absolute or relative to the application root

## Related

- [RSS Function](../built-in-functions/RSS.md) - Simple BIF for reading RSS feeds
