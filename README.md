# Project to scrape ratings for [Lidl job offers](https://www.indeed.fr/cmp/Lidl/reviews)

## Libs to install:
Check requirements.txt

### Spider "rating_urls":
Is recursively scraping [Lidl job offers](https://www.indeed.fr/cmp/Lidl/reviews) to get all the different URLs of the rating pages since only a couple of ratings can be displayed per page

### Spider "ratings":
******explanation******

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
