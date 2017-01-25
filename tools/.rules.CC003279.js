/* Filename:   .rules.CC003279.js
 * Description: Replace all %09 with TAB keystroke - non-symbology specific
 * Copyright:   2014 The Code Corporation.
 * $Title: .rules.CC003279.js$
 * $Revision: 865 $
 * $Date: 2014-10-16 11:56:32 -0600 (Thu, 16 Oct 2014) $
 * $Author: val.jensen $
 * $HeadURL: https://codesvn/svn/Rules/.rules.CC003279.js $
 */

rules_onDecode = function(a)
{
	a.data = a.data.replace(/\x09/g, "\x01X\x1ean//t\x04");
	return a;
}
