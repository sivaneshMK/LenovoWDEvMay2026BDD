Feature: Unlock User

  @wip
  Scenario: Verify User can able to unlock the account
    Given launch the application
    When user enter name, email, and country
    And select terms and conditions check box
    And click on unlocak offer
    Then validate  full name, email id. section


  Scenario Outline: Verify user is able to search a product
    Given launch the application
    When enter "<product_name>" in search box

    Examples:
    | product_name |
    | Monitor      |
    | Key Board    |
    | laptop       |

