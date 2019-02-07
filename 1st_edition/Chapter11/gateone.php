<?php
require_once dirname(__FILE__).'/include/config.inc.php';
$gateone = "gateone-hostname";

$hosts = API::Host()->get(array(
    "hostids" => $_GET['hostid'],
    "selectInterfaces" => "extend"));
$ssh_con_url = "";
if(isset($hosts[0]["interfaces"])){
        $ssh_con_url =get_ssh_interface($hosts[0]);
}

$user = CWebUser::$data['alias'];
$auth = get_authobj($user);

function get_ssh_interface($host){
    foreach( $host["interfaces"] as $interface ){
        if($interface["main"] == 1){
            $ssh_interface = $interface["useip"] == 0 ? $interface["dns"] : $interface["ip"];
            return $ssh_interface;
        }
    }
    return null;
}

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
        <script src="https://$gateone/static/gateone.js"></script>
        <script>
            function GateOneConnect(){
                GateOne.init({url: 'https://$gateone/',auth: $auth });
                setTimeout(function(){ OpenSSHConnection();},2000);
            }

            function OpenSSHConnection(init){
                GateOne.Bookmarks.openBookmark('ssh://$ssh_con_url');
                setTimeout(function(){GateOne.Visual.togglePanel();},10);
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
