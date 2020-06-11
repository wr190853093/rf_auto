*** Settings ***
#Library      RequestsLibrary
#Library      Collections
Variables    Variables/cvr214.py
Resource     Cases/cvr214.robot
#Suite Setup
#Test Template    getCategoryList_case


*** Test Cases ***
biClientLoginoutReport_login
    biClientLoginoutReport_case     ${domain_test}      ${Valid_biClientLoginout_header}     ${Valid_biClientLoginout_body}

biHeartclientUserHeart_case
    FOR    ${n}    IN RANGE     16
        log to console   第${n+1}次发起心跳
        Run Keyword If  ${n}<=14    biHeartclientUserHeart_case     ${domain_test}      ${Valid_biHeartclientUserHeart_header}     ${Valid_biHeartclientUserHeart_body}   1000   3
        ...      ELSE    biHeartclientUserHeart_case     ${domain_test}      ${Valid_biHeartclientUserHeart_header}     ${Valid_biHeartclientUserHeart_body}   1000   9
    END


biClientLoginoutReport_logout
    biClientLoginoutReport_case     ${domain_test}      ${Valid_biClientLoginout_header}     ${Valid_biClientLoginout_logout_body}

biHeartclientUserHeart_heartinvalid
    biHeartclientUserHeart_case     ${domain_test}      ${Valid_biHeartclientUserHeart_header}     ${Valid_biHeartclientUserHeart_body}   1001   3

biVideoOperationReport_valid
    biVideoOperationReport_case     ${domain_test}      ${Valid_biClientLoginout_header}     ${biVideoOperationReport_valid}
        Should Be Equal As Strings    ${code}    ${assert}