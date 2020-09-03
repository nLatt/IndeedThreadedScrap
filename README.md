# Project to scrape ratings for [Lidl job offers](https://www.indeed.fr/cmp/Lidl/reviews)

## Libs to install:
Check requirements.txt

### Spider "rating_urls":
Is recursively scraping [Lidl job offers](https://www.indeed.fr/cmp/Lidl/reviews) to get all the different URLs of the rating pages since only a couple of ratings can be displayed per page

### Spider "ratings":
Is getting every rating of every url fetched by Spider "rating_urls". This includes the actual rating, title, comment, data about the rating (author, date, job, location) and pro/cons given by the author.

Coming features:
  - parallel processing
  - NLTK
  - processing/analyzing the scraped data (maybe)

note to self

relevant structure:
  <div cmp-Review-container>:
    <div cmp-Review-rating>:
      <div>:
        <div cmp-ReviewRating> get text

    <div cmp-Review-content>:
      <title>
      <author>
      <text>
      <pro con>
