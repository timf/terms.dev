# terms.dev

This is the source repository for [terms.dev](https://terms.dev), a website dedicated
to one simple purpose: listing one, succinct definition for terms related to software
development. That's it!

Accepting PRs for new terms or changes to existing definitions.

Don't have time for a PR? Just tweet or DM me on Twitter 
([@peakscale](https://twitter.com/peakscale)). No problem.

You can also anonymously submit suggestions using [this Google Form](https://docs.google.com/forms/d/e/1FAIpQLSfieuAJJIg0uTc3GgowKBH74m6X2G7UiklBH0DfXjapsvY67w/viewform).

Happy to take any suggestions. They should be programming terms or things that software
developers use to build their products (libraries, databases, cloud services, dev tools,
etc.). Descriptions should be boring and short; remove adjectives like "best", "fast",
etc. For each major language, I am looking to have around 50-100 of the most popular
libraries.

Thanks!

## Adding new terms

You can manually create Markdown files in the `content` directory (see examples there).

Alternatively, you can run `./bin/add-one.py -t aterm -d adefinition` to auto-create
the file. This has other options, e.g. to add links or override the URL slug (which is
equal to the term by default).

Or you can run `./bin/add-many.py` which will intake a CSV or JSON file (see `-h`).

## Contributors

Thank you to all of our contributors!

* [Hillel Wayne](https://hillelwayne.com/)

## Building and running locally

This site is built with [Zola](https://www.getzola.org/).

After [installing Zola](https://www.getzola.org/documentation/getting-started/installation/),
go to the base directory and run `zola serve` to build the site and serve it locally.

Then navigate to [http://127.0.0.1:1111](http://127.0.0.1:1111)

It will auto-reload as you make changes.

## Text file generation

It's best to change the static files `static/terms.txt` and `static/terms.json` in the same
commit where a term was added or a definition was changed.
This is done via `./bin/generate-static.py`.

If you run `git config core.hooksPath .git-hooks` then `generate-static.py` will be run
automatically for you and the commit will fail if you hadn't run it yet and something changed.

## Licenses

Dual-licensed under MIT or the [UNLICENSE](https://unlicense.org).

The site is built with [Zola](https://getzola.org) and [Slim](https://github.com/jameshclrk/zola-slim).
Thank you to those project contributors. The original CSS and macros for the Slim theme
remain MIT and copyright the original authors.

The Google Cloud Platform definitions are modified versions of 
[google-cloud-4-words](https://github.com/gregsramblings/google-cloud-4-words) which has a
separate [license](https://github.com/gregsramblings/google-cloud-4-words/blob/master/LICENSE).
