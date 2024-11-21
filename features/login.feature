Feature: Login
    As a user I want to log in to my account
    so that I can access different features


Scenario: Valid Login
    Given I am in the login page
    When I enter the credentials and click on login button
    Then homepage should be displayed with valid text
