rules_onDecode = function(a)
{
	a.data = a.data.replace(/\x09/g,"\x01X\x1ean//t\x04");
	a.data = a.data.replace(/delay500ms/g, "\x01X\x1ean//,\x04");
  a.data = a.data.replace(/enter_key/g, "\x01X\x1ean//n\x04");
  a.data = a.data.replace(/down_arrow/g, "\x01X\x1ean//d\x04");
	return a;
};
