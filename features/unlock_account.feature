Feature: Unlock User

#  Background:
#    Given launch the application


  Scenario: Verify User can able to unlock the account

    When user enter name, email, and country
    And select terms and conditions check box
    And click on unlocak offer
    Then validate  full name, email id. section

  @abc
  Scenario Outline: Verify user is able to search a product
    When enter "<product_name>" in search box
    And enter "<username>" "<password>"

    Examples:
    | product_name |username|password|
    | Monitor      | sivanesh | sivanesh@123|
    | Key Board    | Karthic  | Karthic@123|
    | laptop       | Nithya   | Nithya     |

  @wip
  Scenario: Login with valid credentials

    Given user credentials
      | sivanesh | sivanesh@123|
      | Karthic  | Karthic@123|
      | Nithya   | Nithya     |