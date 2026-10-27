#!/usr/bin/env python3
"""Put the theme loader and the hidden theme picker into a page.

Usage: python3 tools/add_theming.py rulebook.html
Idempotent: earlier theme scripts are stripped before they are re-added.

The themes are stylesheets in style/themes/; with none, the page keeps the
original look from style/base.css. The scripts are written into each page rather
than loaded from a .js file, so that they work when the page is opened straight
from disk. The page marks its title with data-theme-unlock: five quick clicks on
it show the picker. The choice is kept in localStorage, which every page shares,
and applies to the screen only unless the picker's "Print it too" box is ticked;
then the theme prints as well, and html[data-theme-print] tells the page's own
print rules (the rulebook's white cover) to step aside.
"""
import json
import re
import sys

# (file name in style/themes/, label in the picker). "original" is no theme.
THEMES = [
    ("original", "Original"),
    ("imperial", "Imperial"),
    ("lisafrank", "Trapper Keeper"),
    ("pocket", "Pocket Monsters"),
    ("geocities", "GeoCities"),
    ("taxform", "Form 1969-EZ"),
    ("terminal", "Terminal"),
    ("manuscript", "Manuscript"),
    ("vaporwave", "Vaporwave"),
]

LOAD = """<script id="theme-load">
/* Apply the saved theme before the page draws (tools/add_theming.py). */
(function(){
var t,p,q=/[?&]theme=(\\w+)/.exec(location.search);
try{t=localStorage.getItem('dynasty-theme');p=localStorage.getItem('dynasty-theme-print')==='1'}catch(e){}
/* ?theme=name&print=1 for testing, and for printing from a fresh browser */
if(q){t=q[1];p=/[?&]print=1/.test(location.search);}
if(t&&%s.indexOf(t)>0){
  document.write('<link rel="stylesheet" id="theme-css" media="'+(p?'all':'screen')+'" href="style/themes/'+t+'.css">');
  document.documentElement.setAttribute('data-theme',t);
  if(p)document.documentElement.setAttribute('data-theme-print','');
}
})();
</script>
"""

PICK = """<script id="theme-pick">
/* Five quick clicks on the title show the theme picker (tools/add_theming.py). */
(function(){
var T=%s,title=document.querySelector('[data-theme-unlock]'),n=0,last=0;
if(!title)return;
title.addEventListener('click',function(){
  var now=Date.now();
  n=now-last<500?n+1:1;last=now;
  if(n>=5){n=0;show();}
});
function set(t){
  var l=document.getElementById('theme-css');
  if(t==='original'){if(l)l.parentNode.removeChild(l);document.documentElement.removeAttribute('data-theme');}
  else{
    if(!l){l=document.createElement('link');l.rel='stylesheet';l.id='theme-css';l.media=media();document.head.appendChild(l);}
    l.href='style/themes/'+t+'.css';document.documentElement.setAttribute('data-theme',t);
  }
  try{localStorage.setItem('dynasty-theme',t)}catch(e){}
  mark();
}
/* data-theme-print tells the page's own print rules to step aside for the theme */
function mark(){
  var h=document.documentElement;
  if(printing()&&document.getElementById('theme-css'))h.setAttribute('data-theme-print','');
  else h.removeAttribute('data-theme-print');
}
/* themes are for the screen unless "Print it too" is ticked */
function printing(){try{return localStorage.getItem('dynasty-theme-print')==='1'}catch(e){return false}}
function media(){return printing()?'all':'screen';}
function setPrint(on){
  try{localStorage.setItem('dynasty-theme-print',on?'1':'0')}catch(e){}
  var l=document.getElementById('theme-css');if(l)l.media=media();
  mark();
}
function show(){
  try{getSelection().removeAllRanges()}catch(e){}
  if(document.querySelector('.theme-pick'))return;
  var box=document.createElement('div'),sel=document.createElement('select'),x=document.createElement('button');
  box.className='theme-pick';box.innerHTML='<span>Theme</span>';
  T.forEach(function(o){var op=document.createElement('option');op.value=o[0];op.textContent=o[1];sel.appendChild(op);});
  sel.value=document.documentElement.getAttribute('data-theme')||'original';
  sel.addEventListener('change',function(){set(sel.value);});
  x.type='button';x.textContent='\\u00d7';x.setAttribute('aria-label','Close');
  x.addEventListener('click',function(){box.parentNode.removeChild(box);});
  var pr=document.createElement('label'),cb=document.createElement('input');
  cb.type='checkbox';cb.checked=printing();
  cb.addEventListener('change',function(){setPrint(cb.checked);});
  pr.appendChild(cb);pr.appendChild(document.createTextNode(' Print it too'));
  box.appendChild(sel);box.appendChild(pr);box.appendChild(x);document.body.appendChild(box);sel.focus();
}
})();
</script>
"""

OLD_LOAD = re.compile(r'<script id="theme-load">.*?</script>\n', re.S)
OLD_PICK = re.compile(r'<script id="theme-pick">.*?</script>\n', re.S)


def main(path):
    s = open(path, encoding="utf-8").read()
    s = OLD_PICK.sub("", OLD_LOAD.sub("", s))
    names = json.dumps([t for t, _ in THEMES])
    s = s.replace("</head>", LOAD % names + "</head>", 1)
    s = s.replace("</body>", PICK % json.dumps([list(t) for t in THEMES]) + "</body>", 1)
    open(path, "w", encoding="utf-8", newline="\n").write(s)


if __name__ == "__main__":
    main(sys.argv[1])
