*** Test Cases ***
First Test Case 1
    Sleep   1s
    Log   Done

Second Test Case 2
    Sleep   1s
    Log   Done

Third Test Case 3
    Sleep   1s
    Log   Done

Fourth Test Case 4
    :FOR   ${index}   IN RANGE   1   5
        \   My Log To Check

*** Keywords ***
My Log To Check
    Log   Dummy