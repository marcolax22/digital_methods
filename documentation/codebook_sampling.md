# Codebook Channel Sampling

Codebook for the file `channel_sampling.xlxs`. 

- The file is stored here.

## General Information
 Our selection criteria for sampling the given channels were based on qualitative measures which included the ammounts of comments, videos that cover climate change (specifically climate contrarianism), and the number of up-to date videos.

## Channel Sampling Variables

### id
- **Description**: A unique identifier for each channel.
- **Type**: Integer
- **Example**: 1, 2, 3

### channel
- **Description**: The name of the YouTube channel.
- **Type**: String
- **Example**: "Blaze TV", "Jordan B Peterson"

### subscriber
 - **Description**: The number of subscribers to the channel.
- **Type**: Integer
- **Example**: 10000, 500000

### number_of_videos
- **Description**: The total number of videos uploaded by the channel.
- **Type**: Integer
- **Example**: 50, 1200

### information
- **Description**: Additional information about the channel.
- **Type**: String
- **Example**: "Channel XY is a channel about the denial of climate change and environmental issues."

### activity_on_climate
- **Description**: The channel's level of activity related to climate change topics. This column provides a qualitative measure of the channel's engagement with climate-related content.
- **Type**: String
- **Example**: "High", "Medium", "Low"

### category
- **Description**: The broader category to which the channel belongs.
- **Type**: String
- **Example**: "Podcaster", "News"

### based_in
- **Description**: The geographical location where the channel is based.
- **Type**: String
- **Example**: "USA", "UK", "Australia"

### choose
- **Description**: Indicates if the channel has been chosen for the study.
- **Type**: Binary
- **Example**: 1, 0

### choose_not
- **Description**: Indicates why the channel was not taken as part of our study.
- **Type**: String
- **Example**: "not based in the US", "too old videos"

### addtiional_terms
- **Description**: Any additional terms or keywords associated with the channel for defining our search query
- **Type**: String
- **Example**: "renewable energy", "wildfires", "climate alarmism"

### channel_id
- **Description**: The unique identifier assigned to the channel by YouTube.
 - **Type**: String
- **Example**: "UC1234567890", "UC0987654321"

### scraped
 - **Description**: Indicates if the channel's data has been scraped.
- **Type**: Binary
- **Example**: 1, 0

### scraped_comments
- **Description**: Indicates if the comments from the channel's videos have been scraped.
- **Type**: Binary
- **Example**: 1, 0

### and_or
- **Description**: Specifies the logical operation used for filtering the videos of each channel. Depending if the channel is specialising on climate change or conservative news in general the logical operation is different.
- **Type**: String
- **Example**: "AND", "OR"