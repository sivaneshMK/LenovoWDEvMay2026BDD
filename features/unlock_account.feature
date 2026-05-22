Feature: Unlock User

  @wip
  Scenario: Verify User can able to unlock the account
    Given launch the application
    When user enter name, email, and country
    And select terms and conditions check box
    And click on unlocak offer
    Then validate  full name, email id. section