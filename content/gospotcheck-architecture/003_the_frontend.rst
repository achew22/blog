The Frontend
############

:date: 2013-3-10 10:39
:tags: programming, GoSpotCheck
:category: programming
:parts: gospotcheck-architecture
:status: published


The frontend worked so perfectly into `the backend <|filename|002_the_backend.rst>`_, I wrote about this last time,

The great thing about this set up is the decoupling it provided.
A lot of web apps rerender the whole page from scratch and therefore transmit their markup over and over again to the user.
Instead we transmitted our entire package of logic and templates in a single js file.
This file, which clocked in at :math:`\lt 200\,\textrm{kb}` thanks to Google Clousre Compiler's advanced mode, is hosted on `cloudfront <http://aws.amazon.com/cloudfront>`_ which made it super fast.

On top of using a CDN, every deployment of the application got a new url at the CDN.
This means that every time you loaded the page after the first time, the only request that was made was the single request to load the HTML that referenced our assets.
With this, and a few more tricks, we were able to get our page load time down even on junky connections to just a few tens of milliseconds.
According to our internal metrics, :math:`95%` of content arrived from our server in :math:`\lt 100\,\textrm{ms.}`
:math:`100\,\textrm{ms}` was about the worst lag anyone could possibly have experienced but we didn't stop there.
When we fetched data for every page, we preemptively loaded data for the next next screen so that it would already be available when the user clicked that link making the delay :math:`\textrm{sub-}10\,\textrm{ms}` on good browsers.

Deliverability aside, we wrote the application in Google's Closure Framework which provided us with the aforementioned compilation statistic.
This is an old framework that not only has `everything you could possible wish for <http://closure-library.googlecode.com/git/closure/goog/demos/index.html>`_, it also has `extremely thorough documentation <http://docs.closure-library.googlecode.com/git/index.html>`_.
They provide a framework which helps you through the creation of your `:abbr: RIA (Rich Internet Application)`.
