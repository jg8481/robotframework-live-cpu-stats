*** Test Cases ***
First Test Case
    Sleep   1s
    Log   Done

Second Test Case
    Sleep   1s
    Log   Done

Third Test Case
    Sleep   1s
    Log   Done

Fourth Test Case
    :FOR   ${index}   IN RANGE   1   5
        \   My Log To Check

*** Keywords ***
My Log To Check
    Log   Dummy