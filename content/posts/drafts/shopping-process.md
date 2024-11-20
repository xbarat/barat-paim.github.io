# shopping process

user name is "Joey"

Joey is a 32 year old female, earns $100k per year, and lives in New York.
Joey loves clothes shopping, and is always looking for the best deals, or the best quality, or something unique.

This is the shopping process of Joey.
## She goes to the online stores of her favorite brands with a clothing in mind. Lets say a dress.
## She browses the online stores and keeps taking screenshots of the dresses she likes.
## She goes to different stores, and takes screenshots over different points of time in her day.
## She does this for a few days, whenever she has time.
## She goes over the screenshots to compare the dresses.
## She hasn't made her mind yet, she wants to check if she can get the same dress at cheaper stores.
## She image searches, or google searches the dress, to see if she can find the same dress.
## She takes the screenshots of these dresses too.
## If she doesn't find cheaper deals, she buys the dress from the store she liked the most.
## If she finds cheaper deals, she buys the dress from the cheapest store.

How do we automate this process? What are the biggest challenges she faces? What parts she enjoys? What parts she doesn't?
So, based on the above process, we can observe the following:
1. Screenshot is her tool to remember the dress. She doesn't use add to cart, or wishlist, or save for later.
2. She mentally compares the dresses
3. Discovery phase is longer than the decision phase
4. She probably enjoys the discovery phase, as she takes more time to decide.

When asked, she said she would like image search to a part of this process she doesn't enjoy,
and hence we should help her with that.

Jobs to be done:
1. Help her discover the dress based on the screenshots she has taken.
2. Active image search to find similar dresses on the internet.
3. Continuous image search to find the best deals.

Use her screenshots to discover the dress, and provide her a list of dresses she might like.
The screenshots become our prompt or input to the LLM, and the describes the dress in detail as output, and then we can use that to search the internet for similar dresses.

Finding Limitations in Current Solutions:
1. Google Image Search
2. Google Search