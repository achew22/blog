Hello World
###########

:date: 2013-2-2 10:39
:tags: programming, GoSpotCheck
:category: programming
:parts: gospotcheck-architecture
:status: published

I just quit my job, 1 week ago in fact.
I've had a lot of time to think about it, and there were some things that didn't go well, but there were some things that really did.
I worked for a company called `GoSpotCheck <http://www.gospotcheck.com>`_ and helped them build one of the best systems I have ever had the pleasure to be involved with.

When I started doing web development, website design was static pages with all content fully loaded.
Everything was loaded through a portal, a phrase that I still don't fully understand.
After a few years, the world started to buzz about `progressive enhancement <http://wikipedia.org/wiki/Progressive_Enhancement>`_ for the web.
Major page navigation was still handled by making a full HTTP request.
This meant that most of a pages conten't didn't change during this process, making much of the "over the wire" unnecessary.
To combat this, many modern apps are written as `single page apps <http://wikipedia.org/wiki/Single_Page_Application>`_.
All assets are delivered upfront and the only governor on the speed of your application is the speed of the JS VM and your code.

This may sound familiar to many, many people.
It is even more familiar to people if I put it this way, "native application".
This application consumes a remote API and displays the content to the user.
Javascript is the native development language of the web.
How is that different from a mobile app?
We built a fantastic native application for the web.

I intend this blog to be a continued endeavor documenting projects I'm working on or have previously worked on. Next, I'm going to talk about `the backend <|filename|002_the_backend.rst>`_, the core of our architecture.