#!/usr/bin/python
import sys
f = open( sys.argv[1] )

for line in f:

    line  = line[:-1] # trailing newline removal

    line = line.replace( r"\[", r"\begin{equation*}" )
    line = line.replace( r"\]", r"\end{equation*}" )
    if line.startswith('$$') :
        line = line.replace( r"$$", r"\begin{equation}",1 )
        line = line.replace( r"$$", r"\end{equation}",1 )
        
    if line.startswith('\> $$') :
        line = line.replace( r"$$", r"\begin{equation}",1 )
        line = line.replace( r"$$", r"\end{equation}",1 )
    
    line = line.replace( r"<br>", r"\newline")
    line = line.replace( r"#", r"##",1 )
    
    l = line    


    print(l)

