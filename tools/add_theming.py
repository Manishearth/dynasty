#!/usr/bin/env python3
"""Put the theme loader and the hidden theme picker into a page.

Usage: python3 tools/add_theming.py rulebook.html
Idempotent: earlier theme scripts are stripped before they are re-added.

The themes are stylesheets in style/themes/; with none, the page keeps the
original look from style/base.css. The scripts are written into each page rather
than loaded from a .js file, so that they work when the page is opened straight
from disk. The page marks its title with data-theme-unlock: five quick clicks on
it show the picker. The choice is kept in localStorage, which every page shares,
and applies to print as well; html[data-theme] tells the page's own print rules
(the rulebook's white cover) to step aside for the theme.
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
    ("flatpack", "Flat-Pack"),
    ("safety", "Safety Card"),
    ("swiss", "Swiss Style"),
    ("wargame", "Hex & Counter"),
    ("bookshelf", "Bookshelf Game"),
    ("handmedown", "Hand-Me-Down"),
]

LOAD = """<script id="theme-load">
/* Apply the saved theme before the page draws (tools/add_theming.py). */
(function(){
var t,q=/[?&]theme=([\\w-]+)/.exec(location.search);
try{t=localStorage.getItem('dynasty-theme')}catch(e){}
/* ?theme=name for testing, and for printing from a fresh browser */
if(q)t=q[1];
if(t&&%s.indexOf(t)>0){
  document.write('<link rel="stylesheet" id="theme-css" href="style/themes/'+t+'.css">');
  document.documentElement.setAttribute('data-theme',t);
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
    if(!l){l=document.createElement('link');l.rel='stylesheet';l.id='theme-css';document.head.appendChild(l);}
    l.href='style/themes/'+t+'.css';document.documentElement.setAttribute('data-theme',t);
  }
  try{localStorage.setItem('dynasty-theme',t)}catch(e){}
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
  box.appendChild(sel);box.appendChild(x);document.body.appendChild(box);sel.focus();
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
