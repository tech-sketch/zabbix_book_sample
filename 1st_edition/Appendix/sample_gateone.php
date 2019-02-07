<?php
$auth = get_authobj("test-user");
$gateone_hostname = "gateone-hostname";
function get_authobj($upn){
    $secret = 'シークレットキー';
    $api_key = 'APIキー';
    $authobj = array(
        'api_key' => $api_key,
        'upn' => $upn,
        'timestamp' => (string)ceil(microtime(true)*1000),
        'signature_method' => 'HMAC-SHA1',
        'api_version' => '1.0'
    );
    $authobj['signature'] = hash_hmac('sha1', $api_key.$upn.$authobj['timestamp'], $secret);
    return json_encode($authobj);
}
print<<<EOF
<html>
    <head>
        <script src="https://$gateone_hostname/static/gateone.js"></script>
        <script>
            function GateOneConnect(){
                GateOne.init({url: 'https://$gateone_hostname/',auth: $auth });
           }
        </script>
    </head>
    <body onLoad="GateOneConnect();">
        <div style="width: 1024px; height: 800px;">
            <div id="gateone"></div>
        </div>
    </body>
</html>
EOF;
?>

