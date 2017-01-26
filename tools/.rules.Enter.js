rules_onDecode = function(decode)
{
	decode.data = decode.data.replace(/\x54/g, "\x01X\x1ean//,\x04");
	return decode;
}
