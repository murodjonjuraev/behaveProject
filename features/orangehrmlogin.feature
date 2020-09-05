Feature: OrangeHRM Login

  Scenario: Login to rangeHRM with valid parameters
    Given Launch Chrome browser
    When Open orangeHRM homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page

  Scenario Outline: Login to OrangeHRM with multiple parameters
    Given Launch Chrome browser
    When Open orangeHRM homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin321 |
      | adminxyz | admin123 |
      | admin    | admin321 |