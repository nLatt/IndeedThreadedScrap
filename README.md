# Project to scrape ratings for [Lidl job offers](https://www.indeed.fr/cmp/Lidl/reviews)

## Libs to install:
Check requirements.txt

### Spider "rating_urls":
Is recursively scraping [Lidl job offers](https://www.indeed.fr/cmp/Lidl/reviews) to get all the different URLs of the rating pages since only a couple of ratings can be displayed per page

### Spider "ratings":
Is getting every rating of every url fetched by Spider "rating_urls". This includes the actual rating, title, comment, data about the rating (author, date, job, location) and pro/cons given by the author.

### Parallel processing:
With 4 cores parallel processing sped up the program by around 1/3 of the duration, the time for scraping 6400 reviews has been reduced from 28s to 15s, since I need to load webpages the process cant be one fourth of the speed, unless the bandwidth isn't bottlenecking anymore.
