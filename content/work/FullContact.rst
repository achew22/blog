FullContact (formerly RainMaker)
################################

:template: work
:category: work
:author: Andrew Z Allen
:logo: /static/work/images/fullcontact.svg
:date: 2011-06-03
:enddate: 2011-09-03
:position: Contractor
:languages: Python
:web_description: For FullContact, I implemented the first iteration of their python client.
:description: Implemented the Python client for FullContact's API.
:description2: Programmers using this API can obtain enriched information about users.
:workurl: https://github.com/fullcontact/fullcontact-api-python
:status: published
:resume: true
:website: true

Working for `FullContact <https://fullcontact.com>`_ I built the Full Contact `API client <https://github.com/fullcontact/fullcontact-api-python>`_ for python.

Code sample:

.. code-block:: python
    :linenos:

    import rainmaker
    rainmaker = rainmaker.RainMaker("API_KEY")
    print(rainmaker.do_lookup("lorangb@gmail.com"))

    # Output
    {
        "status": 200,
        "contactInfo": {
            "familyName": "Lorang",
            "givenName": "Bart",
            "fullName": "Bart Lorang",
            "emailAddresses":
            [
            "lorangb@gmail.com"
            ]
        },
        "interests": {
            "Football": true,
            "Sports & Recreation": true,
            "Business": true,
            "Online News": true,
            "Baseball": true,
            "Tennis": true,
            "News & Current Events": true,
            "Basketball": true,
            "Blogging": true,
            "Social Networks": true,
            "Online Journals": true,
            "Golf": true,
            "Technology": true
        },
        "organizations": [
            {
                "name": "Forseti Holdings, LLC",
                "title": "Chairman & CEO",
                "startDate": "2010-01"
            },
            {
                "name": "Rainmaker Technologies",
                "title": "CEO",
                "startDate": "2010-01"
            },
            {
                "name": "Forseti Holdings LLC",
                "title": "Chairman & CEO",
                "isPrimary": true
            },
            {
                "name": "CloudCenter LLC",
                "title": "Chairman & CEO",
                "isPrimary": false
            },
            {
                "name": "DTS",
                "isPrimary": false
            }
        ],
        "demographics": {
            "influencerScore": "81-90",
            "householdIncome": "250k+",
            "age": "31",
            "homeOwnerStatus": "Own",
            "locationGeneral": "Denver, Colorado, United States",
            "children": "No",
            "gender": "Male",
            "maritalStatus": "Single"
        },
        "socialProfiles": [
            {
                "type": "facebook",
                "url": "http://www.facebook.com/bart.lorang",
                "id": "651620441",
                "birthday": "08/16/1979",
                "username": "bart.lorang"
            },
            {
                "url": "http://twitter.com/lorangb",
                "id": "5998422",
                "type": "twitter",
                "username": "lorangb"
            },
            {
                "url": "http://www.linkedin.com/in/bartlorang",
                "id": "bartlorang",
                "type": "linkedin",
                "username": "bartlorang"
            },
            {
                "url": "http://about.me/lorangb",
                "type": "about.me"
            },
            {
                "url": "http://www.flickr.com/people/39267654@N00/",
                "id": "39267654@N00",
                "type": "flickr"
            },
            {
                "url": "http://profiles.friendster.com/6986589",
                "type": "friendster"
            },
            {
                "url": "https://profiles.google.com/lorangb",
                "id": "lorangb",
                "type": "google profile",
                "username": "lorangb"
            },
            {
                "url": "http://www.myspace.com/137200880",
                "type": "myspace"
            },
            {
                "url": "http://picasaweb.google.com/lorangb",
                "type": "picasa"
            },
            {
                "url": "http://tungle.me/bartlorang",
                "id": "bartlorang",
                "type": "tungle.me",
                "username": "bartlorang"
            },
            {
                "url": "http://youtube.com/lorangb",
                "type": "youtube"
            },
            {
                "type": "friendster",
                "url": "http://profiles.friendster.com/6986589"
            }
        ],
        "photos": [
            {
                "url": "http://graph.facebook.com/<snip>",
                "type": "facebook"
            },
            {
                "url": "https://lh5<snip>",
                "type": "google profile"
            },
            {
                "url": "http://profile<snip>",
                "type": "facebook"
            },
            {
                "url": "http://photos.friendster.com<snip>",
                "type": "friendster"
            },
            {
                "url": "http://c2.ac-images<snip>",
                "type": "myspace"
            },
            {
                "url": "http://images.plaxo.com/<snip>",
                "type": "plaxo"
            },
            {
                "url": "http://a1.twimg.com/<snip>",
                "type": "twitter"
            },
            {
                "type": "gravatar",
                "url": "https://secure.gravatar.com/<snip>"
            },
            {
                "type": "linkedin",
                "url": "http://media.linkedin.com/<snip>"
            }
        ]
    }