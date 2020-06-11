*** Settings ***
Library    RequestsLibrary
Library    Collections



*** Test Cases ***
Get Requests
    [Documentation]   普通GET请求
    Create Session    api    http://ws.webxml.com.cn/WebServices
    ${params}=        Create Dictionary    theRegionCode=3113
    ${resp}=          Get Request          api    /WeatherWs.asmx/getSuportCityString     params=${params}
    Should Be Equal As Strings    ${resp.status_code}    200

POST Requests
    [Documentation]   POST请求json
    Create Session    api    http://120.196.233.14:33200
    ${header}=        Create Dictionary    Content-Type=application/json
    ${json}=          set variable    {"authenticateBasic": {"connectType": 1,"asDefaultProfile": 0,"userType": 3,"clientPasswd": "Huawei@123","authType": 0,"autoRegister": 0,"userID": "guestusr"},"authenticateTolerant": {"subnetID": "8602"},"authenticateDevice": {"deviceModel": "VR_glass"}}
    ${resp}=          post request          api    /VSP/V3/Authenticate     header=${header}    json=${json}
    Should Be Equal As Strings    ${resp.status_code}    200

