rules_onDecode = function(a)
{
	a.data = a.data.replace(/~t/g,"\x01X\x1ean//t\x04");
	a.data = a.data.replace(/~d/g, "\x01X\x1ean//,\x04");
  a.data = a.data.replace(/~e/g, "\x01X\x1ean//n\x04");
	return a;
};
