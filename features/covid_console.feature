Feature: Getting table with Covid data

  Scenario Outline: Get covid data and write it to the file
    When we run 'covid.py' for the "<country>" and specify filename "<file>"
    Then the table is written into a "<file>"
    And table is not empty (contains more than 4 rows)
    And table contains "<country>"


    Examples:
      | country                                               | file         |
      | "United States of America" "Russian Federation" Japan | US_covid.txt |
      | "Russian Federation"                                  | RF_covid.txt |
      | Japan                                                 | JP_covid.txt |
      | China Japan Singapore                                 | Global.txt   |


  Scenario Outline: Get covid data and print it out to the screen
    When we run 'covid.py' for the "<country>"
    Then we get the table on the screen
    And table is not empty (contains more than 4 rows)
    And table contains "<country>"

    Examples:
      | country                                         |
      | Canada                                          |
      | Ukraine Belarus                                 |
      | "United States of America" "Russian Federation" |


