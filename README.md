# terms.dev

This is the source repository for [terms.dev](https://terms.dev), a website dedicated to one
simple purpose: listing one, succinct definition for software terms. That's it!

Taking PRs - happy to take suggestions which is why I made this repository public.

Don't have time for that? Just tweet or DM me on Twitter
([@peakscale](https://twitter.com/peakscale)). No problem.

Thanks!

## Building and running locally

This site is built with [Zola](https://www.getzola.org/).

After [installing Zola](https://www.getzola.org/documentation/getting-started/installation/), go
to the base directory and run `zola serve` to build the site and serve it locally.

Then navigate to [http://127.0.0.1:1111](http://127.0.0.1:1111)

It will auto-reload as you make changes.

## Adding new terms

You can manually create Markdown files in the `content` directory (see examples there).

Alternatively, you can run `bin/add-one.py -t aterm -d adefinition` to auto-create the file.
This has other options, e.g. to add links or override the URL slug (which is equal to the term
by default).

## Contributors

Thank you to all of our contributors!

* [Hillel Wayne](https://hillelwayne.com/)

## License

Dual-licensed under MIT or the [UNLICENSE](https://unlicense.org).

The site is built with [Zola](https://getzola.org) and [Slim](https://github.com/jameshclrk/zola-slim).
Thank you to those project contributors. The original CSS and macros for the Slim theme remain MIT
and copyright the original authors.
