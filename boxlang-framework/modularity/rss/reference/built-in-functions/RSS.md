# Function: `RSS`

Reads RSS feed from given URL(s) and returns structured feed data with items and channel metadata.

## Method Signature

```
RSS( urls, [filter], [maxItems], [itunes], [mediaRss], [userAgent], [timeout] )
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `urls` | string or array | Yes | URL or Array of URLs to read RSS feed from. Can be http(s) URLs or local file paths (file:/path/to/file) | |
| `filter` | function | No | A filter closure/lambda to filter feed items by certain criteria | `(i) -> true` |
| `maxItems` | numeric | No | Maximum number of items to return (0 = unlimited) | `0` |
| `itunes` | boolean | No | Parse iTunes podcast extensions | `false` |
| `mediaRss` | boolean | No | Parse Media RSS extensions for video/audio thumbnails | `false` |
| `userAgent` | string | No | Custom User-Agent string for HTTP requests | `""` |
| `timeout` | numeric | No | Timeout in seconds for HTTP requests | `25` |

## Examples

### Basic RSS Feed Reading

```javascript
// Read a simple RSS feed
feedData = RSS( "https://example.com/feed.xml" );

println( "Feed Title: " & feedData.channel.title );
println( "Found " & feedData.items.size() & " items" );

// Display first few items
feedData.items.each( ( item, index ) => {
    if ( index <= 3 ) {
        println( "- " & item.title );
        println( "  " & item.link );
    }
} );
```

### Reading Multiple Feeds

```javascript
// Read from multiple RSS feeds
urls = [
    "https://site1.com/feed.xml",
    "https://site2.com/rss.xml",
    "https://site3.com/atom.xml"
];

feedData = RSS( urls );
println( "Combined feeds have " & feedData.items.size() & " total items" );
```

### Using Filters and Limits

```javascript
// Filter items and limit results
feedData = RSS(
    urls = "https://news.example.com/feed.xml",
    filter = ( item ) => {
        // Only include items from last 7 days
        return item.pubDate > dateAdd( "d", -7, now() );
    },
    maxItems = 10
);

println( "Found " & feedData.items.size() & " recent items" );
```

### Reading Podcast Feeds with iTunes Extensions

```javascript
// Read podcast feed with iTunes metadata
podcastData = RSS(
    urls = "https://podcast.example.com/feed.xml",
    itunes = true,
    maxItems = 20
);

// Access iTunes-specific fields
podcastData.items.each( ( episode ) => {
    println( "Episode: " & episode.title );
    println( "Duration: " & episode.itunesDuration ?: "Unknown" );
    println( "Author: " & episode.itunesAuthor ?: "Unknown" );
    println( "Summary: " & episode.itunesSummary ?: "No summary" );
} );

// Channel iTunes metadata
println( "Podcast Category: " & podcastData.channel.itunesCategory ?: "Unknown" );
println( "Podcast Author: " & podcastData.channel.itunesAuthor ?: "Unknown" );
```

### Reading Media RSS with Thumbnails

```javascript
// Read video/media feed with Media RSS extensions
mediaFeed = RSS(
    urls = "https://video.example.com/feed.xml",
    mediaRss = true
);

mediaFeed.items.each( ( item ) => {
    println( "Title: " & item.title );

    // Access Media RSS fields
    if ( structKeyExists( item, "mediaThumbnailUrl" ) ) {
        println( "Thumbnail: " & item.mediaThumbnailUrl );
    }

    if ( structKeyExists( item, "mediaContentUrl" ) ) {
        println( "Media URL: " & item.mediaContentUrl );
    }
} );
```

### Custom HTTP Settings

```javascript
// Read feed with custom timeout and user agent
feedData = RSS(
    urls = "https://slow-server.com/feed.xml",
    userAgent = "MyApp/1.0 (BoxLang RSS Reader)",
    timeout = 60
);
```

### Local File Reading

```javascript
// Read RSS from local file
localFeed = RSS( "file:///path/to/local/feed.xml" );

// Or read multiple local files
localFeeds = RSS( [
    "file:///feeds/news.xml",
    "file:///feeds/blog.xml"
] );
```

## Return Value

The function returns a struct with two main keys:

### `items` (Array)

Array of feed items, each containing:
- `title` - Item title
- `link` - Item URL
- `description` - Item description/content
- `pubDate` - Publication date
- `author` - Item author
- `categories` - Array of categories
- `guid` - Unique identifier
- Additional fields based on feed type and extensions

### `channel` (Struct)

Feed metadata containing:
- `title` - Feed title
- `link` - Feed URL
- `description` - Feed description
- `language` - Feed language
- `lastBuildDate` - Last update date
- `generator` - Feed generator software
- Additional fields based on feed type and extensions

### iTunes Extension Fields

When `itunes=true`, additional fields are available:

**Channel Fields:**

- `itunesAuthor` - Podcast author
- `itunesCategory` - Podcast category
- `itunesImage` - Podcast artwork URL
- `itunesExplicit` - Explicit content flag
- `itunesSubtitle` - Podcast subtitle

**Item Fields:**

- `itunesAuthor` - Episode author
- `itunesDuration` - Episode duration
- `itunesExplicit` - Episode explicit flag
- `itunesSummary` - Episode summary
- `itunesTitle` - Episode title

### Media RSS Extension Fields

When `mediaRss=true`, additional fields are available:

**Item Fields:**

- `mediaThumbnailUrl` - Thumbnail image URL
- `mediaContentUrl` - Media file URL
- `mediaContentType` - Media MIME type
- `mediaPlayerUrl` - Media player URL

## Related

- [Feed Component](../components/Feed.md) - Full-featured component for reading and creating RSS/Atom feeds
