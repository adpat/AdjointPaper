fold -sw 80 $1 > $1.out; mv $1.out $1; ./indenter/latexindent.pl -w $1
