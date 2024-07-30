# freelanceScraper1

This was my first paid job. It is a Crawler to automate basic Search Engine Optimization on a WordPress admin Page.
Because there were 800 products it would have been a pain for my Customer to Optmize it by Hand.

The Main goal here was, for each product, to find the "Keyword" of the product with the highest score.

I.e The Product "STIHL elektrischer Rasenmäher"
the word elektrischer would probably be the highest score when choosen as a keyword. Keywords will be highlighted by the Search Engine.

The try_keywords method in crawler.py tries every possible keyword that a product name has.

"STIHL elektrischer Rasenmäher" would test:
- STIHL elektrischer Rasenmäher
- STIHL elektrischer
- elektrischer Rasenmäher
- STIHL
- elektrischer
- Rasenmäher
