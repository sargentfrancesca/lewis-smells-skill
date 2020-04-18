Feature: lewis-smells

  Scenario: What does lewis smell like
    Given an english speaking user
     When the user says "What does lewis smell like"
     Then "lewis-smells" should contain "Lewis smells like <scents>"
    
    Examples: smells examples  # Table heading
        | scents   |   # Column heading
        |Lush dirty spray|
        |Beard oil|
        |Hash browns|
        |Milk chocolate|
        |jose mourinho|
        |solder|
        |clocks|
        |wet dog|
        |palmolive soap|
        |orange lucozade|
        |original lucozade|
        |his grey blanket|
        |fried chicken|
        |bed slobber|
        |a lovely bit of squirrel|
        |tangfastics|
        |a really long sit down shower|
        |lawnmower oil|
        |hotel chocolat rocky road|
        |the space bar after playing football manager for 3 hours|
        |cheese wraps|