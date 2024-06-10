# Codebook Immersion Journal

Codebook for the file `immersion_journal.xlxs`. 

- The file is stored [here](#immersion-channel).

## Immersion Channel

### comment_id
- **Description**: A unique identifier for each comment in the immersion journal.
- **Type**: Integer
- **Example**: 1, 2, 3

### video_id
- **Description**: A unique identifier for each video in the immersion journal.
- **Type**: string
- **Example**: 'PpcISHuSCpo'

### published_at
- **Description**: Publication date and time of the comment.
- **Type**: date
- **Example**: 2023-05-07T18:59:15Z

### like_count
- **Description**: Like count of the published comment.
- **Type**: Integer
- **Example**: 20, 45, 100 (likes)

### Reflections
- **Description**: Reflections of the authors about the comment to learn about different claims.
- **Type**: string
- **Example**: 'An explanation on why CO2 is not resposnsible for global warming and therefore showing that the C02 which is emmited by us has no effect on the climate. The users is explaining it with enviromental areas everyone knows about to make the explanation as easy as possible.'

### super_claim
- **Description**: Claim of Each comment based on close reading.
- **Categories**:
    - 1 = Global warming is not happening
    - 2 = Human Greenhouse Gases are not causing global warming
    - 3	= Climate impacts are not bad
    - 4	= Climate solutions won't work
    - 5	= Climate movement/science is unreliable
    - 6	= Climate change is invented by the global elite
    - 7	= Appeal to authority or expert
    - 8 = Climate change explained through religion 
- **Type**: Integer
- **Example**: 1, 2, 3

### sub-claim
- **Description**: Sub-claim of Each comment based on close reading. 
- **Type**: Numeric
- **Example**: 4.2, 5.1, 2.3
- **Categories**:

| 1          | 2                                   | 3                       | 4                             | 5                       |
|------------|-------------------------------------|-------------------------|-------------------------------|-------------------------|
| 1.1 Ice isn't melting | 2.1 It's natural cycles       | 3.1 Sensitivity is low   | 4.1 Policies are harmful   | 5.1 Science is unreliable |
| 1.2 Heading into ice age | 2.2 Non-Greenhouse Gas forcings | 3.2 No species impact | 4.2 Policies are ineffective | 5.2 Movement is unreliable |
| 1.3 Weather is cold | 2.3 No evidence for Greenhouse Effect | 3.3 Not a pollutant | 4.3 Too hard | 5.3 Climate is conspiracy |
| 1.4 Hiatus in warming | 2.4 CO, not rising | 3.4 Only a few degrees | 4.4 Clean energy won't work | |
| 1.5 Oceans are cooling | 2.5 Emissions not raising CO2 levels | 3.5 No link to conflict | 4.5 We need energy | |
| 1.6 Sea level rise is exaggerated | | 3.6 No health impacts | | |
| 1.7 Extremes aren't increasing | | | | |
| 1.8 Changed the name | | | | |

### keywords
- **Description**: Important keywords found out during the explorative and focused coding. This helps us do understand the words used for different claims and gives us qualitative knowledge to build the classifier.
- **Type**: String
- **Example**: solar panel, green lifestlye, greeniacs, global elite
																	