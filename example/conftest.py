import pytest


@pytest.fixture
def historical_fact_response():
    return {
      "date": "November 11",
      "url": "https://wikipedia.org/wiki/November_11",
      "data": {
        "Events": [
          {
            "year": "308",
            "text": "At Carnuntum, Emperor emeritus Diocletian confers with "
                    "Galerius, Augustus of the East, and Maximianus, the "
                    "recently returned former Augustus of the West, in an "
                    "attempt to end the civil wars of the Tetrarchy.",
            "html": "At <a href=\"https://wikipedia.org/wiki/Carnuntum\" "
                    "title=\"Carnuntum\">Carnuntum</a>, Emperor <i>emeritus"
                    "</i> <a href=\"https://wikipedia.org/wiki/Diocletian\""
                    " title=\"Diocletian\">Diocletian</a> confers with <a "
                    "href=\"https://wikipedia.org/wiki/Galerius\" "
                    "title=\"Galerius\">Galerius</a>, <i><a "
                    "href=\"https://wikipedia.org/wiki/Augustus_(honorific)"
                    "\" title=\"Augustus (honorific)\">Augustus</a></i> of "
                    "the East, and <a href=\"https://wikipedia.org/wiki/"
                    "Maximian\" title=\"Maximian\">Maximianus</a>, the "
                    "recently returned former <i>Augustus</i> of the West, "
                    "in an attempt to end the <a "
                    "href=\"https://wikipedia.org/wiki/"
                    "Civil_wars_of_the_Tetrarchy\" title=\"Civil wars of the"
                    " Tetrarchy\">civil wars of the Tetrarchy</a>.",
            "links": [
              {
                "title": "Carnuntum",
                "link": "https://wikipedia.org/wiki/Carnuntum"
              },
              {
                "title": "Diocletian",
                "link": "https://wikipedia.org/wiki/Diocletian"
              },
              {
                "title": "Galerius",
                "link": "https://wikipedia.org/wiki/Galerius"
              },
              {
                "title": "Augustus (honorific)",
                "link": "https://wikipedia.org/wiki/Augustus_(honorific)"
              },
              {
                "title": "Maximian",
                "link": "https://wikipedia.org/wiki/Maximian"
              },
              {
                "title": "Civil wars of the Tetrarchy",
                "link": "https://wikipedia.org/wiki/Civil_wars_of_the_Tetrarchy"  # noqa
              }
            ]
          }
        ],
        "Births": [
          {
            "year": "990",
            "text": "Gisela of Swabia, Queen consort of Germany and Empress "
                    "consort of the Holy Roman Empire (d. 1043)",
            "html": "<a href=\"https://wikipedia.org/wiki/Gisela_of_Swabia"
                    "\" title=\"Gisela of Swabia\">Gisela of Swabia</a>, "
                    "Queen consort of Germany and Empress consort of the Holy "
                    "Roman Empire (d. 1043)",
            "links": [
              {
                "title": "Gisela of Swabia",
                "link": "https://wikipedia.org/wiki/Gisela_of_Swabia"
              }
            ]
          }
        ],
        "Deaths": [
          {
            "year": "405",
            "text": "Arsacius of Tarsus, Tarsian archbishop (b. 324)",
            "html": "<a href=\"https://wikipedia.org/wiki/Arsacius_of_Tarsus"
                    "\" title=\"Arsacius of Tarsus\">Arsacius of Tarsus</a>, "
                    "Tarsian archbishop (b. 324)",
            "links": [
              {
                "title": "Arsacius of Tarsus",
                "link": "https://wikipedia.org/wiki/Arsacius_of_Tarsus"
              }
            ]
          }
        ]
      }
    }
