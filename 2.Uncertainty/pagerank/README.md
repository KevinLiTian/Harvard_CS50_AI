# PageRank

## Background

When search engines like Google display search results, they do so by placing more “important” and higher-quality pages higher in the search results than less important pages. But how does the search engine know which pages are more important than other pages?

One heuristic might be that an “important” page is one that many other pages link to, since it’s reasonable to imagine that more sites will link to a higher-quality webpage than a lower-quality webpage. We could therefore imagine a system where each page is given a rank according to the number of incoming links it has from other pages, and higher ranks would signal higher importance

But this definition isn’t perfect: if someone wants to make their page seem more important, then under this system, they could simply create many other pages that link to their desired page to artificially inflate its rank

For that reason, the PageRank algorithm was created by Google’s co-founders (including Larry Page, for whom the algorithm was named). In PageRank’s algorithm, a website is more important if it is linked to by other important websites, and links from less important websites have their links weighted less. This definition seems a bit circular, but it turns out that there are multiple strategies for calculating these rankings

## Random Surfer Model

This method is similar to using sampling to get a general probability. The AI randomly selects one from all the pages, then randomly choose from one of the links in the current page and goes to the next. By sampling a large amount (10000) of samples, the AI will then see how many times it visited each page and calculate the probability of visiting each page based on this

But this method itself might be problematic in some situations. Consider this:

The pages 5 and 6 only link to each other, which means that if the AI initially selects one of these two pages, then it will only visit page 5 and 6 over and over again, and page 1 - 4 will never be visited. A solution to this is to add a damping factor (d), which itself is a probability (usualy set at 0.85). It means 85% of times, the AI will follow the links to the next page, but 15% of times, the AI will randomly select one page from all the pages (including the current page)

## Iterative Algorithm

Using Random Surfer Model (sampling) to get a general probability is a good method, but there is another method that is mathematically more accurate, the iterative algorithm. This method calculates the probability of visiting a page using the following mathematic formula:

PR(p) represents the page rank, which is also the probability of getting visited. d is the damping factor, and N is the total number of pages so the first term stands for the probability of a page to be selected at random. The second term is the probability of a page to be selected through links in other pages

## Files

There are three set of sample pages in folders _corpus0_, _corpus1_ and _corpus2, and a main file _pagerank.py_. In _pagerank.py_, there are two constants, the damping factor (d=0.85) and the sample size (N=10000). The main function takes in arguments specifying which set of pages the program will be using and pass them into two functions, the _sample_pagerank_ and the _iterate_pagerank_. They uses the Random Surfer Model and the Iterative Algorithm respectively

## Example Output

```Python
$ python pagerank.py corpus0
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307
```
