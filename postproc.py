#!/usr/bin/python
import sys
f = open( sys.argv[1] )


inExEnv = False

for line in f:
    line  = line[:-1] # trailing newline removal
    if(line.count("documentclass")) :
        line = '\documentclass[11pt,oneside,a4paper,pdftex,openany]{book}'
        line += '\\usepackage{capt-of}\n\\usepackage{xcolor}'
        line += '\n\\usepackage[most]{tcolorbox}\n'
        line += '\\usepackage{tikz, lipsum}\n\\usepackage{fancyvrb}\n'
        line += '\\tcbuselibrary{breakable,skins}\n\\tcbset{enhanced jigsaw}'
        line += '\n\\newenvironment{example}{\\vspace{0.5cm}\\begin{tcolorbox}[breakable,enhanced,title='',colframe=teal,colback=teal!5!white]}{\\end{tcolorbox}\\vspace{0.5cm}}'
        line += '\n\\newenvironment{antwoord}{\\begin{tcolorbox}[enhanced,breakable, colback=grey]}{\\end{tcolorbox}}\n'

        line += '\\setlength{\\textheight}{21.5cm}\\setlength{\\textwidth}{15.0cm}\n'
        line += '\\setlength{\\topmargin}{0.0cm}\n'
        line += '\\setlength{\\oddsidemargin}{0.0cm}\n'
        line += '\\setlength{\\evensidemargin}{0.0cm}\n'
        line += '\\renewcommand{\\appendixname}{}\n'
        line += '\\renewcommand{\\chaptername}{Hoofdstuk}\n'
        line += '\\renewcommand{\\contentsname}{Inhoud}\n'
        line += '\\renewcommand{\\partname}{Module}\n'
        line += '\\graphicspath{{Figures/}}\n'
        line += '\\usepackage{titlesec}\n'
        #        line += '\\titleformat{\\chapter}[display]\n'
        line += '\\titleformat{\\chapter}[display]\n'
        line += '{\\bfseries\\Large}\n'
        line += '{\\huge{\\partname} \\huge{\\thepart} \\hfill \\huge{\\chaptertitlename} \\huge\\thechapter}\n'
        line += '{1ex}{\\titlerule\\vspace{1ex}\\huge\\filleft}\n'
        line += '[\\vspace{1ex}\\titlerule]'
        
        line += '\\titleclass{\\part}{top} % make part like a chapter\n'
        line += '\\titleformat{\\part}\n'
        line += '[display]'
        line += '{\\normalfont\\Huge\\bfseries\\filright}\n'
        line += '{\\Huge{\\partname} \\thepart}{0pt}\n'
        line += '{\\titlerule[1pt]}\\titlespacing*{\\part}{0pt}{0pt}{3pt}\n'


        
    if(line.count('usepackage{listings}')) :
        line += '\n \\lstset{breaklines=true, basicstyle=\\ttfamily, columns=fullflexible, frame=single}'
        
    if(line.count('begin{document}')) : 
        line = ''
        line += '\\newcommand*{\\titleGM}{\\begingroup\n'
        line += '\\hbox{\\parbox[b]{\\textwidth}{\n'
        line += '\\vspace{0.15\\textheight}'    
        line += '{\\center\\Huge\\bfseries {Data Analyse en Statistiek}} \\\\ [3\\baselineskip]\n'
        line += '{\\center\\huge\\bfseries {Bachelor Natuur- en Sterrenkunde}} \\\\ [3\\baselineskip]\n'
        line += '{\\center\\huge\\bfseries studiejaar 2020-2021} \\\\ [3\\baselineskip]\n'
        line += '\\vspace{0.33\\textheight} \\\\ [3\\baselineskip] \\newline\n'
        line += '{\\filleft\\includegraphics[]{logoVUvA.jpeg}}}}'
        line += '\\endgroup}'

        line += '\\begin{document}\n'
        line += '\\thispagestyle{empty}\n' 
        line += '\\titleGM\n'
        line += '\\parbox[b]{\\textwidth}{ \\vspace{0.8\\textheight}  dr H.L. Snoek \\&  M. F. L. Schut MSc \\\\  versie 2021-02-17 } \n'
        line += '\\tableofcontents\\newpage\n'

    if (line.count("begin{quote")) : 
        line = line.replace( r"\begin{quote}", r"\begin{example}" )
        inExEnv = True
    if (line.count("end{quote}")) :
        inExEnv = False
        line = line.replace( r"\end{quote}", r"\end{example}" )


    line = line.replace( r"\[", r"$" )
    line = line.replace( r"\]", r"$" )

    line = line.replace( r"$$", r"$")
    line = line.replace( r"♥" , r"$\heartsuit$")
    line = line.replace( r"♠" , r"$\spadesuit$")
    line = line.replace( r"♦" , r"$\diamondsuit$")
    line = line.replace( r"♣" , r"$\clubsuit$")
    line = line.replace( r"\displaystyle" , r"")
    line = line.replace( r"<center>" , r"")
    line = line.replace( r"</center>" , r"")
    line = line.replace( r"\lt" , r"<")
    line = line.replace( r"\gt" , r">")

