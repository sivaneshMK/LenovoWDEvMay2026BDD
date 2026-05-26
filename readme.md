Gherkin keywords 
    Given
    When
    And
    Then
    But

Feature file

Feature: 

Background:

Scenario/scenario outline: Test name
    Given precondition
    When Step(action) enter username, password, click on login button
    Then Validation and verification

Example:
        Data Table
        |username|password|
        |abdissivanesh|abcdefghijklmno|


Design patterns:

design patterns are used to handle the common things
like object, and pages

object manager
page factory 
single tone
POM
Lazy page object patern
Dependency injections


Predefined fixture
===================
request --> access current test /scenario context
pytestbdd_stepdef_given --> current given step
pytestbdd_stepdef_when
pytestbdd_stepdef_then
pytestdbb_stepfunc_args --> access resolved step arguments
pytestbdd_step_params --> scenario outline example values
pytestdbb_step_name --> current step name
pytestbdd_scenario --> current scenario
pytestbdd_feature_base_dir --> base feature directory

