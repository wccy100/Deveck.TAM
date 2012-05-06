# $Id: 999_message_no_body.py 2086 2008-06-28 00:39:58Z bennylp $
import inc_sip as sip
import inc_sdp as sdp

# There's some report that incoming MESSAGE without body will crash pjsua
#
complete_msg = \
"""MESSAGE sip:localhost SIP/2.0
Via: SIP/2.0/UDP 192.168.0.14:5060;rport;branch=z9hG4bKPj9db9
Max-Forwards: 70
From: <sip:192.168.0.14>;tag=08cd5bfc2d8a4fddb1f5e59c6961d298
To: <sip:localhost>
Call-ID: 3373d9eb32aa458db7e69c7ea51e0bd7
CSeq: 23809 MESSAGE
Contact: <sip:192.168.0.14:5060>
User-Agent: PJSUA v0.8.0-trunk/win32
Content-Type: text/plain
Content-Length: 50
"""


sendto_cfg = sip.SendtoCfg( "empty MESSAGE", "--null-audio --auto-answer 200", 
			    "", 488, complete_msg=complete_msg)