#    if (line.count('LatexPart')) :
#        line = line.replace( r"chapter", r"part")
#        line = line.replace( r"LatexPart", r"")

    if (line.count('Introductie Module')) :
        line = line.replace( r"chapter", r"part")
        line = line.replace( r"Introductie Module 1", r"")
        line = line.replace( r"Introductie Module 2", r"")
        line = line.replace( r"Introductie Module 3", r"")
        line = line.replace( r"Introductie Module 4", r"")

    if (line.startswith('\\newline')) : line = ""
    
    if (line.count('.png}')) :
        w = '1.0'
        if (line.count('\%'))  :
            width = line[line.find('=')+3:line.find('%')-1]
            if (width == '100') : w='1.0'
            if (width == '60') : w='0.6'
            if (width == '65') : w='0.65'
            if (width == '50') : w='0.5'
            if (width == '45') : w='0.5'
            if (width == '40') : w='0.5'
            if (width == '30') : w='0.5'
            if (width == '80') : w='0.8'
        if (line.count('400px'))  :
            w='0.45'

        if (inExEnv) :
            temp_line = "{\\begin{center}"
            temp_line += line[0:line.find('{')]+'[width='+w+'\\textwidth]'+line[line.find('{'):line.find('}')+1]
#            temp_line += "\\end{center}}"

        else : 
            temp_line = '\\begin{figure}[h!]\n\\centering\n'
            temp_line += line[0:line.find('{')]+'[width='+w+'\\textwidth]'+line[line.find('{'):line.find('}')+1]
#            temp_line += '\n\\end{figure}'
        line = temp_line


    if (line.count('\label{fig')) :
        if (inExEnv) : line += "\\end{center}}"
        else : line += '\n\\end{figure}'

    line = line.replace( r'\hypersetup{', r' \hypersetup{colorlinks=true, linkcolor =blue,')

    #dit werkt niet.. hoe moet hij uit de while loop komen als er een py template fo http is?
    #tel of er meer hrefs zijn dan py template en http...

    
    go = line.count('\\href')
    if (go) :
        start = line.find('\href')
        mid = line.find('}',start)
        end = line.find('}',mid+1)
        while(go) : 
            front_line = line[0:start]
            fix_line = line[start:end+1]
            end_line = line[end+1:]
            #            print('font_line ', front_line)
            #            print('fix_line ', fix_line)
            #            print('end_line ', end_line)
            go = end_line.count('\\href')
            #            print('go ',go)
            if ((fix_line.count('http')==0) & (fix_line.count('.py')==0) & (fix_line.count('.docx')==0)) :
                temp_line = front_line
                temp_line += line[mid+2:end]
                temp_line += ' (Hfdst. \\'+line[start+2:mid+1]+')'
                temp_line += end_line
                line = temp_line
            start = line.find('\href',end)
            mid = line.find('}',start)
            end = line.find('}',mid+1)
            
    l = line
    print(l)

