for i in intro.tex
do
  fold -sw 80 $i > $i.out
  mv $i.out $i
done